from util.DataFrame import globalFrame

import time
import pandas as pd
import threading
import requests
from config import getIP


class Curtain():
    def __init__(self, room_name, space, device_name):
        super().__init__()
        self.df_lock = threading.Lock()
        self.df = pd.DataFrame(columns=('Name', 'Type', 'Location', 'Object', 'Timestamp', 'Payload Data', 'Source'))
        self.space = space
        self.device_name = device_name
        self.room_name = room_name
        self.lock = threading.Lock()
        self.running = threading.Event()
        self.flag_on = threading.Event()
        self.flag_off = threading.Event()
        
    def _enable_on(self):
        if self.ap_on() == '1':
            return 0
        else:
            return 1

    def action_on(self, env, source): 
        self.lock.acquire()
        if self._enable_on():
            url = getIP() + "/set_device_value/" + self.room_name + "/" + self.device_name + "/1"
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room_name + '.' + self.device_name + '.state: on 成功')
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["curtain_on", "Action", self.room_name, self.device_name, Time, self.room_name + '.' + self.device_name + '.state: 1', source]
                globalFrame.afterDeal(env, "curtain_on", self.room_name, self.room_name + '.' + self.device_name + '.state: 1', self.space)
                self.flag_on.set()
                self.flag_off.clear()
            else:
                print(self.room_name + '.' + self.device_name + '.state: on 失败')
        else:
            self.lock.release()

    def effect_on(self, env): 
        inner_state = env["space_dict"][self.room_name]["env_state"]["Brightness"]
        outer_state = env["space_dict"]["Context"]["env_state"]["Brightness"]
        while not self.running.is_set():
            while self.flag_on.is_set() and not self.running.is_set():
                interval = int(outer_state.ap_value()) - int(inner_state.ap_value())
                if interval > 0:
                    inner_state.set_value(interval/2)
                time.sleep(0.08)
            time.sleep(0.08)
    
    def effect_off(self, env):
        inner_state = env["space_dict"][self.room_name]["env_state"]["Brightness"]
        outer_state = env["space_dict"]["Context"]["env_state"]["Brightness"]
        while not self.running.is_set():
            if self.flag_off.is_set():
                if int(outer_state.ap_value()) > int(inner_state.ap_value()):
                    inner_state.set_value(-1.2)
                while self.flag_off.is_set() and not self.running.is_set(): 
                    time.sleep(0.08)
            time.sleep(0.08)

    def _enable_off(self):
        if self.ap_on() == '0':
            return 0
        else:
            return 1

    def action_off(self, env, source):    
        self.lock.acquire()    
        if self._enable_off():
            url = getIP() + "/set_device_value/" + self.room_name + "/" + self.device_name + "/0"
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room_name + '.' + self.device_name + '.state: off 成功')
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["curtain_off", "Action", self.room_name, self.device_name, Time, self.room_name + '.' + self.device_name + '.state: 0', source]
                globalFrame.afterDeal(env, "curtain_off", self.room_name, self.room_name + '.' + self.device_name + '.state: 0', self.space)
                self.flag_off.set()
                self.flag_on.clear()
            else:
                print(self.room_name + '.' + self.device_name + '.state: off 失败')
        else:
            self.lock.release()
            
    def ap_on(self):
        url = getIP() + "/room_device_info/" + self.room_name + "/" + self.device_name
        value = requests.get(url).json()
        return str(value["state"])
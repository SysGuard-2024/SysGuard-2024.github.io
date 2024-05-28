import threading

from DeviceController.DeviceController import *
from util.DataFrame import globalFrame
import time
import requests
import pandas as pd
from config import getIP

class HumanState():
    def __init__(self, room, space):
        super().__init__()
        self.df_lock = threading.Lock()
        self.df = pd.DataFrame(columns=('Name', 'Type', 'Location', 'Object', 'Timestamp', 'Payload Data', 'Source'))
        self.space = space
        self.room = room
        
        self.count_lock = threading.Lock()
        self.lock = threading.Lock()

    def _enable_decrease(self):
        v = self.ap_value()
        if v == '0':
            return 0
        else:
            return 1

    def _enable_increase(self):
        v = self.ap_value()
        if v == '1':
            return 0
        else:
            return 1

    def ext_action_decrease(self,env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.count_lock.acquire()
        url = getIP() + "/room_state_info/" + self.room + "/HumanCount"
        count = (requests.get(url).json())["value"]
        self.count_lock.release()
        if count == 0:
            self.lock.acquire()
            if self._enable_decrease():
                url = getIP() + "/set_state_value/" + self.room + "/HumanState/0"
                response = requests.post(url)   
                self.lock.release()
                if response.status_code == 200:
                    print(self.room + " human_detected false 成功")
                    with self.df_lock:
                        self.df.loc[len(self.df)] = ["human_undetected", "Event", self.room, 'HumanState', Time, self.room + '.HumanState.state: 0', 'Environment Change']
                    globalFrame.afterDeal(env, "human_undetected", self.room, self.room + '.HumanState.state: 0', self.space)
                else:
                    print(self.room + " human_detected false 失败")
            else:
                self.lock.release()
                     
    def ext_action_increase(self, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.count_lock.acquire()
        url = getIP() + "/room_state_info/" + self.room + "/HumanCount"
        count = (requests.get(url).json())["value"]
        self.count_lock.release()
        if count == 1:
            self.lock.acquire()
            if self._enable_increase():
                url = getIP() + "/set_state_value/" + self.room + "/HumanState/1"
                response = requests.post(url)
                self.lock.release()
                if response.status_code == 200:
                    print(self.room + " human_detected true 成功")
                    with self.df_lock:
                        self.df.loc[len(self.df)] = ["human_detected", "Event", self.room, 'HumanState', Time, self.room + '.HumanState.state: 1', 'Environment Change']
                    globalFrame.afterDeal(env, "human_detected", self.room, self.room + '.HumanState.state: 1', self.space)
                else:
                    print(self.room + " human_detected true 失败")
            else:
                self.lock.release()              
            
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/HumanState"
        value = requests.get(url).json()
        return str(value["value"])
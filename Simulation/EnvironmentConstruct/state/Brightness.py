import threading

from util.DataFrame import globalFrame
import time
import requests
import pandas as pd
from config import getIP


class Brightness(): # -2 -1 0 1

    def __init__(self, room,space):
        super().__init__()
        self.df_lock = threading.Lock()
        self.df = pd.DataFrame(columns=('Name', 'Type', 'Location', 'Object', 'Timestamp', 'Payload Data', 'Source'))
        self.space = space
        self.room = room
        self.lock = threading.Lock()
        self.value = 0
        self.value_lock = threading.Lock()
        self.running = threading.Event()

    def set_value(self, value):
        with self.value_lock:
            self.value = self.value + value

    def calculate(self, env):
        while not self.running.is_set():
            self.value_lock.acquire()
            if self.value >= 2:
                self.value = 0
                self.value_lock.release()
                self.ext_action_increase(env)
                self.ext_action_increase(env)
            elif 1 <= self.value and self.value < 2.0:
                self.value = 0
                self.value_lock.release()
                self.ext_action_increase(env)
            elif -2.0 <= self.value and self.value <= -1:
                self.value = 0
                self.value_lock.release()
                self.ext_action_decrease(env)
            elif self.value < -2:
                self.value = 0
                self.value_lock.release()
                self.ext_action_decrease(env)
                self.ext_action_decrease(env)
            else:
                self.value_lock.release()
            time.sleep(0.05)

    def _enable_decrease(self):
        if self.ap_value() == '-2':
            return 0
        else:
            return 1

    def _enable_increase(self):
        if self.ap_value() == '1':
            return 0
        else:
            return 1

    def ext_action_decrease(self, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.lock.acquire()
        if self._enable_decrease():
            value = str(int(self.ap_value()) - 1)
            url = getIP() + "/set_state_value/" + self.room + "/Brightness/" + value
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room + " brightness_down 成功")
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["brightness_down", "Event", self.room, 'Brightness', Time, self.room + '.Brightness.state: ' + value, 'Environment Change']
                globalFrame.afterDeal(env, "brightness_down", self.room, self.room + '.Brightness.state: ' + value, self.space)
            else:
                print(self.room + " brightness_down 失败")
        else:
            self.lock.release()

    def ext_action_increase(self, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.lock.acquire()
        if self._enable_increase():
            value = str(int(self.ap_value()) + 1)
            url = getIP() + "/set_state_value/" + self.room + "/Brightness/" + value
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room + " brightness_up 成功")
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["brightness_up", "Event", self.room, 'Brightness', Time, self.room + '.Brightness.state: ' + value, 'Environment Change']
                globalFrame.afterDeal(env, "brightness_up", self.room, self.room + '.Brightness.state: ' + value, self.space)
            else:
                print(self.room + "  失败")
        else:
            self.lock.release()
                         
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/Brightness"
        value = requests.get(url).json()
        return str(value["value"])
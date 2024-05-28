import threading

from DeviceController.DeviceController import *
from util.DataFrame import globalFrame
import time
import requests
import pandas as pd
from config import getIP

class HumanCount():
    def __init__(self, room, space):
        super().__init__()
        self.df_lock = threading.Lock()
        self.df = pd.DataFrame(columns=('Name', 'Type', 'Location', 'Object', 'Timestamp', 'Payload Data', 'Source'))
        self.space = space
        self.room = room
        self.lock = threading.Lock()

    def _enable_decrease(self):
        v = self.ap_value()
        if v == '0':
            return 0
        else:
            return 1

    def _enable_increase(self):
        return 1

    def ext_action_decrease(self,env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.lock.acquire()
        if self._enable_decrease():
            value = str(int(self.ap_value()) - 1)
            url = getIP() + "/set_state_value/" + self.room + "/HumanCount/" + value
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room + " human_leaved 成功")
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["human_leaved", "Event", self.room, 'HumanCount', Time, self.room + '.HumanCount.state: ' + value, 'Environment Change']
                globalFrame.afterDeal(env, "human_leaved", self.room, self.room + '.HumanCount.state: ' + value, self.space)
            else:
                print(self.room + " human_leaved 失败")
        else:
            self.lock.release()
                     
    def ext_action_increase(self, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.lock.acquire()
        if self._enable_increase():
            value = str(int(self.ap_value()) + 1)
            url = getIP() + "/set_state_value/" + self.room + "/HumanCount/" + value
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room + " human_entered 成功")
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["human_entered", "Event", self.room, 'HumanCount', Time, self.room + '.HumanCount.state: ' + value, 'Environment Change']
                globalFrame.afterDeal(env, "human_entered", self.room, self.room + '.HumanCount.state: ' + value, self.space)
                if value == 10:
                  t1 = threading.Thread(target=self.AirQualityEffect, args=(env,))
                  t1.start()
                  globalFrame.thread_list.append(t1)
            else:
                print(self.room + " human_entered 失败")
        else:
            self.lock.release()
    
    def AirQualityEffect(self, env):
        time.sleep(0.6*20)
        self.lock.acquire()
        if self.ap_value() >= 10:
            self.lock.release()
            t1 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list, self.room, "AirQuality", env, ))
            t1.start()
            globalFrame.thread_list.append(t1)
            t1 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list, self.room, "Co2Level", env, ))
            t1.start()
            globalFrame.thread_list.append(t1)  
        else:
          self.lock.release()               
            
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/HumanCount"
        value = requests.get(url).json()
        return str(value["value"])
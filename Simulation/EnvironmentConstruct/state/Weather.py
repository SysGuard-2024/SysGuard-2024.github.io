import threading
import time

import pandas as pd
from util.DataFrame import globalFrame
import requests
from config import getIP

class Weather():
    def __init__(self, room,space):
        super().__init__()
        self.df_lock = threading.Lock()
        self.df = pd.DataFrame(columns=('Name', 'Type', 'Location', 'Object', 'Timestamp', 'Payload Data', 'Source'))
        self.space = space
        self.room = room
        self.lock = threading.Lock()

    def _enable_change(self, value):
        if self.ap_value() == value:
            return 0
        else:
            return 1

    def ext_action_change(self, value, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        self.lock.acquire()
        if self._enable_change(value):
            url = getIP() + "/set_state_value/" + self.room + "/Weather/" + value
            response = requests.post(url)
            self.lock.release()
            if response.status_code == 200:
                print(self.room + " Weather " + value + " 成功")
                with self.df_lock:
                    self.df.loc[len(self.df)] = ["weather_change", "Event", self.room, 'Weather', Time, self.room + '.Weather.state: ' + value, 'Environment Change']
                globalFrame.afterDeal(env, "weather_change", self.room, self.room + '.Weather.state: ' + value, self.space)
            else:
                print(self.room + " Weather " + value + " 失败")
        else:
            self.lock.release()
                
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/Weather"
        value = requests.get(url).json()
        return str(value["value"])
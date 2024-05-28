import threading
from Characterization.device.AC import AC
from Characterization.device.AirPurifier import AirPurifier
from Characterization.device.BathHeater import BathHeater
from Characterization.device.Curtain import Curtain
from Characterization.device.Door import Door
from Characterization.device.GasStove import GasStove
from Characterization.device.Heater import Heater
from Characterization.device.Humidifier import Humidifier
from Characterization.device.MicrowaveOven import MicrowaveOven
from Characterization.device.TV import TV
from Characterization.device.Light import Light
from Characterization.device.Printer import Printer
from Characterization.device.Speaker import Speaker
from Characterization.device.WaterDispenser import WaterDispenser
from Characterization.device.Window import Window
from Characterization.state.AirQuality import AirQuality
from Characterization.state.Brightness import Brightness
from Characterization.state.Co2Level import Co2Level
from Characterization.state.EnergyConsumtion import EnergyConsumption
from Characterization.state.HumanCount import HumanCount
from Characterization.state.HumanState import HumanState
from Characterization.state.Humidity import Humidity
from Characterization.state.Noise import Noise
from Characterization.state.Temperature import Temperature
from Characterization.state.Weather import Weather
from Characterization.device.TowelDryer import TowelDryer
from Characterization.device.WashingMachine import WashingMachine
from Characterization.device.WaterHeater import WaterHeater
from Characterization.device.Fridge import Fridge
from Characterization.device.CookerHood import CookerHood

import requests
from config import getIP

def getEnvonment(ip,space):
    env = dict()
    space_dict = dict()
    url = ip + "/room_list"
    room_list = requests.get(url).json()
    for room in room_list:
        device_dict = dict()
        env_state = dict()
        
        url = ip + "/room_state/" + room
        room_state = requests.get(url).json()

        for state in room_state:
            match state:
                case "Temperature":
                    env_state["Temperature"] = Temperature(room,space)
                case "Co2Level":
                    env_state["Co2Level"] = Co2Level(room,space)
                case "EnergyConsumption":
                    env_state["EnergyConsumption"] = EnergyConsumption(room,space)
                case "Brightness":
                    env_state["Brightness"] = Brightness(room,space)
                case "AirQuality":
                    env_state["AirQuality"] = AirQuality(room,space)
                case "HumanState":
                    env_state["HumanState"] = HumanState(room,space)
                case "HumanCount":
                    env_state["HumanCount"] = HumanCount(room,space)
                case "Humidity":
                    env_state["Humidity"] = Humidity(room,space)
                case "Noise":
                    env_state["Noise"] = Noise(room,space)
                case "Weather":
                    env_state["Weather"] = Weather(room,space)

        url = ip + "/room_device/" + room
        room_device = requests.get(url).json()

        for device in room_device:
            match device[:-3]:
                case "AC":
                    device_dict[device] = AC(room,space,device)
                case "GasStove":
                    device_dict[device] = GasStove(room,space,device)
                case "Window":
                    device_dict[device] = Window(room,space,device)
                case "Light":
                    device_dict[device] = Light(room,space,device)
                case "Curtain":
                    device_dict[device] = Curtain(room,space,device)
                case "Door":
                    device_dict[device] = Door(room,space,device)
                case "Heater":
                    device_dict[device] = Heater(room,space,device)
                case "Humidifier":
                    device_dict[device] = Humidifier(room,space,device)
                case "MicrowaveOven":
                    device_dict[device] = MicrowaveOven(room,space,device)
                case "Printer":
                    device_dict[device] = Printer(room,space,device)
                case "AirPurifier":
                    device_dict[device] = AirPurifier(room,space,device)
                case "Speaker":
                    device_dict[device] = Speaker(room,space,device)
                case "TV":
                    device_dict[device] = TV(room,space,device)
                case "WaterDispenser":
                    device_dict[device] = WaterDispenser(room,space,device)
                case "Fridge":
                    device_dict[device] = Fridge(room,space,device)
                case "WaterHeater":
                    device_dict[device] = WaterHeater(room,space,device)
                case "TowelDryer":
                    device_dict[device] = TowelDryer(room,space,device)
                case "WashingMachine":
                    device_dict[device] = WashingMachine(room,space,device)
                case "CookerHood":
                    device_dict[device] = CookerHood(room,space,device)
                case "BathHeater":
                    device_dict[device] = BathHeater(room,space,device)

        room_temp = dict()
        room_temp["device_dict"] = device_dict
        room_temp["env_state"] = env_state
        space_dict[room] = room_temp

    env["space_dict"] = space_dict
    return env

env = None

def setEnv(space):
    global env
    env = getEnvonment(getIP(),space)
    for room in env["space_dict"]:
        for device in env["space_dict"][room]["device_dict"]:
            dev = env["space_dict"][room]["device_dict"][device]
            dev.df.drop(dev.df.index, inplace=True)
            threading.Thread(target=dev.effect_on, args=(env, )).start()
            threading.Thread(target=dev.effect_off, args=(env, )).start()
        for state in env["space_dict"][room]["env_state"]: 
            st = env["space_dict"][room]["env_state"][state] 
            st.df.drop(st.df.index, inplace=True)
            if state not in ["HumanState", "HumanCount", "Weather"]:
                threading.Thread(target=st.calculate, args=(env, )).start()
            if state == "Temperature":
                threading.Thread(target=st.change_to_outer, args=(env, )).start()               
    
def getEnv():
    global env
    return env


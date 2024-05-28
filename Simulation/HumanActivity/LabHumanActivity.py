import threading
import time
import random
import datetime
from Characterization.Environment import env
from util.DataFrame import globalFrame
from AutomatedApplication.application.labApplication import *

lab_device_list = [
    [deviceOn, ["Lab", "Curtain001"]],
    [deviceOff, ["Lab", "Curtain001"]],
    [deviceOn, ["Lab", "Curtain002"]],
    [deviceOff, ["Lab", "Curtain002"]],
    [deviceOn, ["Lab", "Door001"]],
    [deviceOff, ["Lab", "Door001"]],
    [deviceOn, ["Lab", "AC001"]],
    [deviceOff, ["Lab", "AC001"]],
    [deviceOn, ["Lab", "Printer001"]],
    [deviceOn, ["Lab", "AirPurifier001"]],
    [deviceOff, ["Lab", "AirPurifier001"]],
    [deviceOn, ["Lab", "Light001"]],
    [deviceOff, ["Lab", "Light001"]],
    [deviceOn, ["Lab", "Light002"]],
    [deviceOff, ["Lab", "Light002"]],
    [deviceOn, ["Lab", "Light003"]],
    [deviceOff, ["Lab", "Light003"]],
    [deviceOn, ["Lab", "Light004"]],
    [deviceOff, ["Lab", "Light004"]],
    [deviceOn, ["Lab", "Humidifier001"]],
    [deviceOff, ["Lab", "Humidifier001"]],
    [deviceOn, ["Lab", "Window002"]],
    [deviceOff, ["Lab", "Window002"]],
    [deviceOn, ["Lab", "Window001"]],
    [deviceOff, ["Lab", "Window001"]]],

# meetingroom_one_device_list = [
#     [deviceOn, ["MeetingRoomOne", "Curtain001"]],
#     [deviceOff, ["MeetingRoomOne", "Curtain001"]],
#     [deviceOn, ["MeetingRoomOne", "Door001"]],
#     [deviceOff, ["MeetingRoomOne", "Door001"]],
#     [deviceOn, ["MeetingRoomOne", "AC001"]],
#     [deviceOff, ["MeetingRoomOne", "AC001"]],
#     [deviceOn, ["MeetingRoomOne", "AirPurifier001"]],
#     [deviceOff, ["MeetingRoomOne", "AirPurifier001"]],
#     [deviceOn, ["MeetingRoomOne", "Light001"]],
#     [deviceOff, ["MeetingRoomOne", "Light001"]],
#     [deviceOn, ["MeetingRoomOne", "Humidifier001"]],
#     [deviceOff, ["MeetingRoomOne", "Humidifier001"]],
#     [deviceOn, ["MeetingRoomOne", "TV001"]],
#     [deviceOff, ["MeetingRoomOne", "TV001"]],
#     [deviceOn, ["MeetingRoomOne", "Window001"]],
#     [deviceOff, ["MeetingRoomOne", "Window001"]]],

# meetingroom_two_device_list = [
#     [deviceOn, ["MeetingRoomTwo", "Curtain001"]],
#     [deviceOff, ["MeetingRoomTwo", "Curtain001"]],
#     [deviceOn, ["MeetingRoomTwo", "Door001"]],
#     [deviceOff, ["MeetingRoomTwo", "Door001"]],
#     [deviceOn, ["MeetingRoomTwo", "AC001"]],
#     [deviceOff, ["MeetingRoomTwo", "AC001"]],
#     [deviceOn, ["MeetingRoomTwo", "AirPurifier001"]],
#     [deviceOff, ["MeetingRoomTwo", "AirPurifier001"]],
#     [deviceOn, ["MeetingRoomTwo", "Light001"]],
#     [deviceOff, ["MeetingRoomTwo", "Light001"]],
#     [deviceOn, ["MeetingRoomTwo", "Humidifier001"]],
#     [deviceOff, ["MeetingRoomTwo", "Humidifier001"]],
#     [deviceOn, ["MeetingRoomTwo", "TV001"]],
#     [deviceOff, ["MeetingRoomTwo", "TV001"]],
#     [deviceOn, ["MeetingRoomTwo", "Window001"]],
#     [deviceOff, ["MeetingRoomTwo", "Window001"]]],

# tearoom_device_list = [
#     [deviceOn, ["TeaRoomTwo", "Curtain001"]],
#     [deviceOff, ["TeaRoomTwo", "Curtain001"]],
#     [deviceOn, ["TeaRoomTwo", "Door001"]],
#     [deviceOff, ["TeaRoomTwo", "Door001"]],
#     [deviceOn, ["TeaRoomTwo", "AirPurifier001"]],
#     [deviceOff, ["TeaRoomTwo", "AirPurifier001"]],
#     [deviceOn, ["TeaRoomTwo", "Light001"]],
#     [deviceOff, ["TeaRoomTwo", "Light001"]],
#     [deviceOn, ["TeaRoomTwo", "Humidifier001"]],
#     [deviceOff, ["TeaRoomTwo", "Humidifier001"]],
#     [deviceOn, ["TeaRoomTwo", "Window001"]],
#     [deviceOff, ["TeaRoomTwo", "Window001"]],
#     [deviceOn, ["TeaRoomTwo", "WaterDispenser001"]],
#     [deviceOn, ["TeaRoomTwo", "MicrowaveOven001"]]],
    
random_event_list = [CatchWater, GoRestRoom, HaveLunch, Reservation]

def test():
    deviceOff(globalFrame.thread_list, "Lab","AC001", env, 'User Activity')
    deviceOff(globalFrame.thread_list, "Lab","Window001", env, 'User Activity')
    time.sleep(5)
    deviceOn(globalFrame.thread_list, "Lab","AC001", env, 'User Activity')
    deviceOn(globalFrame.thread_list, "Lab","Window001", env, 'User Activity')

def personOne():
    time.sleep(random.uniform(0.6*60*8.5, 0.6*60*9.2))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    t1 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Humidifier001", env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(0.6, 5*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t2 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t2.start()
    time.sleep(random.uniform(0.6, 5*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    time.sleep(random.uniform(60*0.6, 80*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t4 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t4.start()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(10*0.6, 20*0.6))
    if random.randint(0, 1) == 0:
        have_lunch = threading.Thread(target=HaveLunch)
        have_lunch.start()
        have_lunch.join()
        time.sleep(random.uniform(90*0.6, 120*0.6))
    else:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(10*0.6, 120*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        if t < 65*0.6:
            time.sleep(random.uniform((70-t)*0.6, (110-t)*0.6))
    time.sleep(random.uniform(1*0.6, 3*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t5 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t5.start()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()
    time.sleep(random.uniform(50*0.6, 90*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        time.sleep(random.uniform(5*0.6, 20*0.6))
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
    time.sleep(random.uniform(5*0.6, 20*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(100*0.6, 130*0.6))
    t6 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "AC001", env, 'User Activity',))
    t6.start()
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
 

def personTwo():
    pool = []
    time.sleep(random.uniform(0.6*60*8.8, 0.6*60*9))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(30*0.6, 60*0.6))
    t2 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Printer001", env, 'User Activity',))
    t2.start()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(60*0.6, 120*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(1*0.6, 3*0.6))
    if random.randint(0, 2) == 0:
        have_lunch = threading.Thread(target=HaveLunch)
        have_lunch.start()
        have_lunch.join()
        time.sleep(random.uniform(60*0.6, 90*0.6))
    else:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(10*0.6, 90*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        if t < 55*0.6:
            time.sleep(random.uniform((60-t)*0.6, (90-t)*0.6))
    time.sleep(random.uniform(1*0.6, 3*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    time.sleep(random.uniform(30*0.6, 60*0.6))
    catch_water = threading.Thread(target=CatchWater)
    catch_water.start()
    catch_water.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()
    time.sleep(random.uniform(120*0.6, 150*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t4 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t4.start()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t5 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t5.start()
    time.sleep(random.uniform(0.6*30, 0.6*45))
    t6 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Window001", env, 'User Activity',))
    t6.start()
    t7 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Window002", env, 'User Activity',))
    t7.start()
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    
    for item in pool:
        item.join()


def personThree():
    pool = []
    time.sleep(random.uniform(0.6*60*8, 0.6*60*9))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    pool.append(t1)
    time.sleep(random.uniform(90*0.6, 110*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t2 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t2.start()
    pool.append(t2)
    time.sleep(random.uniform(30*0.6, 60*0.6))
    rest_room = threading.Thread(target=GoRestRoom)
    rest_room.start()
    rest_room.join()
    time.sleep(random.uniform(80*0.6, 100*0.6))
    have_lunch = threading.Thread(target=HaveLunch)
    have_lunch.start()
    have_lunch.join()
    time.sleep(random.uniform(80*0.6, 100*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    pool.append(t3)
    time.sleep(random.uniform(15*0.6, 30*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 100*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(120*0.6, 150*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        time.sleep(random.uniform(20*0.6, 50*0.6))
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(5*0.6, 15*0.6))
    else:
        time.sleep(random.uniform(30*0.6, 60*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t4 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t4.start()
    pool.append(t4)    
    time.sleep(random.uniform(0.6, 0.6*2))
    t5 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Printer001", env, 'User Activity',))
    t5.start()
    pool.append(t5)
    time.sleep(random.uniform(15*0.6, 30*0.6))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    for item in pool:
        item.join()


def personFour():
    pool = []
    time.sleep(random.uniform(0.6*60*8.3, 0.6*60*9.1))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(90*0.6, 150*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    pool.append(t1)
    time.sleep(random.uniform(0.6, 0.6*2))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(50*0.6, 110*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(40*0.6, 70*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t2 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t2.start()
    pool.append(t2)
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(30*0.6, 40*0.6))
    else:
        time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    pool.append(t3)
    time.sleep(random.uniform(30*0.6, 60*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t4 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t4.start()
    pool.append(t4)
    time.sleep(random.uniform(120*0.6, 180*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 40*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(5*0.6, 15*0.6))
    else:
        time.sleep(random.uniform(30*0.6, 60*0.6))
    time.sleep(random.uniform(0.6, 0.6*2))
    if random.randint(0, 1) == 0:
        t5 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Light001", env, 'User Activity',))
        t5.start()
        pool.append(t5)
    if random.randint(0, 1) == 0:
        t5 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Light002", env, 'User Activity',))
        t5.start()
        pool.append(t5)
    if random.randint(0, 1) == 0:
        t5 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Light003", env, 'User Activity',))
        t5.start()
        pool.append(t5)
    if random.randint(0, 1) == 0:
        t5 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Light004", env, 'User Activity',))
        t5.start()
        pool.append(t5)
    time.sleep(random.uniform(75*0.6, 80*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t6 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t6.start()
    pool.append(t6)
    time.sleep(random.uniform(0.1, 0.15))
    t5 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Light001", env, 'User Activity',))
    t5.start()
    pool.append(t5)
    t5 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Light002", env, 'User Activity',))
    t5.start()
    pool.append(t5)
    t5 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Light003", env, 'User Activity',))
    t5.start()
    pool.append(t5)
    t5 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Light004", env, 'User Activity',))
    t5.start()
    pool.append(t5)
    time.sleep(random.uniform(0.1, 0.15))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    for item in pool:
        item.join()


def personFive():
    pool = []
    time.sleep(random.uniform(0.6*60*8.5, 0.6*60*8.9))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6*5, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    pool.append(t1)
    time.sleep(random.uniform(0.6*8, 0.6*15))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(60*0.6, 80*0.6))
    else:
        t_window = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Window001", env, 'User Activity',))
        t_window.start()
        pool.append(t_window)
        time.sleep(random.uniform(90*0.6, 110*0.6))
    t2 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Printer001", env, 'User Activity',))
    t2.start()
    pool.append(t2)
    time.sleep(random.uniform(90*0.6, 110*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*3, 0.6*15))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    pool.append(t3)
    time.sleep(random.uniform(90*0.6, 100*0.6))
    t4 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Curtain001", env, 'User Activity',))
    t4.start()
    pool.append(t4)
    time.sleep(random.uniform(70*0.6, 95*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomTwo",))
    meeting.start()
    meeting.join()
    time.sleep(random.uniform(0.6*8, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 70*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(40*0.6, 50*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*8, 0.6*15))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    for item in pool:
        item.join()


def personSix():
    pool = []
    time.sleep(random.uniform(0.6*60*8.6, 0.6*60*9.1))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    random_device = random.randint(0, len(lab_device_list)-1)
    t = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t.start()
    pool.append(t)
    time.sleep(random.uniform(60*0.6, 90*0.6))
    # random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "Humidifier001", env, 'User Activity',))
    t1.start()
    pool.append(t1)
    time.sleep(random.uniform(90*0.6, 120*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomTwo",))
    meeting.start()
    meeting.join()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    t2 = threading.Thread(target=deviceOn, args=(globalFrame.thread_list, "Lab", "AC001", env, 'User Activity',))
    t2.start()
    pool.append(t2)
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(60*0.6, 110*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    pool.append(t3)
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
    else:
        time.sleep(random.uniform(20*0.6, 40*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t4 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t4.start()
    pool.append(t4)
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(120*0.6, 150*0.6))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    for item in pool:
        item.join()


def personSeven():
    time.sleep(random.uniform(0.6*60*8, 0.6*60*9))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(60*0.6, 120*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(60*0.6, 120*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()

    time.sleep(random.uniform(60*0.6, 120*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t2 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t2.start()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(50*0.6, 60*0.6))
    else:
        time.sleep(random.uniform(90*0.6, 120*0.6))
    t3 = threading.Thread(target=deviceOff, args=(globalFrame.thread_list, "Lab", "Door001", env, 'User Activity',))
    t3.start()
    time.sleep(random.uniform(40*0.6, 70*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t4 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t4.start()
    time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t5 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t5.start()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(30*0.6, 45*0.6))
    else:
        time.sleep(random.uniform(60*0.6, 90*0.6))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def personEight():
    pool = []
    time.sleep(random.uniform(0.6*60*8, 0.6*60*8.9))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(15*0.6, 30*0.6))
    water = threading.Thread(target=CatchWater)
    water.start()
    water.join()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(40*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(80*0.6, 100*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    random_device = random.randint(0, len(lab_device_list)-1)
    t2 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t2.start()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(30*0.6, 40*0.6))
    else:
        time.sleep(random.uniform(50*0.6, 100*0.6))
    restRoom = threading.Thread(target=GoRestRoom)
    restRoom.start()
    restRoom.join()
    time.sleep(random.uniform(10*0.6, 30*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(100*0.6, 110*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t3 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t3.start()
    time.sleep(random.uniform(60*0.6, 70*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    for item in pool:
        item.join()


def personNine():
    pool = []
    time.sleep(random.uniform(0.6*60*8.5, 0.6*60*9.2))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 90*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(60*0.6, 70*0.6))
    else:
        time.sleep(random.uniform(90*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 90*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(70*0.6, 100*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    for item in pool:
        item.join()


def personTen():
    pool = []
    time.sleep(random.uniform(0.6*60*8.6, 0.6*60*8.9))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(60*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(60*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(20*0.6, 30*0.6))
    else:
        time.sleep(random.uniform(40*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room, ))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 60*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(60*0.6, 75*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(150*0.6, 160*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    for item in pool:
        item.join()


def weekendPersonOne():
    time.sleep(random.uniform(0.6*60*10, 0.6*60*12))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(30*0.6, 50*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        time.sleep(random.uniform(20*0.6, 50*0.6))
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(20*0.6, 40*0.6))
    else:
        time.sleep(random.uniform(60*0.6, 80*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*15, 0.6*45))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()


def weekendPersonTwo():
    time.sleep(random.uniform(0.6*60*10, 0.6*60*14))
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(30*0.6, 50*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(5*0.6, 10*0.6))
    else:
        time.sleep(random.uniform(30*0.6, 50*0.6))
    time.sleep(random.uniform(10*0.6, 15*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t1 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t1.start()
    time.sleep(random.uniform(0.6*15, 0.6*45))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    random_device = random.randint(0, len(lab_device_list)-1)
    t2 = threading.Thread(target=lab_device_list[0][random_device][0], args=(globalFrame.thread_list, lab_device_list[0][random_device][1][0],lab_device_list[0][random_device][1][1], env, 'User Activity',))
    t2.start()
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()

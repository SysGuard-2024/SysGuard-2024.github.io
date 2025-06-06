# SysGuard-2024.github.io

## Detecting and Handling WoT Violations by Learning Physical Interactions from Device Logs

We propose a novel WoT violation detecting and handling approach, named SysGuard. SysGuard models physical interactions between actuators and environment attributes as a Physical Interaction Graph (PIG) and learns these interactions from device logs. SysGuard monitors device logs during runtime and infers the PIG to predict violation states and generate handling policies that can transition the violation states to the target states.  
To evaluate SysGuard, we construct the first real-world WoT violation dataset by collecting device logs from two WoT systems, and annotate the collected logs with ten frequently reported violation types.

## [Dataset](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Dataset/)

We continuously collect four weeks of device logs starting from the initial states of two typical real-world WoT systems, including a smart home WoT system and a intelligent building WoT system.  
In the smart home WoT system, there are 45 actuators of 16 different types and 43 sensors of 9 different types deployed in 7 spaces. In the intelligent building WoT system, there are 36 actuators of 13 different types and 34 sensors of 8 different types deployed in 5 spaces. The deployed devices and spatial layout are illustrated as follows:

<p>
<div align=center>
<img width="98%" style="margin-right:2%" src="/images/layout.png"/>
</div>
</p>

For each WoT system, we also use the graph database neo4j to represent the spatial layout of deployed devices, the relationships between environmental spaces, and the attribute states of devices and spaces.  
The environment representation of the smart home WoT system: [LINK](http://47.101.169.122:7475/browser/) (bolt port: 7688, username: neo4j, password: 12345678)  
The environment representation of the intelligent building WoT system: [LINK](http://47.101.169.122:7474/browser/) (bolt port: 7687, username: neo4j, password: 12345678)

Each device corresponds to a device description model that documents its functionality, as well as a device proxy service that integrates the device into WoT system and generates device logs. Additionally, we also access the daytime, outdoor weather, air quality, temperature, humidity, and ultraviolet conditions through online weather forecasting services. For each WoT system, multiple trigger-action style automation applications are developed to meet the daily needs of users, listed as follows:

<div align=center> 
<img width="48%" style="margin-right:10pt;" src="/images/home_application.png"/>
<img width="48%" style="margin-right:10pt;" src="/images/building_application.png"/>
</div>

In the smart home WoT system, an average of 350 device logs are collected per day, with a total of 9981 valid device logs collected. In the intelligent building WoT system, an average of 1,250 device logs are collected per day, with a total of 34,916 device logs collected. For each device log, we anonymize the sensitive data such as user information, and record it in the following format:

- **logType：** Operations that change the working state of actuators are recorded as Action Log type, and changes in environmental attributes sensed by sensors are recorded as Event Log type.
- **logName：** It records the specific name of the current log.
- **deviceLocation：** It records the location of the device that generates the log.
- **Timestamp：** It records the timestamp when the device log is generated.
- **stateInfo：** For action logs, it records the current working state of actuators; For event logs, it records the current state of environmental attributes.
- **actionSource：** For action logs, we additionally record whether the current device operation originates from a software application call (marked as "network") or physical control (marked as "physical").

To make the dataset more realistic and targeted, we summarize 10 types of frequently reported real-world violations according to the previous user studies and our interviews with the stakeholders and individuals of each environment, as shown below. Each violation involves the effect of physical interactions that may occur in the smart home WoT system (marked as H) or the intelligent building WoT system (marked as B). For each type of violation, we manually review the collected device logs and label a total of 1,571 violations in the "**violationLabel**" field of the device logs.

<div align=center> 
<img width="98%" src="/images/violation.png"/>
</div>

## [Violation Description Tool](http://47.101.169.122:9038/)

To help non-technical users customize violation rules, SysGuard provides a GUI tool to simplify this process. The tool is designed similarly to the popular WoT application construction tools such as IFTTT, which automatically initializes using environment information, and allows users to easily configure violation and target states through mouse clicks. The GUI of the violation description tool is shown below.

<div align=center> 
<img width="98%" src="/images/GUI.png"/>
</div>

Additionally, we also provide the example violation rules constructed for the ten violations in the smart home WoT system and intelligent building WoT system.  
Example violation rules in smart home WoT system: [LINK](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Dataset/Smart%20Home/Violation%20Rules/)  
Example violation rules in intelligent building WoT system: [LINK](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Dataset/Intelligent%20Building/Violation%20Rules/)


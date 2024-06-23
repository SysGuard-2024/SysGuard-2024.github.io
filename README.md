## SysGuard-2024.github.io

## Application

The spatial layout and the deployed devices of the smart office and the smart home are illustrated as follows:

<div align=center>
<img width="50%" style="margin-right:2%" src="https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/images/SmartOfficeEnv.png"/>
<img width="47%" src="https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/images/SmartHomeEnv.png"/>
</div>
</p>

<!-- There are 21 students working and studying in the laboratory, and 5 types of WoT applications are deployed to provide convenience for daily office work. Details of the applications are described below:
<div align=center><img width="400" src="https://raw.githubusercontent.com/EnvGuard-2024/EnvGuard-2024.github.io/master/images/application.png"/></div> -->

We deployed 5 types of WoT applications in office and home for our daily office work and home life. The applications are as follows:

<div align=center> 
<img width="44.7%" style="margin-right:2%" src="https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/images/office_application.png"/>
<img width="48%" src="https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/images/home_application.png"/> 
</div>

Through interviews with staff in the environment, we obtained ten expected safety and security property requirements from interviews with individuals who work or live there daily for each environment. We invited six experts with WoT development experience to independently analyze and label the events and actions that violated the properties (Fleiss Kappa = 0.68) and resolve discrepancies through discussion to obtain the ground truth. The properties are as follows:

<div align=center>
<img width="46.3%" style="margin-right:2%" src="https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/images/office_propertys.png"/>
<img width="46.3%" src="https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/images/home_propertys.png"/>
</div>

## GUI

The visualized environment property description tool. ([GUI](http://47.101.169.122:9038/))

## Environment Information

<!-- We use the information in the [json file](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Simulation/PhysicalSpaceLayout) to construct neo4j for different smart WoT environments, and construct the [simulation environment](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Simulation/EnvironmentConstruct) by accessing neo4j. -->

The environment representation of the smart office WoT environment in [neo4j](http://47.101.169.122:7474/browser/) (bolt port: `7687`, username: `neo4j`, password: `12345678`)

The environment representation of the smart home WoT environment in [neo4j](http://47.101.169.122:7475/browser/) (bolt port: `7688`, username: `neo4j`, password: `12345678`)

## WoT System

Through the [device agent interface](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Code/WotSystem/DeviceProxyService/device_proxy_service.docx), we can efficiently schedule and manage devices. At the same time, the [ELK system](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Code/WotSystem/LogCollector/log_collector.py) is integrated to generate detailed log data. In addition, [the device description model](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Code/WotSystem/DeviceDescriptionModel/) provides detailed configuration and parameter information of the devices, which helps to parse the logs more accurately in the ELK system, thus enabling comprehensive monitoring and analysis of the device status.

## Data

All the experimental data of our work is available:
[Data](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Data)

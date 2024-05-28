## EnvGuard-2024.github.io

## Simulation

We use the information in the [json file](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Simulation/PhysicalSpaceLayout) to construct neo4j for different smart WoT environments, and construct the [simulation environment](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/Simulation/EnvironmentConstruct) by accessing neo4j.

The environment representation of the smart office WoT environment in [neo4j](http://47.101.169.122:7474/browser/) (bolt port: `7687`, username: `neo4j`, password: `12345678`)

The environment representation of the smart home WoT environment in [neo4j](http://47.101.169.122:7475/browser/) (bolt port: `7688`, username: `neo4j`, password: `12345678`)

## WoT System

Through the [device agent interface](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/WotSystem/DeviceProxyService/device_proxy_service.docx), we can efficiently schedule and manage devices. At the same time, the [ELK system](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/WotSystem/LogCollector/log_collector.docx) is integrated to generate detailed log data. In addition, [the device description model](https://github.com/SysGuard-2024/SysGuard-2024.github.io/blob/master/WotSystem/DeviceDescriptionModel/) provides detailed configuration and parameter information of the devices, which helps to parse the logs more accurately in the ELK system, thus enabling comprehensive monitoring and analysis of the device status.

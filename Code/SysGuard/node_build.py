import os
import json

device_nodes = {}

def extract_info(json_data):
    return {
        "id": json_data.get("id"),
        "type": "actuator" if "Actions" in json_data else "sensor",
        "Category": json_data.get("Category"),
        "location": json_data.get("location"),
        "state": json_data["Properties"]["power"]["enum"][0] if "Properties" in json_data and "power" in json_data["Properties"] else None
    }

for root, dirs, files in os.walk("/DeviceDescriptionModel"):
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                node_info = extract_info(data)
                device_nodes[node_info["id"]] = node_info

print(device_nodes)
import pandas as pd
import os

devices = ['Balcony_Temperature', 'Balcony_AirQuality', 'Bathroom_AirQuality', 'BedroomTwo_Temperature',
'Bathroom_Temperature', 'BedroomOne_Humidity', 'BedroomOne_Temperature', 'Bathroom_HumanState', 
'LivingRoom_AirQuality', 'BedroomTwo_Humidity', 'BedroomOne_Brightness', 'Kitchen_Temperature', 
'Bathroom_Humidity', 'Context_Humidity', 'Context_AirQuality', 'BedroomOne_AirQuality', 
'Cloakroom_HumanState', 'Cloakroom_Temperature', 'Kitchen_HumanState', 'Cloakroom_AirQuality', 
'Bathroom_Brightness', 'BedroomOne_HumanState', 'BedroomTwo_AirQuality', 'Balcony_HumanState', 
'LivingRoom_Humidity', 'LivingRoom_Temperature', 'Balcony_Humidity', 'Kitchen_AirQuality', 
'BedroomTwo_Brightness', 'Context_Temperature', 'Kitchen_Humidity', 'Cloakroom_Humidity', 
'Kitchen_Brightness', 'LivingRoom_Brightness', 'BedroomTwo_HumanState', 'LivingRoom_HumanState',
 'Balcony_Brightness', 'Context_Brightness', 'Cloakroom_Brightness','BedroomTwo_Heater', 
 'Balcony_Light', 'Kitchen_CookerHood', 'BedroomOne_AirPurifier', 'BedroomTwo_Door', 
 'Balcony_Curtain', 'LivingRoom_Heater', 'BedroomTwo_AirPurifier', 'LivingRoom_Door', 
 'Kitchen_Window', 'LivingRoom_Humidifier', 'BedroomTwo_Window', 'BedroomOne_Humidifier', 
 'LivingRoom_AirPurifier', 'BedroomOne_AC', 'Balcony_Door', 'Bathroom_Light', 
 'BedroomTwo_Light', 'LivingRoom_AC', 'BedroomOne_Light', 'BedroomTwo_AC', 
 'Kitchen_Curtain', 'Cloakroom_Door', 'BedroomOne_Curtain', 'Balcony_Window', 
 'BedroomTwo_Curtain', 'LivingRoom_Curtain', 'BedroomOne_Heater', 'BedroomOne_Window', 
 'Bathroom_Door', 'Kitchen_Light', 'Cloakroom_Light', 'LivingRoom_Window', 
 'Kitchen_Door', 'BedroomTwo_Humidifier', 'BedroomOne_Door', 'LivingRoom_Light']

special_mapping = {
    "0": 0,
    "1": 1,
    "-1": 2,
}


all_data = []
for i in range(1, 2):
    file_path = f'row_data/day_{i:02d}.xlsx'
    if os.path.exists(file_path):
        data = pd.read_excel(file_path)
        all_data.append(data)
    else:
        print(f"{file_path} not exist.")
time_series_data = pd.concat(all_data, ignore_index=True)
time_series_data.to_excel('merged_data/train_data.xlsx', index=False)

# all_data = []
# for i in range(11, 15):
#     file_path = f'row_data/day_{i:02d}.xlsx'
#     if os.path.exists(file_path):
#         data = pd.read_excel(file_path)
#         all_data.append(data)
#     else:
#         print(f"{file_path} 不存在")
# time_series_data = pd.concat(all_data, ignore_index=True)
# time_series_data.to_excel('merged_data/test_data.xlsx', index=False)


input_directory = 'merged_data'
output_directory = 'data'
excel_files = [f for f in os.listdir(input_directory) if f.endswith('.xlsx')]

os.makedirs(output_directory, exist_ok=True)

for file_name in excel_files:
    file_path = os.path.join(input_directory, file_name)
    raw_df = pd.read_excel(file_path)

    time_series_data = pd.DataFrame(columns=[device for device in devices])

    for timestamp in raw_df['Timestamp'].unique():
        row_data = {}
        for device in devices:
            device_name = device.replace('_', '.')
            state = raw_df[(raw_df['Timestamp'] == timestamp) & (raw_df['Payload Data'].str.contains(device_name))]
            if not state.empty:
                payload_data = state['Payload Data'].values[0]
                value = payload_data.split(device_name + '.state: ')[1]
                row_data[device] = value
            else:
                row_data[device] = None
        time_series_data = pd.concat([time_series_data, pd.DataFrame([row_data])], ignore_index=True)

    time_series_data.ffill(inplace=True)
    time_series_data.fillna(0, inplace=True)

    for column in time_series_data.columns:
        if time_series_data[column].dtype == 'object':
            time_series_data[column] = time_series_data[column].apply(lambda x: special_mapping.get(x, x))

    output_file_path = os.path.join(output_directory, file_name)
    time_series_data.to_excel(output_file_path, index=False)

    print(f"Successfully exported to {output_file_path}")



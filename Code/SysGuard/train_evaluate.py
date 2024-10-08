import time
import json
import networkx as nx
import bnlearn as bn
import pandas as pd
from pgmpy.estimators import HillClimbSearch, BicScore
from openai import OpenAI
import os

# JSON file path
room_state_path = 'config/room_state.json'

# Read the JSON file
with open(room_state_path, 'r') as file:
    room_state = json.load(file)

# Read log data from Excel file
file_path = '../data/sorted_combined_log.xlsx'
log_data = pd.read_excel(file_path)

# Read time series data from Excel file
file_path = '../data/processed.xlsx'
time_series_data = pd.read_excel(file_path)

# Get all device column names
devices = time_series_data.columns.tolist()

# Create a new DataFrame by shifting the original data by one row to create data pairs from consecutive time points
time_series_shifted = time_series_data.shift(-1).dropna().reset_index(drop=True)
time_series_combined = pd.concat([time_series_data.iloc[:-1].reset_index(drop=True), time_series_shifted], axis=1)
time_series_combined.columns = [f"{col}_0" if i < len(devices) else f"{col}_1" for i, col in enumerate(time_series_combined.columns)]

# Sample the data
sampled_data = time_series_combined.sample(n=500)

# Perform structure learning using constraint-based learning (CL) method
DAG = bn.structure_learning.fit(sampled_data, methodtype='cl') 
edges = list(DAG['model'].edges())

client = OpenAI()
for edge in edges:
    multi_line_string = f'''You are a WoT expert and skilled at analyzing causal relationships between 
    interactions of devices. Your task is to determine whether {edge[0]} influences {edge[1]} with yes or no 
    through PHYSICAL INTERACTION based on the given Scenario:'''
    print(multi_line_string)
    
    # Search for matching terms in log data
    search_terms = [edge[0].replace("_", ".") for edge in edges]
    Scenario = []
    for term in search_terms:
        match_indices = log_data[log_data["payloadData"].str.contains(term)].index[:5]
        for idx in match_indices:
            start = max(0, idx - 3)
            end = min(len(log_data), idx + 4)
            matches.extend(log_data["payloadData"].iloc[start:end].tolist())
    Scenario = matches[:35]

    # Append scenarios to the multi_line_string
    for scenario in Scenario:
        multi_line_string += f"- {scenario}\n"

    # Get response from OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": multi_line_string,
            },
        ],
    )

    # Remove edge if response indicates no influence
    if "no" in completion.choices[0].message.content:
        DAG = bn.del_edge(DAG, edge[0], edge[1]) 

# Record start time
start_time = time.time()

# Fit the model
DAG = bn.parameter_learning.fit(DAG, sampled_data)

# Record end time
end_time = time.time()

# Calculate and print the fitting time
fit_time = end_time - start_time
print(f"Model fitting time: {fit_time} seconds")

# Initialize counters
sum_all = 0
sum_true_all = 0

# Collect all relevant nodes (excluding those with "Context")
relevant_nodes = [node + '_1' for node in nodes_with_state if "Context" not in node]

nodes = list(DAG['model'].nodes())

sum_all = 0
sum_true_all = 0
for node in nodes:
    if "Context" in node:
        continue
    if node not in relevant_nodes:
        continue
    if node not in time_series_combined.columns:
        continue

    # Predict based on the DAG
    pred = bn.predict(DAG, df=time_series_combined[nodes].sample(n=500), variables=[node])
    pred_grass = pred[node]

    sum_true = 0
    sum = 0
    for index in pred.index:
        sum += 1
        sum_all += 1
        row_v = time_series_combined[node][index]
        pred_v = pred_grass[index]
        if row_v == pred_v:
            sum_true += 1
            sum_true_all += 1

    # Print accuracy for each node
    print("rate: " + str(sum_true / sum))

# Print overall accuracy
print("all_rate: " + str(sum_true_all / sum_all))

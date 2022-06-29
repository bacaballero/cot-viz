import json
import os
import pandas as pd
from futures_list import futures_list


def cot_all_to_json():
    dir_name = os.path.dirname(__file__)

    df = pd.read_csv(
        dir_name + '\COT Combined Report\COT-All.csv')

    futures = {'data': []}

    name_list = []
    for future in df['Market_and_Exchange_Names'].unique():
        name_list.append(future)

    for future_name in name_list:
        date_list = []
        comm_list = []
        noncomm_list = []
        nonrept_list = []
        is_df = df['Market_and_Exchange_Names'] == future_name
        is_df = df[is_df]
        for report_date in is_df['Report_Date_as_MM_DD_YYYY']:
            date_list.append(report_date)
        for comm_data in is_df['Comm_Net_All']:
            comm_list.append(comm_data)
        for noncomm_data in is_df['NonComm_Net_All']:
            noncomm_list.append(noncomm_data)
        for nonrept_data in is_df['NonRept_Net_All']:
            nonrept_list.append(nonrept_data)
        futures['data'].append({"name": future_name, "dates": date_list, "commercial": comm_list,
                               "non commercial": noncomm_list, "non reporting": nonrept_list})

    json_object = json.dumps(futures, indent=4)
    print(json_object)

    with open(dir_name + '\cot-viz\src\json_data.json', 'w') as outfile:
        json.dump(futures, outfile)

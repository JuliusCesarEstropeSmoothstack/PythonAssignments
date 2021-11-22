import logging
import re
import processAgentFile
import pandas as pd
from os import listdir
from os.path import isfile, join

file_directory_name = '.\\files'
name_prefix = 'NYL_FieldAgent_'

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='pandasProcessingLog.log')

file_list = []
try:
    logging.info(f'Getting files from {file_directory_name}')
    file_list = [file for file in listdir(file_directory_name) if isfile(join(file_directory_name, file))]
    file_list.sort(reverse=True)

    if len(file_list) <= 0:
        raise FileExistsError

    logging.info(f'Found these files: {file_list} in {file_directory_name}.')
except FileNotFoundError:
    message = f'Directory {file_directory_name} does not exist.'
    logging.fatal(message)
    print(message)
    exit(-1)
except FileExistsError:
    message = f'No files found in {file_directory_name}.'
    logging.fatal(message)
    print(message)
    exit(-1)

df = pd.read_csv(join(file_directory_name, file_list[0]))

if len(file_list) >= 2 and len(df) - 500 < len(pd.read_csv(join(file_directory_name, file_list[1]))):
    message = 'Most recent file is less than 500 lines different. Ending process'
    logging.warning(message)
    print(message)
    exit(0)

try:
    processed_file_log = open('NYL.lst', 'r')

    if re.search(file_list[0], str(processed_file_log.readlines())):
        message = f'{file_list[0]} has already been processed. Exiting.'
        logging.warning(message)
        print(message)
        exit(0)
except FileExistsError:
    message = f'NYL.lst does not exist. Creating it.'
    logging.warning(message)
    print(message)

processed_file_log = open('NYL.lst', 'w+')

processed_file_log.write(file_list[0])

processed_file_log.close()

processAgentFile.process_agent_dataframe(df)

# Data Frame after processing
logging.info(df)
print(df)

# Group all agents by Agency State
agency_df = df.groupby('Agency State')
logging.info(agency_df)
print(agency_df)

# Data Frame giving Agent Name, Agent Writing Contract Start Date, Date when agent became A20
selected_data_frame = df[['Agent First Name', 'Agent Writing Contract Start Date', 'Date when an agent became A2O']]
logging.info(selected_data_frame)
print(selected_data_frame)

df.plot.hist()
agency_df.plot.hist()

import h5py
import numpy as np
import pandas as pd
import requests
import re
import datetime as dt
import os
import logging
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(filename='temp_data.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

filename = 'temp_data.h5'

# If file exists, open it in append mode, otherwise create it
if os.path.isfile(filename):
    f = h5py.File(filename, 'a')
else:
    f = h5py.File(filename, 'w')

# Read URLs from the CSV file using pandas
df = pd.read_csv('urls.csv')
urls = df['URL']

# Loop over the websites and scrape the temperature and timestamp data
for i, url in enumerate(urls):
    # Send a request to the website and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Get the current temperature
    if i == 0:  # For the first website
        temp = soup.find(class_='vorhersage_schrift2', id='temp_1').text.split('\n')[2]
        temp = re.split('[:°]', temp)
        temp = temp[1]
    elif i == 1:  # For the second website
        temp = soup.find('span', {'data-unit': 'c'}).text
        temp = re.split('°', temp)
        temp = temp[0]
    else:  # For the third website
        temp = soup.find('span', class_='c-current-weather__temperature unit_C ltr').text.strip().split('\n')
        temp = temp[0]

    # Convert temperature to float
    temp = np.array([temp]).astype(float)

    # Get the current date and time
    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the temperature and timestamp data to the HDF5 file
    with h5py.File(filename, "a") as f:
        # Check if group already exists
        group_name = url.split("//")[-1].split("/")[0]
        if group_name in f:
            group = f[group_name]
        else:
            group = f.create_group(group_name)

        # Check if dataset already exists
        if "temperature" in group:
            dset_temp = group["temperature"]
            dset_temp.resize(dset_temp.shape[0] + 1, axis=0)
            dset_temp[-1] = temp
        else:
            dset_temp = group.create_dataset("temperature", shape=(1,), maxshape=(None,), chunks=True, dtype=float)
            dset_temp[0] = temp

        if "timestamp" in group:
            dset_timestamp = group["timestamp"]
            dset_timestamp.resize(dset_timestamp.shape[0] + 1, axis=0)
            dset_timestamp[-1] = np.string_(timestamp)
        else:
            dset_timestamp = group.create_dataset("timestamp", shape=(1,), maxshape=(None,), dtype=h5py.special_dtype(vlen=str))
            dset_timestamp[0] = np.string_(timestamp)

    # Log the data saved to the file
    logging.info(f"{timestamp} - {url} - Temperature: {temp[0]}")
    
# Log the end of the script
logging.info("Temperature data saved to HDF5 file.")
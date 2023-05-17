import numpy as np
import pandas as pd
import plotly.express as px
import h5py

# read data out of h5py file and create visualization
with h5py.File('temp_data.h5', 'r') as hdf:
    # retrieve datasets
    wetterdienst_timestamp = np.array(hdf.get("www.wetterdienst.de/timestamp")).astype('datetime64', copy=False)
    wetterdienst_temperature = np.array(hdf.get("www.wetterdienst.de/temperature"))
    euro_timestamp = np.array(hdf.get("de.euronews.com/timestamp")).astype('datetime64', copy=False)
    euro_temperature = np.array(hdf.get("de.euronews.com/temperature"))
    topweather_timestamp = np.array(hdf.get("www.topweather.net/timestamp")).astype('datetime64', copy=False)
    topweather_temperature = np.array(hdf.get("www.topweather.net/temperature"))
    
    # create dataframes
    wetterdienst_df = pd.DataFrame({'timestamp': wetterdienst_timestamp, 'temperature': wetterdienst_temperature, 'Location': 'Garbsen, Hannover'})
    euro_df = pd.DataFrame({'timestamp': euro_timestamp, 'temperature': euro_temperature, 'Location': 'Langenhagen, Hannover'})
    topweather_df = pd.DataFrame({'timestamp': topweather_timestamp, 'temperature': topweather_temperature, 'Location': 'Anderten, Hannover'})

    # concatenate dataframes
    df = pd.concat([wetterdienst_df, euro_df, topweather_df], axis=0)

    # create plot with title and subtitle
    fig = px.line(df, x='timestamp', y='temperature', color='Location', 
                  labels={'timestamp': 'Timestamp', 'temperature': 'Temperature in C°'},
                  template='plotly_white')
    fig.update_layout(
        title={
            'text': "Temperature Development in Hannover<br><sup>Data from Garbsen, Langenhagen, and Anderten</sup>",
            'font': {'size': 20},
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    fig.show()

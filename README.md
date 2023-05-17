## Web Scraping and Temperature Data Visualization
This project is designed to scrape temperature data from multiple websites and visualize the temperature trends over time. It utilizes web scraping techniques to extract temperature information from different sources and then presents the data using interactive visualizations.

## Project Overview
The main components of this project are as follows:

### Web Scraping: 
The project includes a script that reads a list of URLs from a CSV file and performs web scraping to extract temperature data. The script sends HTTP requests to each website, retrieves the HTML content, and uses BeautifulSoup to parse and extract the temperature values.

### Data Storage: 
The scraped temperature data is stored in an HDF5 file format. The script creates or appends to an HDF5 file, organizes the data by website source, and saves the temperature values along with the corresponding timestamps.

### Data Visualization: 
The project utilizes the Plotly library to create interactive line charts for visualizing the temperature trends. The temperature data from different sources is combined into a single dataframe, and Plotly Express is used to generate line charts with timestamps on the x-axis and temperature values on the y-axis. The charts are customizable, allowing users to explore the temperature development over time.

### Automation: 
The project includes instructions for setting up a cron job on a Windows machine to run the web scraping script periodically. The cron job is scheduled to execute once every hour, collecting temperature data for the next two days. This ensures that the temperature data remains up to date and provides a continuous monitoring of temperature trends.

## Getting Started
To get started with this project, follow the steps below:

1. Install the required dependencies by running pip install -r requirements.txt.

2. Set up the URLs: Create a CSV file named urls.csv and populate it with the URLs of the websites from which you want to scrape temperature data.

3. Run the web scraping script: Execute the scrap.py script to initiate the web scraping process. This script will send requests to the specified URLs, extract temperature data, and store it in the temp_data.h5 HDF5 file.

4. Visualize the temperature data: Run the visualize.py script to generate interactive line charts using the stored temperature data. The charts will be displayed in your default web browser, allowing you to explore temperature trends over time.

5. Set up the cron job (optional): Follow the instructions provided in the documentation to set up a cron job on your Windows machine. This will automate the data collection process by running the web scraping script periodically.

## Contributing
Contributions to this project are welcome. If you encounter any issues, have suggestions for improvements, or would like to add new features, please open an issue or submit a pull request. Your contributions will help enhance the functionality and usability of this project.

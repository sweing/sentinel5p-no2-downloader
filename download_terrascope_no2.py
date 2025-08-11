import requests
import os
import configparser
from datetime import datetime

def download_terrascope_no2_data(year, output_dir="Terrascope_NO2_Local_Exports"):
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        username = config['terrascope']['username']
        password = config['terrascope']['password']
    except KeyError:
        print("Error: Terrascope credentials not found in config.ini. Please ensure 'username' and 'password' are set under the '[terrascope]' section.")
        return

    base_url = "https://services.terrascope.be/download/Sentinel5P/L3_NO2_TM_V2/"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for month in range(1, 13):
        month_str = f"{month:02d}"
        
        # Construct the URL based on the pattern provided
        # Example: https://services.terrascope.be/download/Sentinel5P/L3_NO2_TM_V2/2025/S5P_OFFL_L3_NO2_TM_20250601_V200/S5P_NO2_TM_202506_NO2_V200.tif
        
        # The day in the folder name seems to always be '01' for monthly files
        folder_date = f"{year}{month_str}01"
        file_date = f"{year}{month_str}"

        url = f"{base_url}{year}/S5P_OFFL_L3_NO2_TM_{folder_date}_V200/S5P_NO2_TM_{file_date}_NO2_V200.tif"
        
        file_name = f"S5P_NO2_TM_{file_date}_NO2_V200.tif"
        local_file_path = os.path.join(output_dir, file_name)

        print(f"Attempting to download {url}")
        try:
            with requests.get(url, auth=(username, password), stream=True) as r:
                r.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
                with open(local_file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        f.write(chunk)
            print(f"Successfully downloaded {file_name}")
        except requests.exceptions.HTTPError as e:
            print(f"Error downloading {file_name}: HTTP Error {e.response.status_code} - {e.response.reason}")
        except requests.exceptions.ConnectionError as e:
            print(f"Error downloading {file_name}: Connection Error - {e}")
        except requests.exceptions.Timeout as e:
            print(f"Error downloading {file_name}: Timeout Error - {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {file_name}: An unexpected error occurred - {e}")

if __name__ == "__main__":
    download_year = 2024
    download_terrascope_no2_data(download_year)
    print(f"Download process for year {download_year} completed. Check the 'Terrascope_NO2_Local_Exports' directory.")

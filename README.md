# Global NO2 Data Downloader

This project contains a Python script to download monthly average Nitrogen Dioxide (NO2) composites from the Copernicus Sentinel-5P satellite using the Terrascope service. The script saves the data as GeoTIFF files directly to your local machine.

## Features

- Downloads monthly mean NO2 data for a specified year from Terrascope.
- Saves data directly to a local directory.
- Authenticates using credentials stored in a `config.ini` file.

## Requirements

- Python 3.6+
- A Terrascope account with a username and password.

## Installation and Setup

This project uses [Pixi](https://pixi.sh/) for environment and dependency management.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install Pixi:**
    Follow the official instructions at [pixi.sh](https://pixi.sh/latest/) to install Pixi on your system.

3.  **Install Dependencies:**
    Once Pixi is installed, run the following command to create the environment and install all necessary dependencies.
    ```bash
    pixi install
    ```

4.  **Configure Terrascope Credentials:**
    Create a file named `config.ini` in the root of the project and add your Terrascope credentials:
    ```ini
    [terrascope]
    username = YOUR_USERNAME
    password = YOUR_PASSWORD
    ```
    Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your actual Terrascope login details. This file is included in `.gitignore` and will not be committed to source control.

To download the data, run the script using Pixi:
```bash
pixi run start
```

The script will:
1.  Create a local directory (default: `Terrascope_NO2_Local_Exports`).
2.  Begin downloading the 12 monthly GeoTIFF files for the current year.

This process can take some time, depending on your internet connection.

## Configuration

You can modify the following parameter at the bottom of the `download_terrascope_no2.py` script:

- `download_year`: The year for which you want to download data (e.g., `2024`).
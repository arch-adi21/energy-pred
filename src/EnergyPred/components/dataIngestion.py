import os
import requests
import zipfile
import os

def download_and_extract_repository(url, folder_name):
    """Downloads a GitHub repository from the given URL in zip format,
    extracts it, and saves it in the specified folder. Creates the folder
    if it doesn't exist.

    Args:
        url (str): The URL of the GitHub repository (e.g., "https://github.com/arch-adi21/EnergyPredData").
        folder_name (str): The name of the folder to save the extracted files in.
    """

    filename = url.split("/")[-1] + ".zip"  # Extract filename from URL

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Downloaded {filename}")

        # Create the folder if it doesn't exist
        os.makedirs(folder_name, exist_ok=True)  # Handle existing folder

        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(folder_name)

        print(f"Extracted repository contents to '{folder_name}'")

        # Remove the downloaded zip file (optional)
        # os.remove(filename)  # Uncomment if you want to delete the zip

    except requests.exceptions.RequestException as e:
        print(f"Error downloading repository: {e}")
    except zipfile.ZipException as e:
        print(f"Error extracting repository: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/arch-adi21/EnergyPredData"
    folder_name = "/artifacts/data"  # Customize the folder name as desired
    download_and_extract_repository(repo_url, folder_name)


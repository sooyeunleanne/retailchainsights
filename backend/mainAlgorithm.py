import requests
import pandas as pd
import zipfile
import io
import os
from urllib.parse import urlparse, parse_qs

def get_data(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    pid_full = query_params.get('pid', [None])[0]

    if pid_full is None:
        raise ValueError("Invalid URL: PID not found.")
    
    pid = pid_full[:8]  # Trim to 8-digit productId
    api_url = f'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{pid}/en'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(api_url, headers=headers)

    if not response.ok:
        raise Exception(f"Failed to fetch download link. Status: {response.status_code}\n{response.text}")

    # Get the ZIP file URL
    zip_url = response.json()['object']
    print(f"📥 ZIP Download URL: {zip_url}")

    # Download and unzip the file in memory
    zip_response = requests.get(zip_url)
    with zipfile.ZipFile(io.BytesIO(zip_response.content)) as z:
        # Assume first file in zip is the CSV
        csv_filename = z.namelist()[0]
        print(f"📄 Extracting file: {csv_filename}")
        with z.open(csv_filename) as f:
            df = pd.read_csv(f)

    print(df.head)
            
    return df

def save_csv_file(df, filename, directory='fetchedData'):
    os.makedirs(directory, exist_ok=True)  # Create directory if it doesn't exist
    filepath = os.path.join(directory, filename)
    df.to_csv(filepath, index=False)
    print(f"✅ Saved CSV to: {filepath}")


# Example usage
if __name__ == "__main__":
    url = input("Enter a StatCan table URL (e.g. https://...pid=1810024501): ")
    try:
        df = get_data(url)
        print("\n✅ Successfully loaded full dataset!")
        print(df.head())
        print(f"\n🔢 Total rows: {len(df)}")
    except Exception as e:
        print("❌ Error:", e)

# import requests
# import pandas as pd
# from urllib.parse import urlparse, parse_qs

# def get_data(url):
#   parsed_url = urlparse(url)
#   query_params = parse_qs(parsed_url.query)
#   pid = query_params.get('pid', [None])[0]  # pid = table id

#   if pid is None :
#     raise ValueError("Invalid URL: PID not found.")
  
#   # building API url using the given pid
#   api_url = f'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{lang}/{pid}/'
#   print(f"🔗 API URL: {api_url}")  # <== DEBUG PRINT

#   headers = {'User-Agent': 'Mozilla/5.0'}
#   response = requests.get(api_url, headers=headers)
#   print(f"📡 Status Code: {response.status_code}")  # <== DEBUG PRINT
  

#   if not response.ok:
#     print(f"❌ Response Text: {response.text}")  # <== DEBUG PRINT
#     raise Exception("Failed to retrieve data.")
  
#   # grab csv download link from the response
#   download_info = response.json()
#   print(f"🔽 CSV URL: {download_info['object']['downloadUrl']['english']}")  # <== DEBUG PRINT

#   csv_url = download_info['object']['downloadUrl']['english']

#   # load data into pd dataframe
#   df = pd.read_csv(csv_url)
  
#   return df

  
# # eg.
# if __name__ == "__main__":
#   url = input("Enter StatCan table URL: ")
#   try:
#     df = get_data(url)
#     print("\nSuccessfully loaded full dataset!")
#     print(df.head())
#     print(f"\nTotal rows: {len(df)}")
#   except Exception as e:
#     print("Error: ", e)

import requests
import pandas as pd
import zipfile
import io
from urllib.parse import urlparse, parse_qs

def get_data(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    pid_full = query_params.get('pid', [None])[0]

    if pid_full is None:
        raise ValueError("Invalid URL: PID not found.")
    
    pid = pid_full[:8]  # Trim to 8-digit productId
    api_url = f'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{pid}/en'
    print(f"🔗 API URL: {api_url}")

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

    return df

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

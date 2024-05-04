import requests
import json
from datetime import datetime

# Constants (Sensitive information like API tokens and IDs should be stored securely and imported from a safe location)
API_TOKEN = 'your_api_token_here'
FILE_ID = 'your_file_id_here'
NODE_ID = 'your_node_id_here'

# Figma API endpoint URL
URL = f"https://api.figma.com/v1/files/{FILE_ID}/nodes?ids={NODE_ID}"

# HTTP headers for authorization
headers = {"X-Figma-Token": API_TOKEN}

# Fetch data from Figma API
response = requests.get(URL, headers=headers)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
else:
    print(f"Error: {response.status_code} - {response.text}")
    exit()

# Function to extract node IDs and names from Figma document
def extract_id_and_name(document):
    extracted_data = []
    if "children" in document:
        for child in document["children"]:
            if child["name"].startswith("FR_"):  # Filter nodes with names starting with "FR_"
                extracted_data.append({"id": child["id"], "name": child["name"]})
    return extracted_data

# Extract node IDs and names from Figma document
root_document = data["nodes"][NODE_ID.replace("%3A", ":")]["document"]
extracted_data = extract_id_and_name(root_document)

# List to store image URLs
image_urls = []

# Iterate over extracted node IDs and names
for item in extracted_data:
    node_id = item['id']
    params = {'ids': node_id, 'format': 'png'}
    image_response = requests.get(f"https://api.figma.com/v1/images/{FILE_ID}", headers=headers, params=params)

    # Check if image URL was successfully fetched
    if image_response.status_code == 200:
        image_data = image_response.json()
        if node_id in image_data['images']:
            image_url = image_data['images'][node_id]
            # Append image URL to the list along with metadata
            image_urls.append({
                "name": item['name'],
                "id": node_id,
                "url": image_url,
                "dateTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print(f"Image URL fetched for node {node_id}: {image_url}")
    # Handle rate limit exceeded error
    elif image_response.status_code == 429:
        print("Rate limit exceeded. Waiting for 30 seconds...")
        time.sleep(30)  # Wait for 30 seconds before retrying
        image_response = requests.get(f"https://api.figma.com/v1/images/{FILE_ID}", headers=headers, params=params)
        if image_response.status_code == 200:
            image_data = image_response.json()
            if node_id in image_data['images']:
                image_url = image_data['images'][node_id]
                image_urls.append({
                    "name": item['name'],
                    "id": node_id,
                    "url": image_url,
                    "dateTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                print(f"Image URL fetched for node {node_id}: {image_url}")
    else:
        print(f"Error fetching image URL for node {node_id}: {image_response.status_code} - {image_response.text}")

# Save the list of image URLs to a JSON file
json_file_name = 'image_urls.json'
with open(json_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(image_urls, json_file, ensure_ascii=False, indent=4)

print(f"Image URLs saved to {json_file_name}")

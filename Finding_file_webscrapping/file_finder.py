import requests
from bs4 import BeautifulSoup
import os

# Replace with your webpage URL
webpage_url = "https://archive.stsci.edu/hlsps/reference-atlases/cdbs/grid/pickles/"

# Replace with the specific file name you're looking for
# target_file = "target_file.txt"
target_file = "pickles_10.fits"

def check_for_file(folder_url):
    folder_response = requests.get(folder_url)
    folder_content = folder_response.text
    # Use string manipulation to check if the target file exists in folder_content
    if target_file in folder_content:
        return True
    return False

# Fetch the webpage content
response = requests.get(webpage_url)
print("Webpage Caught")

webpage_content = response.text
# print(webpage_content)
# input()

# Parse the webpage content
soup = BeautifulSoup(webpage_content, "html.parser")
# print(soup)
# input()

# Find folder links
folder_links = [a['href'] for a in soup.find_all('a') if not a['href'].endswith('.')] # Remove the .. link, else it will go on loops 😵
# print(folder_links)
# input()

for folder_link in folder_links:
    folder_url = os.path.join(webpage_url, folder_link)
    if check_for_file(folder_url):
        print(f"File '{target_file}' found in folder '{folder_link}'.")
        ##
        ## DO SOME OPERATIONS HERE
        ##
    else:
        print(f"File '{target_file}' not found in folder '{folder_link}'.")

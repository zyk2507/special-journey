import requests
from bs4 import BeautifulSoup
import re

# URL of the HTML file containing the download links
url = "https://darkbzoj.cc/data/"

# Send a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the <a> tags that contain a download link
download_links = soup.find_all("a", href=True)

# Extract the download links from the <a> tags
links = []
for link in download_links:
    href = link.get("href")
    if re.match(r"^https?://", href):
        # Link is already an absolute URL
        links.append(href)
    else:
        # Link is a relative URL, so prepend the base URL
        links.append(url + href)

# Write the download links to a new file
with open("download_links.txt", "w") as f:
    for link in links:
        f.write(link + "\n")

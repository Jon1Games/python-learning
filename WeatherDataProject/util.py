from bs4 import BeautifulSoup
import requests

def get_all_links(url, endsWith):
    """Get all links from <a href="URL">
    Args:
        url (str): URL to the website to scrape.
        endsWith (str): The ending of the link to filter by.
    Returns:
        list: A list of all hyperlinks that end with the specified string.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    files = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith(endsWith):
            files.append(url + href)
    return files
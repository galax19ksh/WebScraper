# This code will handle failures of unicode text extraction. It takes the filename of the txt file that contains a list of failed links and then run the 
# same unicode text extraction. Like the main program, it gives the list of failed links so that we can run it recursively until all links are used.

from collections import deque  # Import deque for queue functionality
from bs4 import BeautifulSoup
import requests


def fetch_webpage(url):
  """
  Fetches the webpage using requests and returns the HTML content.
  """
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  else:
    print(f"Error fetching URL: {url}. Status code: {response.status_code}")
    return None


def extract_links_from_file(filename):
  """
  Extracts links from a text file.

  Args:
      filename (str): Path to the text file containing links.

  Returns:
      deque: Queue containing extracted links.
  """
  links = deque()
  try:
    with open(filename, 'r') as f:
      for line in f:
        link = line.strip()  # Remove leading/trailing whitespace
        if link:  # Check if line is not empty
          links.append(link)
  except FileNotFoundError:
    print(f"Error: File not found: {filename}")
  return links


def extract_and_save_unicode_text(links):
  """
  Extracts and saves Unicode text from URLs using BeautifulSoup.

  Args:
      links (deque): Queue containing URLs to process.
  """
  failed_links = deque()  # Queue to store links with failed Unicode generation

  for url in links:
    try:
      html = fetch_webpage(url)
      if html:
        soup = BeautifulSoup(html, 'html.parser')

        # Extract group and chapter number from the URL
        url_parts = url.split("/")[-2:]  # Get the last two parts (group and chapter)
        group, chapter = url_parts[0], url_parts[1]

        # Customize this part to extract your desired Unicode text
        # Here, we'll extract all text elements with characters beyond ASCII range
        unicode_text = ''.join([element.text for element in soup.find_all(string=True) if any(ord(char) > 127 for char in element.string)])

        if unicode_text:
          # Filename generation based on group and chapter
          filename = f"{group}{chapter}.txt"

          with open(filename, 'w', encoding='utf-8') as f:
            f.write(unicode_text)
          print(f"Unicode text saved to: {filename}")
        else:
          # Add URL to failed links queue
          failed_links.append(url)
          print(f"Failed to generate Unicode text for: {url}")
    except Exception as e:
      print(f"Error processing URL: {url}. Exception: {e}")

  # Print a message if there are failed links
  if failed_links:
    print("\nThe following links failed to generate Unicode text:")
    for link in failed_links:
      print(link)


if __name__ == "__main__":
  # Replace "failed_links.txt" with your actual filename
  link_file = input("Enter file name (failed links): ")
  links = extract_links_from_file(link_file)
  if links:
    extract_and_save_unicode_text(links)
  else:
    print(f"No links found in the file: {link_file}")

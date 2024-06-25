# this is for single webpage 
import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return None

def extract_english_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from HTML elements containing Unicode characters
    english_text = ''.join([element.text for element in soup.find_all(string=True)])
    return english_text

def write_to_file(text, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Unicode text saved to '{filename}'")
    except IOError as e:
        print("Error writing to file:", e)

def main():
    url = input("Enter the URL of the webpage: ")
    html = fetch_webpage(url)
    if html:
        english_text = extract_english_text(html)
        if english_text:
            filename = input("Enter the name of the output text file: ")
            write_to_file(english_text, filename)
        else:
            print("No Unicode text found on the webpage.")
    else:
        print("Failed to fetch the webpage.")

if __name__ == "__main__":
    main()

## Webpage Unicode Text Extractor VERSION 1

This Python script allows you to extract unicode text from a webpage and save it to a text file.

### Tools used

- `requests`: Used to fetch the webpage.
- `BeautifulSoup`: Used for parsing HTML content.

### How it Works
**Fetching the Webpage:** The script uses the requests library to fetch the HTML content of the webpage specified by the user.

**Extracting Unicode Text:** It then uses BeautifulSoup to parse the HTML content and extract text from HTML elements containing Unicode characters. This is achieved by iterating through all text elements and checking if any character has an ASCII value greater than 127.

**Writing to File:** The extracted Unicode text is then written to a text file specified by the user.


### Example Usage
1. Clone the repository to your local machine:
```bash
git clone https://github.com/galax19ksh/WebScraper.git
```

2. Run the script:

```bash
python3 main.py
```

3. Enter the URL of the webpage when prompted.
```bash
Enter the URL of the webpage: [Enter URL here] 
```
If Unicode text is found on the webpage, provide a name for the output text file when prompted.
```bash
Enter the name of the output text file: [Enter filename here]
```




**Note:**
Although the original intent of this project was to web scrape unicode texts of regional languages, this code script works on all websites. It will output a text file of the website. 

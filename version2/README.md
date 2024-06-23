## Webpage Unicode Text Extractor VERSION 2

This Python script allows you to extract text from webpages of a website having similar url and then save into text files.

### Tools used

- `requests`: Used to fetch the webpage.
- `BeautifulSoup`: Used for parsing HTML content.
- `urllib.parse`: Used for URL manipulation.

### How it Works
**Fetching the Webpage:** The script uses the requests library to fetch the HTML content of the webpage specified by the user.

**Extracting Unicode Text:** It then uses BeautifulSoup to parse the HTML content and extract text from HTML elements containing Unicode characters. This is achieved by iterating through all text elements and checking if any character has an ASCII value greater than 127.

**Writing to File:** The extracted Unicode text is then written to a text file specified by the user.


### Example Usage
1. Clone the repository to your local machine:
```bash
git clone https://github.com/galax19ksh/WebScraper/version2.git
```

2. Run the script:

```bash
python ws2.py
```

3. Enter the URL of the webpage when prompted.
```bash
Enter the URL of the webpage: [Enter URL here] 
```
Then provide the starting and finishing numbers of links to be scrapped from (within same website)
```bash
Enter the starting chapter number (inclusive): [Enter start no here]
```
```bash
Enter the ending chapter number (inclusive): [Enter end no here]
```



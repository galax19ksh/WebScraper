## Web Scraper - unicode text
This repository contains mutiple versions of source codes for extracting unicode text from webpages. This project is originally intended for creating corpus data that could be used in Machine Translation and other NLP tasks. The original motive for this came from finding [this bible website](https://live.bible.is/bible/MNIBIV/GEN/1) which has potentially a fairly huge text data of english along with parallel translation to almost all other languages. So I wanted to write some python script using useful libraries like beautifulsoup, selenium etc that can automatically scrap Manipuri text as they are necessary especially for low resource language processing. This work was done during my internship at IITG.
![image](https://github.com/user-attachments/assets/ad75f235-88f5-4125-a7e7-e8d9e959f2ea)
![image](https://github.com/user-attachments/assets/16978d97-99f8-42ff-b15e-ee9f3aa4d1f0)

#### Major Tools Used: 
`beautifulsoup` `selenium`

### Source Code

[Version 1](https://github.com/galax19ksh/WebScraper/tree/main/version1): Extracts Unicode text (manipuri) from a single webpage and saves it to a file.

[Version 2](https://github.com/galax19ksh/WebScraper/tree/main/version2): Extracts text from a range of URLs with similar structure within a website and saves them to separate files.There is also version 2.5 that takes file no as inputs.

[Version 3](https://github.com/galax19ksh/WebScraper/tree/main/version3): Dynamically extracts unicode from all the links in the desired section of a website and then saves them into separate files. It can also handle failures by running another code.

[Version 4](https://github.com/galax19ksh/WebScraper/tree/main/version4): Same as version 3 code except it is for scraping parallel english data. 

[Unicode Converter](https://github.com/galax19ksh/WebScraper/tree/main/unicode_mapping): Converts pdf files with non-standard unicode mapping used by local newspapers for Manipuri language (Bengali script) into proper unicode. 

**Note:** 
* You might need to make small changes or tweaks to the source code to make it work for other websites.

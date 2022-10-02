# Text Summarization Using Python

## Scraping data without using beatifulsoup

```python
# Importing the libraries
import wikipedia as w
import pandas as pd

# Summarizing the wikipedia article
text=w.summary("Flash (DC Comics character)")

# Searching and reading the wikipedia article
R = w.search("Flash (DC Comics character)")
page = w.page(R[0])
title = page.title
content = page.content
print("Page title : ", title, "\n")
print("Page content : ", content, "\n")
```

## Sentiment analysis using NLP

```python
# Importing the libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Removing stop words
stopWords = set(stopwords.words("english"))
words = word_tokenize(content)

# Creating a frequency table
freq_table = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freq_table:
        freq_table[word] += 1
    else:
        freq_table[word] = 1

# Analyzing the sentiment
sents = sent_tokenize(text)
sent_val = dict()
for sent in sents:
    for word, freq in freq_table.items():
        if word in sent.lower():
            if sent in sent_val:
                sent_val[sent] += freq
            else:
                sent_val[sent] = freq


# Counting the frequent words
sumvalues = 0
for sent in sent_val:
    sumvalues += sent_val[sent]
 
# Calculting average of frequent words
avg = int(sumvalues / len(sent_val))

# Summarizing text based on sentiment
summary = ''
for sent in sents:
    if (sent in sent_val) and (sent_val[sent] > (1 * avg)):
        summary += sent
print(summary)
```

## Scraping data using beautifulsoup
```python  
# Importing the libraries
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen 

# Requesting the web page
html=urlopen('https://en.wikipedia.org/wiki/Flash_(DC_Comics_character)')

# Reading HTML tags
bs=BeautifulSoup(html.read(),'html.parser')
HD=bs.findAll(['h1','h2','h3','h4','h5','h6'])

# Selecting all the paragraphs
bs.select('p')

# Separating the paragraphs
for i in bs.select('p'):
    content=i.text
    print(content)
    
# Removing the stop words
stopWords = set(stopwords.words("english"))
words = word_tokenize(content)

# Creating a frequency table
freq_table = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freq_table:
        freq_table[word] += 1
    else:
        freq_table[word] = 1
        
# Counting the frequency of words
sentences = sent_tokenize(text)
sent_value = dict()
for sentence in sentences:
    for word, freq in freq_table.items():
        if word in sentence.lower():
            if sentence in sent_value:
                sent_value[sentence] += freq
            else:
                sent_value[sentence] = freq
                
# Analyzing the sentiment of sentences
sum_val = 0
for sentence in sent_value:
    sum_val += sent_value[sentence]

# Calculating average of the count
avg = int(sum_val / len(sent_value))

# Printing the summary of the text
summary = ''
for sentence in sentences:
    if (sentence in sent_value) and (sent_value[sentence] > (0.6 * avg)):
        summary += sentence
print(summary)

```

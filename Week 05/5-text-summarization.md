# Text Summarization Using Python

## Scraping data without using beatifulsoup

```python
import wikipedia as w
import pandas as pd

text=w.summary("Flash (DC Comics character)")

R = w.search("Flash (DC Comics character)")
page = w.page(R[0])
title = page.title
content = page.content
print("Page title : ", title, "\n")
print("Page content : ", content, "\n")
```

## Sentiment analysis using NLP

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stopWords = set(stopwords.words("english"))
words = word_tokenize(content)

freq_table = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freq_table:
        freq_table[word] += 1
    else:
        freq_table[word] = 1
        
```

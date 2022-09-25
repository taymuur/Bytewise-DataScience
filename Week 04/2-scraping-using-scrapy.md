# Getting Started with Scrapy

The following code can be used to scrape quotes from the website [Quotes to Scrape](www.quotes.toscrape.com)

```python
import scrapy
class Quote_spider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {"Titletext" : title }
        
```

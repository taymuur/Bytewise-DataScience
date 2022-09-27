# Scraping Multiple Web Pages Using Scrapy

## Pagination

The process of pagination, commonly referred to as paging, involves separating a document into distinct pages, putting a collection of material on each page. Each of these unique pages has a unique url. Therefore, we must scrape these sites one by one using each of these urls. 

However, we should be aware of when to halt pagination. In most cases, pages have a next button. When a page is done, this button is disabled. When the next page button is active, this technique is utilised to obtain the URL of each page, and when it is disabled, no pages are left for scraping.

## Quotes to Scrape

```python
import scrapy
from ..items import QuotetItem

class Quotes_to_scrape(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
            items = QuotetItem()
            all_div_quotes = response.css('div.quote')
            for quotes in all_div_quotes:
                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tag = quotes.css(".tag::text").extract()

                items['title'] = title
                items['author'] = author
                items['tag'] = tag

                yield items

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)

```

## Amazon

```python
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A3248684011&dc&ds=v1%3AI91B%2BdZTSA96JFKRasp6HXQXmnwcDXjnGP3sdGiHpdM&qid=1663938140&ref=sr_ex_n_1']

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.a-size-base-plus::text').extract()
        product_price = response.css('.a-size-base-plus').css('::text').extract()
        product_image = response.css('.s-height-equalized .s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield  items
        next_page = 'https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A3248684011&dc&page='+ str(AmazonSpiderSpider.page_number) + '&qid=1663950585&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 100:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)
```

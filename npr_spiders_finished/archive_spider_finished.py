import scrapy

class ArchiveSpider(scrapy.Spider):
    name = "archive"
    start_urls = [
        f'https://www.npr.org/sections/news/archive?start={15*page+1}' for page in range(5)
    ]

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'title': article.css('h2.title a::text').get(),
                'url': article.css('h2.title a::attr(href)').get(),
                'date': article.css('p.teaser time::attr(datetime)').get(),
                'teaser': article.css('p.teaser a::text').get()
            }

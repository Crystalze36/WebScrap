import scrapy

class SongSpider(scrapy.Spider):
    name = "song"
    start_urls = [
        'https://www.npr.org/sections/allsongs/606254804/new-music-friday'
    ]

    def parse(self, response):
        yield self.parse_article(response)
        for tag in response.css('h2.title a'):
            yield response.follow(tag, self.parse_article)

    def parse_article(self, response):
        albums = response.css('li::text').re('(.+?)\s+—\s+<em>(.+?)</em>\s+<br>Featured Song: "(.+?)"')
        artists = response.css('div.storytext li::text').re('(.+) —')
        albums = response.css('div.storytext li em::text').getall()
        songs = response.css('div.storytext li::text').re('Featured Song: "(.+)"')
        yield {
            'artists': artists,
            'albums': albums,
            'songs': songs
        }

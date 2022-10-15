import scrapy
import logging

class PauvreteSpider(scrapy.Spider):
    name = 'pauvrete'
    allowed_domains = ['www.seneweb.com/news/Pauvrete']
    start_urls = ['https://www.seneweb.com/news/Pauvrete']

    def parse(self, response):
        pauvrete = response.xpath("//td/0")
        for poverty in pauvrete:
            name = pauvrete.xpath(".//text()").get()
            title = pauvrete.xpath(".//@href").get()
            description = pauvrete.xpath(".//@href").get()
            pub_date = pauvrete.xpath(".//text()").get()
            views = pauvrete.xpath(".//text()").get()
            comments = pauvrete.xpath(".//text()").get()

        yield {
            'poverty_source':poverty,
            'title':title,
            'description':description,
            'pub_date':pub_date,
            'views':views,
            'comments':comments


        }
        yield response.follow(url=title)
        yield response.follow(url=description)
        pass

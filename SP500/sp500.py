import scrapy


class Sp500Spider(scrapy.Spider):
    name = "sp500"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        rows = response.xpath('//table[contains(@class, "table")]/tbody/tr')

        for row in rows:
            yield {
                "Number": row.xpath("td[1]/text()").get(),
                "Company": row.xpath("td[2]/a/text()").get(),
                "Symbol": row.xpath("td[3]//text()").get(),
                "YTD Return": row.xpath("td[last()]//text()").get(), 
            }


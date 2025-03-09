import scrapy
import csv

class Sp500PerformanceSpider(scrapy.Spider):
    name = "sp500_performance"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://slickcharts.com"]

    def parse(self, response):
        rows = response.xpath("//table[@class='table-hover']/tbody/tr")

        data = []
        for row in rows:
            number = row.xpath(".//td[1]/text()").get()
            company = row.xpath(".//td[2]/a/text()").get()
            symbol = row.xpath(".//td[3]/text()").get()
            ytd_return = row.xpath(".//td[7]/text()").get()

            data.append([number, company, symbol, ytd_return])

        # Save to CSV file
        with open("sp500_performance.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Number", "Company", "Symbol", "YTD Return"])
            writer.writerows(data)


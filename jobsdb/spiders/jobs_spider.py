import scrapy
from jobsdb.items import JobsItem

class JobsdbSpider(scrapy.Spider):
    name = "jobsdb"
    allowed_domains = ["hk.jobsdb.com"]
    start_urls = [
		"http://hk.jobsdb.com/HK/en/Search/FindJobs?AD=3&Blind=1&Host=J&JSRV=1&Key=programmer&KeyOpt=COMPLEX&SearchFields=Positions%2cCompanies&page=0"
    ]

    def parse(self, response):
			for sel in response.xpath('//div[@class="job-main"]'):
				item = JobsItem()
				position_list = sel.xpath('*/a[@class="posLink"]//text()').extract()
				item['position'] = ''.join(position_list)
				item['company'] = sel.xpath('*//meta[@itemprop="name"]/@content').extract()
				item['address'] = sel.xpath('*//span[@itemprop="address"]/text()').extract()
				item['link'] = sel.xpath('*/a[@class="posLink"]/@href').extract()
				yield item
			
			next_page = response.xpath('//a[@class="pagebox pagebox-next"]/@href')
			
			if next_page:
				yield scrapy.Request(next_page[0].extract(), self.parse)


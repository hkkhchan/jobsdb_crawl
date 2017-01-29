import scrapy
from jobsdb.items import JobsItem

class JobsdbSpider(scrapy.Spider):
    name = "jobsdb"
    allowed_domains = ["hk.jobsdb.com"]
    start_urls = [
        "http://hk.jobsdb.com/HK/EN/Search/FindJobs?KeyOpt=COMPLEX&JSRV=1&RLRSF=1&JobCat=1&SearchFields=Positions,Companies&Key=programmer"
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


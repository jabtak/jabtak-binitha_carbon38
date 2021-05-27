import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'quotes'
    #allowed_domains = ['www.carbon38.com/shop-all-activewear/tops']
    start_urls = ['https://www.carbon38.com/shop-all-activewear/tops']

    def parse(self, response):
       urls = response.css(".product-item-link::attr(href)").extract()
       for url in urls:
           url = response.urljoin(url)
           yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self,response):
        scraped_info = {
            'brand': response.css("div.brand > a > span::text").extract_first(),
            'price': response.css("span.price::text").extract_first(),
            'image url': response.css("a.cloud-zoom > img::attr(src)").extract_first(),
            'product name': response.css("div.product_name > span::text").extract_first(),
            'product review': response.css("div.pdp_info_reviewCount::text").extract()[1],
            'colour': response.css("span.current::text").extract_first(),
            'description': response.css("div.value  > p::text").extract_first(),
            'product id': response.css("div.product-add-form > form ::attr(data-product-id)").extract_first(),
            'SKU': response.css("div.product-add-form > form ::attr(data-product-sku)").extract_first()

        }
        yield scraped_info

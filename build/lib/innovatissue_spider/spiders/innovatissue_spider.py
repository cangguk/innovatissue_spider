import scrapy

class testSpider(scrapy.Spider):
    name = 'innovatissue_spider'
    allowed_domains = ['innovatissue.it']
    start_urls = ['https://www.innovatissue.it/second-hand/']

    def parse(self, response):  
        category_url = response.xpath('//h5[@class="mkd-product-list-title"]/a/@href').extract()
        #category_url = response.xpath('//h3/a[contains(@href,"/winkel/")]/@href').extract()
        for url1 in category_url:
            url_desc = response.urljoin(url1)
            yield scrapy.Request(url=url_desc, callback = self.parse_item)

   
    def parse_item(self, response):
        Url = response.url
        #Reference = Url[-5:]
        #Url = Urls.replace('://','://www.')
        #UUrl = Url.replace('usata','used')
        #UR = response.meta['URL']
        #Url = Urls + '?lang=en'
        #Description = response.xpath('//h1[@class="et_pb_column et_pb_column_1_2 et_pb_column_4_tb_body  et_pb_css_mix_blend_mode_passthrough et-last-child"]/text()|'
                                     #'//div[@class="LibDetailCaract"]/p[2]/text()|'
                                     #'//div[@class="page-link"]/p[3]/text()|'
                                     #'//div[@class="left_p"]/p[4]/text()|'
                                     #'//div[@class="post-content"]/p[5]/text()|'
                                     #'//h1[@class="uael-heading"]/strong/text()').extract()
        #Description = response.xpath('//div[@id="tab1"]/ul[string-length(text()) > 0]/text()').extract()
        #Price = response.xpath('//*[@id="price"]/div/span/text()').extract()
        Reference = response.xpath('//span[@class="sku"]/text()').extract()
        #Model = response.xpath('//html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/h1/font/font/text()').extract()
   #Year = response.xpath('//strong[contains (text(),"Year : ")]/ancestor::div/text()').extract()
        Year = response.xpath('//span[@class="year"]/text()').extract()
        #Price = response.xpath('//td[@id="salePrice"]/strong/text()').extract()
        #----

      
        yield {#'description': Description,
               #'model': Model,#
               'reference': Reference,
               #'priceee': Pricee,
               'year': Year,
               #'price': Price,
               #'image': Img,
               #'urlreal': response.url,
               'url': Url,}
             #yield scrapy.Request(item_url, callback=self.parse_cat)

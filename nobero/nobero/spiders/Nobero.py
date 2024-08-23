import scrapy
import json
from nobero.items import Variant, Product

class NoberoSpider(scrapy.Spider):
    name = "Nobero"
    allowed_domains = ["nobero.com"]
    
    def start_requests(self):
        urls = [
            "https://nobero.com/collections/men-oversized-t-shirts", 
            "https://nobero.com/collections/pick-printed-t-shirts",
            "https://nobero.com/collections/best-selling-co-ord-sets",
            "https://nobero.com/collections/fashion-joggers-men",
            "https://nobero.com/collections/mens-shorts-collection",
            "https://nobero.com/collections/plus-size-t-shirts",
        ]
        
        # product = Product()
        # yield scrapy.Request(url="https://nobero.com/products/co-ord-set?variant=44185195184294", callback=self.parseProduct, cb_kwargs=dict(product=product))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css(".product-card-container a::attr(href)")
        # category = response.url.split("/")[-1].split("?")[0]
        parent = response.css("h1::text").get()
        for link in links:
            product = Product()
            product["parent"] = response.css("h1::text").get()
            yield response.follow(link.get(), callback=self.parseProduct, cb_kwargs=dict(product=product))
        
        next_page = response.css("#load-more-products a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parseNextPage, cb_kwargs=dict(parent=parent))
        
        # link = response.css(".product-card-container a::attr(href)").get()
        # yield self.parse(response)

    def parseNextPage(self, response, parent):
        links = response.css(".product-card-container a::attr(href)")
        for link in links:
            product = Product()
            product["parent"] = parent
            yield response.follow(link.get(), callback=self.parseProduct, cb_kwargs=dict(product=product))
        
        next_page = response.css("#load-more-products a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parseNextPage, cb_kwargs=dict(parent=parent))        

    def parseProduct(self, response, product):
        availSize = set({"S", "M", "L", "XL", "XXL", "XXXL", "4XL", "5XL", "6XL", "7XL"})
        
        data = response.css("div.px-4>script::text")[0].get().strip().split("const ")[1].replace("_product =", "")
        # data = response.css("script.product-json::text").get()
        data = json.loads(data)
        
        # last 7 day sale value
        sale = response.css("div > img+span ::text").get()
        if sale is not None: 
            sale = sale.strip().split()[0]
        else:
            sale = 0
        
        # variants/colors data
        variants = response.css("option")
        variantData = {}
        for variant in variants:
            options = variant.css("::attr(data-variant)").get().split("-")
            # options = variant.css("::text").get().split("/")
            quantity = variant.css("::attr(data-variant-qty)").get()
            if options[0] in availSize:
                size = options[0]
                color = options[1]
            else:
                color = options[0]
                size = options[1]
            
            if color not in variantData:
                variantData[color] = Variant()
                variantData[color]["size"] = []
                variantData[color]["quantity"] = []
                variantData[color]["color"] = color
            
            variantData[color]["size"].append(size)
            variantData[color]["quantity"].append(quantity)
        
        # image data
        for variant in data["variants"]:
            if variant["option1"] in availSize:
                color = variant["option2"]
            else:
                color = variant["option1"]
            
            image = variant["featured_image"]
            if variant["featured_image"] is not None:
                image = variant["featured_image"]["src"]
            
            variantData[color]["image"] = image
        
        product["category"] = data["type"]
        product["url"] = response.url
        product["title"] = data["title"]
        product["price"] = response.css("#variant-price * ::text").get()
        product["mrp"] = response.css("#variant-compare-at-price * ::text").get()
        product["weekly_sale"] = sale
        product["variants"] = list(variantData.values())
        product["description"] = data["description"]
        product["images"] = data["images"]
        
        # meta data
        fields = response.css("div.product-metafields-values * ::text").getall()
        
        i = 0
        while i < len(fields):
            key = ""
            key = key.join(fields[i].casefold().split())
            value = fields[i+1]
            product[key] = value
            i += 2
        
        return product
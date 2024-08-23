# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NoberoItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass
    
class Product(Item):
    parent = Field()
    category = Field()
    url = Field()
    title = Field()
    price = Field()
    mrp = Field()
    weekly_sale = Field()
    description = Field()
    variants = Field()
    images = Field()
    fit = Field()
    fabric = Field()
    pattern = Field()
    neck = Field()
    sleeve = Field()
    length = Field()
    waistrise = Field()
    waistband = Field()
    bottomwearlength = Field()

class Variant(Item):
    color = Field()
    image = Field()
    size = Field()
    quantity = Field()
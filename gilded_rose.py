# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.callback = {"Aged Brie": self.update_quality_aged_brie,
                         "Sulfuras, Hand of Ragnaros": self.update_quality_sulfuras,
                         "Backstage passes to a TAFKAL80ETC concert": self.update_quality_backstage,
                         "Conjured": self.update_quality_conjured}

    def update_quality(self):

        for item in self.items:
            self.callback.get(item.name, self.update_quality_common)(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                if item.quality > 50:
                    item.quality = 50

                if item.quality < 0:
                    item.quality = 0
                item.sell_in -= 1

    @staticmethod
    def update_quality_aged_brie(item):
        if item.sell_in > 0:
            item.quality += 1
        else:
            item.quality += 2

    @staticmethod
    def update_quality_sulfuras(item):
        pass

    @staticmethod
    def update_quality_backstage(item):
        if item.sell_in > 10:
            item.quality += 1
        elif 10 >= item.sell_in > 5:
            item.quality += 2
        elif 5 >= item.sell_in > 0:
            item.quality += 3
        elif item.sell_in <= 0:
            item.quality = 0

    @staticmethod
    def update_quality_conjured(item):
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4

    @staticmethod
    def update_quality_common(item):
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

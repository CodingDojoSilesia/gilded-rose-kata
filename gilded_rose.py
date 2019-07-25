# -*- coding: utf-8 -*-
from collections import defaultdict


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.updaters = defaultdict(
            lambda: self.default_updater,
            {
                'Aged Brie': self.aged_brie_updater,
                'Backstage passes to a TAFKAL80ETC concert': self.backstage_passes_updater,
                'Sulfuras, Hand of Ragnaros': self.sulfuras_updater,
                'Conjured': self.conjured_updater
            }
        )

    def sulfuras_updater(self, item):
        return None

    def default_updater(self, item):
        if item.sell_in <= 0:
            item.quality -= 2
        else:
            item.quality -= 1
        item.quality = max(0, item.quality)
        item.sell_in -= 1

    def aged_brie_updater(self, item):
        if item.sell_in <= 0:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(50, item.quality)
        item.sell_in -= 1

    def backstage_passes_updater(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(50, item.quality)
        item.sell_in -= 1

    def conjured_updater(self, item):
        if item.sell_in <= 0:
            item.quality -= 4
        else:
            item.quality -= 2
        item.quality = max(0, item.quality)
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            self.updaters[item.name](item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.sell_in, self.quality)

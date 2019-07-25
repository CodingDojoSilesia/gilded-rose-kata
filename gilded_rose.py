# -*- coding: utf-8 -*-
from collections import defaultdict

from updaters import (AgedBrieUpdater, BackstagePassesUpdater, ConjuredUpdater,
                      RegularUpdater, SulfurasUpdater)


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.updaters = defaultdict(
            lambda: RegularUpdater.tick,
            {
                'Aged Brie': AgedBrieUpdater.tick,
                'Backstage passes to a TAFKAL80ETC concert': BackstagePassesUpdater.tick,
                'Sulfuras, Hand of Ragnaros': SulfurasUpdater.tick,
                'Conjured': ConjuredUpdater.tick
            }
        )

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

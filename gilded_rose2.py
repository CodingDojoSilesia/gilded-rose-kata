# -*- coding: utf-8 -*-


def normal_tick(item):
  item.sell_in -= 1

  if item.quality == 0:
    return

  item.quality -= 1
  if item.sell_in <= 0:
    item.quality -= 1


def brie_tick(item):
  item.sell_in -= 1
  if item.quality >= 50:
    return

  item.quality += 1
  if item.sell_in <= 0:
    item.quality += 1


def backstage_tick(item):
  item.sell_in -= 1
  if item.quality >= 50:
    return

  if item.sell_in < 0:
    item.quality = 0
    return

  item.quality += 1

  if item.sell_in < 10:
    item.quality += 1
  
  if item.sell_in < 5:
    item.quality += 1

def sulfras_tick(item):
  pass

def conjured_tick(item):
  item.sell_in -= 1
  item.quality -= 2

  if item.sell_in < 0:
    item.quality -= 2

  if item.quality < 0:
    item.quality = 0




class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
      STRATEGIES = {
          'Aged Brie': brie_tick,
          'Backstage passes to a TAFKAL80ETC concert': backstage_tick,
          'Sulfuras, Hand of Ragnaros': sulfras_tick,
          'Conjured': conjured_tick,
      }
      for item in self.items:
        strategy = STRATEGIES.get(item.name, normal_tick)
        strategy(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

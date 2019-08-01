class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                update_backstage(item)
            elif (item.name == "Aged Brie"):
                update_Aged(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Conjured":
                update_conjured(item)
            else:
                update_normal(item)
            item.sell_in -=1

def update_backstage(item):
        if 10 < item.sell_in:
            if item.quality < 50:
                item.quality += 1
            else:
                item.quality = 50
        elif 6 <= item.sell_in:
            if item.quality < 49:
                item.quality +=2
            else:
                item.quality = 50
        elif 0 < item.sell_in:
            if item.quality < 48: 
                item.quality +=3
            else:
                item.quality = 50
        else:
            item.quality = 0   
def update_Aged(item):
    if(item.quality < 50):
        if item.sell_in > 0:
            item.quality +=1
        else:
            item.quality +=2
def update_conjured(item):
    if item.quality > 0:
        if item.sell_in > 0:
            if(item.quality < 2):
                item.quality =0
            else:
                item.quality -=2
        else:
            if(item.quality < 4):
                    item.quality =0
            else:
                item.quality -=4
            
   
def update_normal(item):
    if item.quality > 0:
        if item.sell_in > 0:
            item.quality -=1
        else:
            item.quality -=2
    else:
        pass
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
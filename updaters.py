""" Updater for regular items. """
from abc import ABCMeta, abstractmethod


class AbstractUpdater(ABCMeta):

    @abstractmethod
    def tick(item):
        pass


class SulfurasUpdater(AbstractUpdater):

    @staticmethod
    def tick(item):
        return None


class RegularUpdater(AbstractUpdater):

    @staticmethod
    def tick(item):
        if item.sell_in <= 0:
            item.quality -= 2
        else:
            item.quality -= 1
        item.quality = max(0, item.quality)
        item.sell_in -= 1


class AgedBrieUpdater(AbstractUpdater):

    @staticmethod
    def tick(item):
        if item.sell_in <= 0:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(50, item.quality)
        item.sell_in -= 1


class BackstagePassesUpdater(AbstractUpdater):

    @staticmethod
    def tick(item):
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


class ConjuredUpdater(AbstractUpdater):

    @staticmethod
    def tick(item):
        if item.sell_in <= 0:
            item.quality -= 4
        else:
            item.quality -= 2
        item.quality = max(0, item.quality)
        item.sell_in -= 1

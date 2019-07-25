from gilded_rose import Item
from gilded_rose import GildedRose


class ItemEnum:
    NORMAL = "normal"
    BRIE = "Aged Brie"
    SULFRAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


def test_normal_item_before_sell_date():
    item = Item(ItemEnum.NORMAL, 5, 10)

    GildedRose([item]).update_quality()

    assert item.sell_in == 4
    assert item.quality == 9


def test_normal_item_on_sell_date():
    item = Item(ItemEnum.NORMAL, 0, 6)

    GildedRose([item]).update_quality()

    assert item.sell_in == -1
    assert item.quality == 4


def test_normal_item_after_sell_date():
    item = Item(ItemEnum.NORMAL, -1, 3)

    GildedRose([item]).update_quality()

    assert item.sell_in == -2
    assert item.quality == 1


def test_normal_item_of_zero_quality():
    item = Item(ItemEnum.NORMAL, 5, 0)

    GildedRose([item]).update_quality()

    assert item.sell_in == 4
    assert item.quality == 0


def test_normal_item_of_maximum_quality():
    item = Item(ItemEnum.NORMAL, 5, 50)

    GildedRose([item]).update_quality()

    assert item.sell_in == 4
    assert item.quality == 49


def test_aged_brie_before_sell_date():
    item = Item(ItemEnum.BRIE, 5, 11)

    GildedRose([item]).update_quality()

    assert item.sell_in == 4
    assert item.quality == 12


def test_aged_brie_on_sell_date():
    item = Item(ItemEnum.BRIE, 0, 11)

    GildedRose([item]).update_quality()

    assert item.sell_in == -1
    assert item.quality == 13


def test_aged_brie_after_sell_date():
    item = Item(ItemEnum.BRIE, -1, 15)

    GildedRose([item]).update_quality()

    assert item.sell_in == -2
    assert item.quality == 17


def test_aged_brie_of_maximum_quality():
    item = Item(ItemEnum.BRIE, 10, 50)

    GildedRose([item]).update_quality()

    assert item.sell_in == 9
    assert item.quality == 50


def test_aged_brie_of_zero_quality():
    item = Item(ItemEnum.BRIE, -1, 0)

    GildedRose([item]).update_quality()

    assert item.sell_in == -2
    assert item.quality == 2


def test_sulfras_before_sell_date():
    item = Item(ItemEnum.SULFRAS, 10, 22)

    GildedRose([item]).update_quality()

    assert item.sell_in == 10
    assert item.quality == 22


def test_sulfras_on_sell_date():
    item = Item(ItemEnum.SULFRAS, 0, 22)

    GildedRose([item]).update_quality()

    assert item.sell_in == 0
    assert item.quality == 22


def test_sulfras_after_sell_date():
    item = Item(ItemEnum.SULFRAS, -1, 22)

    GildedRose([item]).update_quality()

    assert item.sell_in == -1
    assert item.quality == 22


def test_sulfras_of_maximum_quality():
    item = Item(ItemEnum.SULFRAS, 10, 80)

    GildedRose([item]).update_quality()

    assert item.sell_in == 10
    assert item.quality == 80


def test_backstage_more_than_10_days_sell_date():
    item = Item(ItemEnum.BACKSTAGE, 12, 22)

    GildedRose([item]).update_quality()

    assert item.sell_in == 11
    assert item.quality == 23


def test_backstage_10_days_sell_date():
    item = Item(ItemEnum.BACKSTAGE, 10, 22)

    GildedRose([item]).update_quality()

    assert item.sell_in == 9
    assert item.quality == 24


def test_backstage_more_than_5_days_less_than_10_days_sell_date():
    item = Item(ItemEnum.BACKSTAGE, 6, 11)

    GildedRose([item]).update_quality()

    assert item.sell_in == 5
    assert item.quality == 13


def test_backstage_5_days_sell_date():
    item = Item(ItemEnum.BACKSTAGE, 5, 33)

    GildedRose([item]).update_quality()

    assert item.sell_in == 4
    assert item.quality == 36


def test_backstage_less_than_5_days_sell_date():
    item = Item(ItemEnum.BACKSTAGE, 2, 33)

    GildedRose([item]).update_quality()

    assert item.sell_in == 1
    assert item.quality == 36


def test_backstage_on_sell_date():
    item = Item(ItemEnum.BACKSTAGE, 0, 9)

    GildedRose([item]).update_quality()

    assert item.sell_in == -1
    assert item.quality == 0


def test_backstage_after_sell_date():
    item = Item(ItemEnum.BACKSTAGE, -1, 19)

    GildedRose([item]).update_quality()

    assert item.sell_in == -2
    assert item.quality == 0


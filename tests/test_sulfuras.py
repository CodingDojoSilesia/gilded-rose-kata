from gilded_rose import GildedRose, Item


class TestSulfuras:
    def test_before_sell_date(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 15, 10)
        gr = GildedRose([sulfuras])
        gr.update_quality()

        assert sulfuras.sell_in == 15
        assert sulfuras.quality == 10

    def test_at_zero_quality(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 15, 0)
        gr = GildedRose([sulfuras])
        gr.update_quality()

        assert sulfuras.sell_in == 15
        assert sulfuras.quality == 0

    def test_on_sell_date(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 0, 10)
        gr = GildedRose([sulfuras])
        gr.update_quality()

        assert sulfuras.sell_in == 0
        assert sulfuras.quality == 10

    def test_on_sell_date_at_zero_quality(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 0, 0)
        gr = GildedRose([sulfuras])
        gr.update_quality()

        assert sulfuras.sell_in == 0
        assert sulfuras.quality == 0

    def test_after_sell_date(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", -1, 10)
        gr = GildedRose([sulfuras])
        gr.update_quality()

        assert sulfuras.sell_in == -1
        assert sulfuras.quality == 10

    def test_after_sell_date_at_zero_quality(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", -1, 0)
        gr = GildedRose([sulfuras])
        gr.update_quality()

        assert sulfuras.sell_in == -1
        assert sulfuras.quality == 0

from gilded_rose import GildedRose, Item


class TestBackstagePasses:
    def test_before_sell_date(self):
        passes = Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)
        gr = GildedRose([passes])
        gr.update_quality()

        assert passes.sell_in == 14
        assert passes.quality == 11
        
    def test_at_zero_quality(self):
        passes = Item("Backstage passes to a TAFKAL80ETC concert", 15, 0)
        gr = GildedRose([passes])
        gr.update_quality()

        assert passes.sell_in == 14
        assert passes.quality == 1

    def test_on_sell_date(self):
        passes = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gr = GildedRose([passes])
        gr.update_quality()

        assert passes.sell_in == -1
        assert passes.quality == 0

    def test_on_sell_date_at_zero_quality(self):
        passes = Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)
        gr = GildedRose([passes])
        gr.update_quality()

        assert passes.sell_in == -1
        assert passes.quality == 0

    def test_after_sell_date(self):
        passes = Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)
        gr = GildedRose([passes])
        gr.update_quality()

        assert passes.sell_in == -2
        assert passes.quality == 0

    def test_after_sell_date_at_zero_quality(self):
        passes = Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)
        gr = GildedRose([passes])
        gr.update_quality()

        assert passes.sell_in == -2
        assert passes.quality == 0

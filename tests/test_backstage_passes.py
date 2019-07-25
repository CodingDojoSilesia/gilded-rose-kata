from gilded_rose import GildedRose, Item


class TestBackstagePasses:

    def test_before_sell_date_ten_and_more(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == 14
        assert backstage_passes.quality == 11

    def test_before_sell_date_ten_and_less(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == 9
        assert backstage_passes.quality == 12

    def test_before_sell_date_five_and_less(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == 4
        assert backstage_passes.quality == 13

    def test_at_zero_quality(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 15, 0)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == 14
        assert backstage_passes.quality == 1

    def test_on_sell_date(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == -1
        assert backstage_passes.quality == 0

    def test_on_sell_date_at_zero_quality(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == -1
        assert backstage_passes.quality == 0

    def test_after_sell_date(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == -2
        assert backstage_passes.quality == 0

    def test_after_sell_date_at_zero_quality(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)
        gr = GildedRose([backstage_passes])
        gr.update_quality()

        assert backstage_passes.sell_in == -2
        assert backstage_passes.quality == 0


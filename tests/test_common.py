from gilded_rose import GildedRose, Item


class TestCommon:
    def test_before_sell_date(self):
        common = Item("Common", 15, 10)
        gr = GildedRose([common])
        gr.update_quality()

        assert common.sell_in == 14
        assert common.quality == 9

    def test_at_zero_quality(self):
        common = Item("Common", 15, 0)
        gr = GildedRose([common])
        gr.update_quality()

        assert common.sell_in == 14
        assert common.quality == 0

    def test_on_sell_date(self):
        common = Item("Common", 0, 10)
        gr = GildedRose([common])
        gr.update_quality()

        assert common.sell_in == -1
        assert common.quality == 8

    def test_on_sell_date_at_zero_quality(self):
        common = Item("Common", 0, 0)
        gr = GildedRose([common])
        gr.update_quality()

        assert common.sell_in == -1
        assert common.quality == 0

    def test_after_sell_date(self):
        common = Item("Common", -1, 10)
        gr = GildedRose([common])
        gr.update_quality()

        assert common.sell_in == -2
        assert common.quality == 8

    def test_after_sell_date_at_zero_quality(self):
        common = Item("Common", -1, 0)
        gr = GildedRose([common])
        gr.update_quality()

        assert common.sell_in == -2
        assert common.quality == 0

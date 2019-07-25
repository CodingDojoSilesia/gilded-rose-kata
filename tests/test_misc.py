from gilded_rose import GildedRose, Item


class TestConjured:
    def test_before_sell_date(self):
        item = Item("qwerty", 15, 10)
        gr = GildedRose([item])
        gr.update_quality()

        assert item.sell_in == 14
        assert item.quality == 9

    def test_at_zero_quality(self):
        item = Item("qwerty", 15, 0)
        gr = GildedRose([item])
        gr.update_quality()

        assert item.sell_in == 14
        assert item.quality == 0

    def test_on_sell_date(self):
        item = Item("qwerty", 0, 10)
        gr = GildedRose([item])
        gr.update_quality()

        assert item.sell_in == -1
        assert item.quality == 8

    def test_on_sell_date_at_zero_quality(self):
        item = Item("qwerty", 0, 0)
        gr = GildedRose([item])
        gr.update_quality()

        assert item.sell_in == -1
        assert item.quality == 0

    def test_after_sell_date(self):
        item = Item("qwerty", -1, 10)
        gr = GildedRose([item])
        gr.update_quality()

        assert item.sell_in == -2
        assert item.quality == 8

    def test_after_sell_date_at_zero_quality(self):
        item = Item("qwerty", -1, 0)
        gr = GildedRose([item])
        gr.update_quality()

        assert item.sell_in == -2
        assert item.quality == 0

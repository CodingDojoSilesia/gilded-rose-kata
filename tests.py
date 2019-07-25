from gilded_rose import GildedRose, Item


class TestConjured:
    def test_before_sell_date(self):
        conjured = Item("Conjured", 15, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 8

    def test_at_zero_quality(self):
        conjured = Item("Conjured", 15, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 0

    def test_on_sell_date(self):
        conjured = Item("Conjured", 0, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 6

    def test_on_sell_date_at_zero_quality(self):
        conjured = Item("Conjured", 0, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 0

    def test_after_sell_date(self):
        conjured = Item("Conjured", -1, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 6

    def test_after_sell_date_at_zero_quality(self):
        conjured = Item("Conjured", -1, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 0

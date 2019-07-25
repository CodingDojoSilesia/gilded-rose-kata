from gilded_rose import GildedRose, Item


class TestBrie:
    def test_before_sell_date(self):
        brie = Item("Aged Brie", 15, 10)
        gr = GildedRose([brie])
        gr.update_quality()

        assert brie.sell_in == 14
        assert brie.quality == 11

    def test_at_zero_quality(self):
        brie = Item("Aged Brie", 15, 0)
        gr = GildedRose([brie])
        gr.update_quality()

        assert brie.sell_in == 14
        assert brie.quality == 1

    def test_on_sell_date(self):
        brie = Item("Aged Brie", 0, 10)
        gr = GildedRose([brie])
        gr.update_quality()

        assert brie.sell_in == -1
        assert brie.quality == 12

    def test_on_sell_date_at_zero_quality(self):
        brie = Item("Aged Brie", 0, 0)
        gr = GildedRose([brie])
        gr.update_quality()

        assert brie.sell_in == -1
        assert brie.quality == 2

    def test_after_sell_date(self):
        brie = Item("Aged Brie", -1, 10)
        gr = GildedRose([brie])
        gr.update_quality()

        assert brie.sell_in == -2
        assert brie.quality == 12

    def test_after_sell_date_at_zero_quality(self):
        brie = Item("Aged Brie", -1, 0)
        gr = GildedRose([brie])
        gr.update_quality()

        assert brie.sell_in == -2
        assert brie.quality == 2

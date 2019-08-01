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



class TestAgedBrie:
    
    def test_before_sell_date(self):
        conjured = Item("Aged Brie", 15, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 11

    def test_at_zero_quality(self):
        conjured = Item("Aged Brie", 15, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 1

    def test_on_sell_date(self):
        conjured = Item("Aged Brie", 0, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 12

    def test_on_sell_date_at_zero_quality(self):
        conjured = Item("Aged Brie", 0, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 2


    def test_after_sell_date(self):
        conjured = Item("Aged Brie", -1, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 12

    def test_after_sell_date_at_zero_quality(self):
        conjured = Item("Aged Brie", -1, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 2

    def test_after_sell_date_at_max_quality(self):
        conjured = Item("Aged Brie", -1, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 50
    
    def test_on_sell_date_at_max_quality(self):
        conjured = Item("Aged Brie", 0, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 50

    def test_before_sell_date_at_max_quality(self):
        conjured = Item("Aged Brie", 15, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 50


class TestBackstagePasses:
    
    def test_more_than_ten_and_zero_quality(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 15, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 1

    def test_at_zero_quality_and_before_fifth_day(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 4
        assert conjured.quality == 3

    def test_on_sell_date(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 0

    def test_on_sell_date_at_zero_quality(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 0

    def test_after_sell_date(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 0

    def test_after_sell_date_at_zero_quality(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 0

    def test_on_sell_date_at_max_quality(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 0

    def test_at_zero_quality_and_before_tenth_day(self):
       
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 9
        assert conjured.quality == 2

    def test_before_fifth_day(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 4
        assert conjured.quality == 13

    def test_before_tenth_day(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 9
        assert conjured.quality == 12
    
    def test_after_tenth_day(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 10
        assert conjured.quality == 11

    def test_at_max_value_after_sell_date(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", -1, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 0

    def test_at_max_value_at_normal_time(self):
        conjured = Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 10
        assert conjured.quality == 50


class TestNormal:


    def test_before_sell_date(self):
        conjured = Item("Normal", 15, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 9

    def test_at_zero_quality(self):
        conjured = Item("Normal", 15, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 14
        assert conjured.quality == 0

    def test_on_sell_date(self):
        conjured = Item("Normal", 0, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 8

    def test_on_sell_date_at_zero_quality(self):
        conjured = Item("Normal", 0, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 0

    def test_after_sell_date(self):
        conjured = Item("Normal", -1, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 8
        
    def test_after_sell_date_at_zero_quality(self):
        conjured = Item("Normal", -1, 0)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 0

    def test_max_value(self):
        conjured = Item("Normal", 5, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 4
        assert conjured.quality == 49
    
    def test_at_sell_date_at_max_quality(self):
        conjured = Item("Normal", 0, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 48
    
    def test_after_sell_date_max_quality(self):
        conjured = Item("Normal", -1, 50)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -2
        assert conjured.quality == 48



class TestSulfuras:

    def test_before_sell_date(self):
        conjured = Item("Sulfuras, Hand of Ragnaros", 15, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 15
        assert conjured.quality == 10

    def test_at_sell_date(self):
        conjured = Item("Sulfuras, Hand of Ragnaros", 0, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == 0
        assert conjured.quality == 10

    def test_after_sell_date(self):
        conjured = Item("Sulfuras, Hand of Ragnaros", -1, 10)
        gr = GildedRose([conjured])
        gr.update_quality()

        assert conjured.sell_in == -1
        assert conjured.quality == 10


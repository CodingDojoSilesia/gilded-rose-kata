from gilded_rose import GildedRose, Item


def test_number_one():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
    ]

    gr = GildedRose(items)
    gr.update_quality()

    # verification
    vest, brie = gr.items

    assert vest.sell_in == 9
    assert vest.quality == 19

    assert brie.sell_in == 1
    assert brie.quality == 1

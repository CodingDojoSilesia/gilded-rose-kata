const { GildedRose, Item } = require('../gilded_rose');

test('FAIL', () => {
	const items = [new Item('foo', 0, 0)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item('foo', -1, 0)]);
});
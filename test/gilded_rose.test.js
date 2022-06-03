const { GildedRose, Item } = require('../gilded_rose');

const ItemEnum = {
    NORMAL: "normal",
    BRIE: "Aged Brie",
    SULFRAS: "Sulfuras, Hand of Ragnaros",
    BACKSTAGE: "Backstage passes to a TAFKAL80ETC concert",
    CONJURED: "Conjured"
};

test('Test normal item before sell date', () => {
	const items = [new Item(ItemEnum.NORMAL, 5, 10)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.NORMAL, 4, 9)]);
});

test('Test normal item on sell date', () => {
	const items = [new Item(ItemEnum.NORMAL, 0, 6)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.NORMAL, -1, 4)]);
});

test('Test normal item after sell date', () => {
	const items = [new Item(ItemEnum.NORMAL, -1, 3)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.NORMAL, -2, 1)]);
});

test('Test normal item of zero quality', () => {
	const items = [new Item(ItemEnum.NORMAL, 5, 0)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.NORMAL, 4, 0)]);
});

test('Test normal item of maximum quality', () => {
	const items = [new Item(ItemEnum.NORMAL, 5, 50)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.NORMAL, 4, 49)]);
});

test('Test aged brie before sell date', () => {
	const items = [new Item(ItemEnum.BRIE, 5, 11)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BRIE, 4, 12)]);
});

test('Test aged brie on sell date', () => {
	const items = [new Item(ItemEnum.BRIE, 0, 11)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BRIE, -1, 13)]);
});

test('Test aged brie after sell date', () => {
	const items = [new Item(ItemEnum.BRIE, -1, 15)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BRIE, -2, 17)]);
});

test('Test aged brie of maximum quality', () => {
	const items = [new Item(ItemEnum.BRIE, 10, 50)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BRIE, 9, 50)]);
});

test('Test aged brie of zero quality', () => {
	const items = [new Item(ItemEnum.BRIE, -1, 0)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BRIE, -2, 2)]);
});

test('Test sulfuras before sell date', () => {
	const items = [new Item(ItemEnum.SULFRAS, 10, 22)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.SULFRAS, 10, 22)]);
});

test('Test sulfuras on sell date', () => {
	const items = [new Item(ItemEnum.SULFRAS, 0, 22)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.SULFRAS, 0, 22)]);
});

test('Test sulfuras after sell date', () => {
	const items = [new Item(ItemEnum.SULFRAS, -1, 22)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.SULFRAS, -1, 22)]);
});

test('Test sulfuras of maximum quality', () => {
	const items = [new Item(ItemEnum.SULFRAS, 10, 80)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.SULFRAS, 10, 80)]);
});

test('Test backstage more than 10 days sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, 12, 22)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, 11, 23)]);
});

test('Test backstage 10 days sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, 10, 22)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, 9, 24)]);
});

test('Test backstage more than 5 days, less than 10 days sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, 6, 11)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, 5, 13)]);
});

test('Test backstage 5 days sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, 5, 33)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, 4, 36)]);
});

test('Test backstage less than 5 days sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, 2, 33)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, 1, 36)]);
});

test('Test backstage on sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, 0, 9)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, -1, 0)]);
});

test('Test backstage after sell date', () => {
	const items = [new Item(ItemEnum.BACKSTAGE, -1, 19)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.BACKSTAGE, -2, 0)]);
});

test('Test conjured before sell date', () => {
	const items = [new Item(ItemEnum.CONJURED, 15, 10)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.CONJURED, 14, 8)]);
});

test('Test conjured at zero quality', () => {
	const items = [new Item(ItemEnum.CONJURED, 15, 0)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.CONJURED, 14, 0)]);
});

test('Test conjured on sell date', () => {
	const items = [new Item(ItemEnum.CONJURED, 0, 10)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.CONJURED, -1, 6)]);
});

test('Test conjured on sell date at zero quality', () => {
	const items = [new Item(ItemEnum.CONJURED, 0, 0)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.CONJURED, -1, 0)]);
});

test('Test conjured after sell date', () => {
	const items = [new Item(ItemEnum.CONJURED, -1, 10)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.CONJURED, -2, 6)]);
});

test('Test conjured after sell date at zero quality', () => {
	const items = [new Item(ItemEnum.CONJURED, -1, 0)];
	const app = new GildedRose(items);
	expect(app.updateQuality()).toEqual([new Item(ItemEnum.CONJURED, -2, 0)]);
});

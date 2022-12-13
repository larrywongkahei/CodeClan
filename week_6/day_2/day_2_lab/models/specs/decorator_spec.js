const assert = require('assert');
const Decorator = require('../decorator.js');
const Room = require('../room.js');
const Paint_can = require('../paint_can.js');

describe('Room', function(){
    let room;
    beforeEach(function(){
        room = new Room(30);
    })

    it('should have an area in square meters', function(){
        const actual = room.area
        assert.strictEqual(actual, 30)
    })

    it('should start not painted', function(){
        const actual = room.painted
        assert.strictEqual(actual, false)
    })

    it('should be able to be painted', function(){
        room.Paint()
        const actual = room.painted
        assert.strictEqual(actual, true)
    })
})

describe('Paint', function(){
    let paint;
    beforeEach(function(){
        paint = new Paint_can(20);
    })

    it('should have a number of litres', function(){
        const actual = paint.litres
        assert.strictEqual(actual, 20)
    })

    it('should be able to check if it is empty', function(){
        const actual = paint.check_if_empty();
        assert.strictEqual(actual, false)
    })

    it('should be able to empty itself', function(){
        paint.empty();
        const actual = paint.check_if_empty();
        assert.strictEqual(actual, true)
    })
})

describe('Decorator', function(){
    let decorator;
    beforeEach(function(){
        decorator = new Decorator();
    })

    it('should start with an empty paint stock', function(){
        const actual = decorator.stock.length;
        assert.strictEqual(actual, 0);
    })

    it('should be able to calculate total litres paint it has in stock', function(){
        let paint1 = new Paint_can(20);
        decorator.addCanToStock(paint1);
        let paint2 = new Paint_can(20);
        decorator.addCanToStock(paint2);
        let paint3 = new Paint_can(20);
        decorator.addCanToStock(paint3);
        let paint4 = new Paint_can(20);
        decorator.addCanToStock(paint4);
        let paint5 = new Paint_can(20);
        decorator.addCanToStock(paint5);
        let paint6 = new Paint_can(15);
        decorator.addCanToStock(paint6);
        const actual = decorator.cal_stock();

        assert.strictEqual(actual, 115)
    })

    it('should be able to push a paint', function(){
        
        decorator.addCanToStock('red');
        const actual = decorator.stock
        assert.deepStrictEqual(actual, ['red'])
    })

    it('should be able to calculate whether is has enough paint to paint a room', function(){
        let room = new Room(20);
        let paint1 = new Paint_can(20);
        decorator.addCanToStock(paint1);
        const actual = decorator.check_if_enough_to_paint(room);
        assert.strictEqual(actual, true)
    })

    it('should be able to paint room if has enough paint in stock', function(){
        let room = new Room(20);
        let paint = new Paint_can(20);
        decorator.addCanToStock(paint);
        decorator.paint_room(room);
        const actual = room.painted;
        assert.strictEqual(actual, true)

    })

    it('should be able to decrease amount of paint in stock when painting a room', function(){
        let paint1 = new Paint_can(20);
        decorator.addCanToStock(paint1);
        let paint2 = new Paint_can(20);
        decorator.addCanToStock(paint2);
        let paint3 = new Paint_can(20);
        decorator.addCanToStock(paint3);
        let room = new Room(50);
        decorator.paint_room(room)
        const actual = decorator.cal_stock();
        assert.strictEqual(actual, 10)
    })

    it('should be able to remove empty paint cans from stock', function(){
        let paint1 = new Paint_can(20);
        decorator.addCanToStock(paint1);
        let paint2 = new Paint_can(20);
        decorator.addCanToStock(paint2);
        let paint3 = new Paint_can(20);
        decorator.addCanToStock(paint3);
        let room = new Room(50);
        decorator.paint_room(room);
        const actual = decorator.stock.length
        assert.strictEqual(actual, 1)
    })

})

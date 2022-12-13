const assert = require('assert')
const Park = require('../park.js')
const Dinosaur = require('../dinosaur.js')

describe('Park', function(){
    let park;
    let dinosaur;
    beforeEach(function(){
        park = new Park("Larry's park", 500)
        dinosaur = new Dinosaur("Tyrannosaurus rex", "carnivore", 20)
        dinosaur2 = new Dinosaur("Brighstoneus simmondsi", "plant", 60)
        dinosaur3 = new Dinosaur("Cryolophosaurus ellioti", "carnivore", 26)
        dinosaur4 = new Dinosaur("Bellusaurus sui", "plant", 78)
        dinosaur5 = new Dinosaur("Bellusaurus sui", "plant", 34)
        dinosaur_object = {
            "Brighstoneus simmondsi" : 1,
            "Cryolophosaurus ellioti" : 1,
            "Bellusaurus sui" : 2
        };
        park.addDinosaur(dinosaur5);
        park.addDinosaur(dinosaur2);
        park.addDinosaur(dinosaur3);
        park.addDinosaur(dinosaur4);

    })

    it('should be able to add a dinosaur to its collection', function(){
        const actual = park.collection.length;
        assert.strictEqual(actual, 4)
    })

    it('should be able to remove a dinosaur from collection', function(){
        park.removeDinosaur(dinosaur2);
        const actual = park.collection.length
        assert.strictEqual(actual, 3)
    })

    it('should be able to find the dinosaur that attracts the most visitors', function(){
        const actual = park.find_most_visitors();
        assert.strictEqual(actual, dinosaur4)
    })

    it('should be able to find all the dinosaurs of a particular species', function(){
        const actual = park.find_dinosaurs_by_species("Bellusaurus sui");
        assert.deepStrictEqual(actual, [dinosaur5, dinosaur4])
    })

    it('should be able to calculate the total number of visitiors per day', function(){
        const actual = park.cal_per_day();
        assert.strictEqual(actual, 198)
    })

    it('should be able to calculate the total number of visitiors per year', function(){
        const actual = park.cal_per_year();
        assert.strictEqual(actual, 72270)
    })

    it('should be able to calculate the total revenue fro ticket sales for one year', function(){
        const actual = park.cal_revenue_year();
        assert.strictEqual(actual, 36135000)
    })

    it('should be able to remove all dinosaurs with same species', function(){
        park.remove_same_species("Bellusaurus sui");
        const actual = park.collection.length
        assert.strictEqual(actual, 2)
    })

    it('should be able to provide an object', function(){
        const actual = park.provide_object();
        assert.deepStrictEqual(actual, dinosaur_object)
    })
})
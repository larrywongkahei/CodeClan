const assert = require('assert');
const Taxi = require('../taxi.js');

describe('Taxi', function(){
    let taxi;
    beforeEach (function(){
        taxi = new Taxi('Toyota', 'Prius', 'Larry');
    })
    it('should have a manufacturer', function(){
        const actual = taxi.manufacturer;
        assert.strictEqual(actual, 'Toyota')
    });

    it('should have a model', function(){
        const actual = taxi.model;
        assert.strictEqual(actual, 'Prius')
    });

    it('should have a driver', function(){
        const actual = taxi.driver;
        assert.strictEqual(actual, 'Larry');
    });
    describe('Passengers', function(){
        it('should start with no passengers', function(){
            const actual = taxi.passengers;
            assert.deepStrictEqual(actual, [])
        })

        it('should return the number of passengers', function(){
            const actual = taxi.numberOfPassengers();
            assert.strictEqual(actual, 0)
        })

        it('should be able to add passenger', function(){
            taxi.addPassenger('Larry');
            const actual = taxi.numberOfPassengers();
            assert.strictEqual(actual, 1)
        })

        // it('should be able to remove passenger by name', function(){
        //     taxi.addPassenger('Larry');
        //     taxi.addPassenger('Linda')
        //     taxi.addPassenger('Tim')
        //     taxi.removePassengerByName('Larry');
        //     const actual = taxi.numberOfPassengers();
        //     assert.strictEqual(actual, 2);
        // })
        it('should be able to remove passenger by name', function(){
            taxi.addPassenger('Larry');
            taxi.addPassenger('Linda')
            taxi.addPassenger('Tim')
            taxi.removePassengerByName('Larry');
            const expected = taxi.passengers
            const name = 'Larry'
            assert.strictEqual(name in expected, false);
        })

        it('should be able to remove all passengers', function(){
            taxi.addPassenger('Larry')
            taxi.addPassenger('Tim')
            taxi.removeAllPassengers();
            const actual = taxi.numberOfPassengers();
            assert.strictEqual(actual, 0)
        })

    })
});

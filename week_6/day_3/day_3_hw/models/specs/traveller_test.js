const assert = require('assert');
const Traveller = require('../traveller.js')
const Journey = require('../journey.js')


describe('Traveller', function(){

    let journey1;
    let journey2;
    let journey3;
    let journey4;
    let journey5;
    let journeys;
    let traveller;

    beforeEach(function(){
    journey1 = new Journey('linlithgow', 'stirling', 'train', 30);
    journey2 = new Journey('paris', 'frankfurt', 'train', 400);
    journey3 = new Journey('sydney', 'new york', 'aeroplane', 10000);
    journey4 = new Journey('london', 'rome', 'car', 1200);
    journey5 = new Journey('lancaster', 'isle of man', 'ferry', 80);
    journeys = [journey1, journey2, journey3, journey4, journey5];
    traveller = new Traveller(journeys);
  });

    it('Should have a collection of journeys', function(){
        const expected = journeys;
        const actual = traveller.Journeys;
        assert.deepStrictEqual(actual, expected)
    })

    it('should be able to get the journeys start locations', function(){
        const expected = traveller.getJourneysDetails('startLocation');
        const actual = ['linlithgow', 'paris', 'sydney', 'london', 'lancaster'];
        assert.deepStrictEqual(actual, expected)
    })

    it('should be able to get the journeys end locations', function(){
        const expected = traveller.getJourneysDetails('endLocation');
        const actual = ['stirling', 'frankfurt', 'new york', 'rome', 'isle of man']
        assert.deepStrictEqual(actual, expected)
    })

    it('should be able to get the journeys by transport', function(){
        const expected = traveller.getJourneyByTansport('car');
        const actual = [journey4]
        assert.deepStrictEqual(actual, expected)
    })

    it('should be able to get journeys over a certain distance', function(){
        const expected = traveller.getJourneysOverDistance(100);
        const actual = [journey2, journey3, journey4];
        assert.deepStrictEqual(actual, expected)
    })

    it('should be able to calculate total distance travellerd', function(){
        const expected = traveller.getTravelledTotal();
        const actual = 11710;
        assert.strictEqual(actual, expected)
    })

    it('should be able to get a unique list of modes of transport', function(){
        const expected = traveller.getUniqueTransport();
        const actual = ['train', 'aeroplane', 'car', 'ferry']
        assert.deepStrictEqual(actual, expected)
    })
})
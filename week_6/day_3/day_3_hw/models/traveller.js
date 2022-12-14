const Traveller = function(journeys){
    this.Journeys = journeys
}

Traveller.prototype.getJourneysDetails = function(property){
    return this.Journeys.map((journey) => journey[property])
}

Traveller.prototype.getJourneyByTansport = function(transport){
    return this.Journeys.filter((journey) => journey.modeOfTransport === transport);
}

Traveller.prototype.getJourneysOverDistance = function(distance){
    return this.Journeys.filter((journey) => journey.DistanceInMiles >= distance);
}

Traveller.prototype.getTravelledTotal = function(){
    return this.Journeys.reduce((previous, current) => previous + current.DistanceInMiles, 0)
}

Traveller.prototype.getUniqueTransport = function(){
    const transports = this.getJourneysDetails('modeOfTransport')
    return transports.filter((journey, index) => transports.indexOf(journey) === index)
}

module.exports = Traveller;
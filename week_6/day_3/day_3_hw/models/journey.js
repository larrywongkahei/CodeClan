const Journey = function(start_location, end_location, modeOfTransport, DistanceInMiles){
    this.startLocation = start_location;
    this.endLocation = end_location;
    this.modeOfTransport = modeOfTransport;
    this.DistanceInMiles = DistanceInMiles;
}



module.exports = Journey;
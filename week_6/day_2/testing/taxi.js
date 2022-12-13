const Taxi = function(manufacturer, model, driver){
    this.manufacturer = manufacturer;
    this.model = model;
    this.driver = driver;
    this.passengers = []
}

Taxi.prototype.numberOfPassengers = function(){
    return this.passengers.length

}


Taxi.prototype.addPassenger = function(name){
    this.passengers.push(name)
}

Taxi.prototype.removePassengerByName = function(name){
    for (let i = 0; i < this.passengers.length; i++){
        if (this.passengers[i] === name){
            this.passengers.splice(i, 1);
        }
    }
}

Taxi.prototype.removeAllPassengers = function(){
    this.passengers = []
}
module.exports = Taxi
const Dinosaur = require("./dinosaur");

const Park = function(name, ticket_price){
    this.name = name;
    this.ticket_price = ticket_price;
    this.collection = []
}

Park.prototype.addDinosaur = function(dinosaur){
    this.collection.push(dinosaur)
}

Park.prototype.removeDinosaur = function(dinosaur){
    for (let i = 0; i < this.collection.length; i++){
        if (this.collection[i].species === dinosaur.species){
            this.collection.splice(i, 1)
        }
    }
}

Park.prototype.find_most_visitors = function(){
    let number = 0
    let the_one;
    for (let i = 0; i < this.collection.length; i++){
        if (this.collection[i].number_of_visitors > number){
            number = this.collection[i].number_of_visitors;
            the_one = this.collection[i]
        }
    }
    return the_one;
}

Park.prototype.find_dinosaurs_by_species = function(species){
    let the_list = [];
    for (let i = 0; i < this.collection.length; i++){
        if (this.collection[i].species === species){
            the_list.push(this.collection[i])
        }
    }
    return the_list
}

Park.prototype.cal_per_day = function(){
    let total = 0
    for (let i = 0; i < this.collection.length; i++){
        total += this.collection[i].number_of_visitors
    }
    return total
}

Park.prototype.cal_per_year = function(){
    return this.cal_per_day() * 365
}

Park.prototype.cal_revenue_year = function(){
    return this.cal_per_year() * 500
}

Park.prototype.remove_same_species = function(species){ 
    let the_list = []
    for (let i = 0; i < this.collection.length; i++){
        if (this.collection[i].species !== species){
            the_list.push(this.collection[i])
        }
    }
    this.collection = the_list
}

Park.prototype.provide_object = function(){
    let object = {};
    for (let i = 0; i < this.collection.length; i++){
        if (this.collection[i].species in object){
            let the_name = this.collection[i].species;
            object[the_name] += 1;
        } else {
            let the_name = this.collection[i].species;
            object[the_name] = 1;
        }
    }
    return object
}
module.exports = Park;
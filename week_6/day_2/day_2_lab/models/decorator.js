const Decorator = function(){
    this.stock = []
}

Decorator.prototype.addCanToStock = function(paint){
    this.stock.push(paint)
}

Decorator.prototype.cal_stock = function(){
    let total = 0;
    for (let i = 0; i < this.stock.length; i++){
        total += this.stock[i].litres
    }
    return total
}

Decorator.prototype.check_if_enough_to_paint = function(room){
    if (this.cal_stock() >= room.area){
        return true
    }
    return false
}

Decorator.prototype.paint_room = function(room){
    let cans_left = []
    if (this.check_if_enough_to_paint){
        room.painted = true
    }
    for (let i = 0; i < this.stock.length; i++){
        if (room.area >= this.stock[i].litres){
            room.area -= this.stock[i].litres;
            this.stock[i].empty();
    } else {
        this.stock[i].litres -= room.area
        cans_left.push(this.stock[i])
        this.stock = cans_left
    }
}
}
module.exports = Decorator;
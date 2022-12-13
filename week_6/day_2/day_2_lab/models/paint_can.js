const Paint_can = function(number){
    this.litres = number
}

Paint_can.prototype.check_if_empty = function(){
    if (this.litres > 0){
        return false
    }
    return true
}

Paint_can.prototype.empty = function(){
    this.litres = 0
}


module.exports = Paint_can
const Cinema = function(films){
    this.films = films;
}

Cinema.prototype.getTitles = function(){
    const return_title = this.films.map((film) => film.title)
    return return_title
}

Cinema.prototype.findByTitle = function(title){
    const film = this.films.filter((film) => film.title === title);
    return film[0]
}

// Cinema.prototype.filterByGenre = function(genre){
//     return this.films.filter((film) => film.genre === genre);
// }

Cinema.prototype.checkYears = function(year){
    return this.films.some((film) => film.year === year);
}

Cinema.prototype.checkLength = function(length){
    return this.films.every((film) => film.length >= length);
}

Cinema.prototype.calAllTime = function(){
    const time = this.films.reduce((previous, current) =>{
        return previous + current.length
    }, 0)
    return time
}

Cinema.prototype.filterByProperty = function(property, value){
    return this.films.filter((film) => film[property] === value);
}

module.exports = Cinema;
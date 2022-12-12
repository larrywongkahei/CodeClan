var myArray = [];
var sports = ['football', 'tennis', 'rugby'];

// console.log(myArray);


// sports.push('snnoker');
// console.log(sports);
// var removedSport = sports.pop();

// sports.unshift('hockey');
// console.log(sports);

// var removed = sports.shift();
// console.log(removed);
// console.log(sports)

// var removedElements = sports.splice(1, 2);
// console.log(removedElements);
// console.log(sports);

// for (var currentSport of sports) {
//     var upperCaseSport = currentSport.toUpperCase();
//     console.log(upperCaseSport);
// }

for (var i = 0; i < sports.length; i+=2) {
    console.log('counter was : ', i, ' sport was ', sports[i])
}
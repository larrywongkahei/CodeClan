var movie = {
    title: "It's a wonderful life",
    year: 1946,
    language: 'Spanish'
};
// console.log('movie:', movie);
// console.log(movie.title)

movie.cast = ['James Stewart', 'Donna Reed'];
movie['subtitle-language'] = 'French';

console.log(movie)
var keyName = 'cast';
// console.log(movie[keyName])

delete movie[keyName];
console.log(movie)

movie.ratings = {
    critic: 94,
    audience: 95,
}
// console.log(movie.ratings.audience)

// for (var key in movie) {
//     console.log('key was: ', key, 'value was: ', movie[key]);
//     console.log(`key was: ${key} value was: ${movie[key]}`);
// };

var movieKeys = Object.keys(movie);
// console.log(movieKeys)

for (var movieKey of movieKeys) {
    console.log(`the value of the key is : ${movie[movieKey]}`)
}


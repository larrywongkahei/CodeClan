const arrayOfNums = [1, 2, 3, 4, 5, 6, 7, 8]
const getEvens = function(arrayOfNums) {
    return arrayOfNums.filter((number) => number % 2 === 0);
}

// console.log(getEvens(arrayOfNums))
const getOdds = function (arrayOfNums, even_fun){
    const evens = even_fun(arrayOfNums)
    return arrayOfNums.filter((number) => !(evens.includes(number)))
}

console.log(getOdds(arrayOfNums, getEvens))

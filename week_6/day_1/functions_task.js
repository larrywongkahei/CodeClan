// 1,
function return_sum_of_array (array) {
    var sum = 0;
    for (var item of array) {
        sum += item;
    }
    return sum;
}

// 2,
// function return_sum_of_array (array) {
//     var sum = 0;
//     for (var i = 0;i < array.length;i++) {
//         sum += array[i]
//     }
//     return sum;
// }

// 3,
// var return_sum_of_array = function (array) {
//     var sum = 0;
//     for (var item of array) {
//         sum += item;
//     }
//     return sum
// }

console.log(return_sum_of_array([1, 2, 3, 4]))

var check_if_string_is_key = function (object, string) {
    for (var key in object) {
        if (key === string) {
            return true
        } else {
            return false
        }
    }
}

// var check_if_string_is_key = function (object, string) {
//     if (string in object) {
//         return true
//     }
//     return false
// }
var object = {
    haha : 123,
    nono : 456
};

console.log(check_if_string_is_key(object, 'haha'))

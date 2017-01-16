function concat(arr1, arr2) {
    var array = []
    for (var i = 0; i < arr1.length; i++) {
        array.push(arr1[i]);
    }
    for (var i = 0; i < arr2.length; i++) {
        array.push(arr2[i]);
    }
}

var arr1 = ["a", "b"]
var arr2 = [1, 2]

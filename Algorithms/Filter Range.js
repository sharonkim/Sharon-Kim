function filterRange(arr, min, max) {
    var temp = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] <= min || arr[i] >= max) {
            arr[temp] = arr[i];
            temp++;
        }
    }
    console.log(temp);
    arr.length = temp;
}

var arr = [20, 5, 3, 17, 9, 1, 7, 12, 30]
filterRange(arr, 5, 17)

console.log(arr);

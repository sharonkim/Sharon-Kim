function reverseArr(arr){
    var length = (arr.length - 1)/2
    for(var idx = 0; idx < length; idx++){
        var hold = arr[arr.length - 1 - idx];
        arr[idx] = arr[end];
        arr[arr.length - 1 - idx] = hold;
        end--;
    }
return arr;
}

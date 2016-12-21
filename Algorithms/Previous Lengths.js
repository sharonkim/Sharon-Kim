["start", "middle", "end"]

function prevLength(arr){
    var temp = arr[arr[arr.length - 1].length]
    for(var i = arr.length - 1; i > 0; i--){
        arr[i] = arr[i - 1].length;
        arr[0] = temp;
    }

return arr;

}

function makeBig(arr){

    for(var i in arr){
        if(arr[i] > 0){
            arr[i] = "big";
        }
    }

return arr
}

var array = [-1, 3, 5, -4]

console.log(makeBig(array));

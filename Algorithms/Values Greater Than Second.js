var count = 0;
var arrNew = [];

function greaterThan2nd(arr){
        for(var idx = 2; idx < arr.length){
            console.log(arr[idx]);
            arrNew[arr.length] = arr[idx];
            count++
        return count;
}


or


var x = arr[1]
var count = 0;
var arrNew = [];

function greaterThan2nd(arr){
        for(var idx = 0; idx < arr.length; idx++){
            if(arr[idx] > x){
            console.log(arr[idx]);
            arrNew[arr.length] = arr[idx];
            count++
            }
        }
        return count;
}

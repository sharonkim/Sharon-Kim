function greaterThanY(arr, Y){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > Y){
            count++;
        }
    }
    console.log(count);
}

function countdown(num){

    var arr = [];
    for(; num >= 0; num--){
        arr.push(num);
    }
    return(arr);
    console.log("length = " + arr.length);
}

countdown()

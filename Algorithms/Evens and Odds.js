function eAndO(arr){
    var counterOdds = 0
    var counterEvens = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 0){
            counterEvens++;
        }
        else {
            counterEvens = 0;
        }
        if(arr[i] % 2 !== 0){
            counterOdds++;
        }
        else {
            counterOdds = 0
        }
        if(counterEvens = 3){
            console.log("That's odd");
            counterOdds = 0;
        }
        if(counterEvens === 3){
            console.log("Even more so");
            counterEvens = 0
        }
    }
}

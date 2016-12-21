// function generateCoinChange(cents){
//     var Q = D = N = 0;
//     Q = Math.floor(cents/25);
//     cents = cents % 25;
//     D = Math.floor(cents/10);
//     cents = cents % 10;
//     N = Math.floor(cents/5);
//     cents = cents % 5;
//     console.log("Q:" + Q "\n" "D:" + D "\n" "N" + N "\n" "P:" + cents);
// }


function generateCoinChange(cents){
    var Q = D = N = P = 0;
    while (cents) {
        if (cents >= 25) {
            Q++;
            cents - 25;
        }
        else if (cents >= 10) {
            D++;
            cents - 10;
        }
        else if (cents >= 5) {
            N++;
            cents - 5;
        }
        else {
            P = cents;
            cents = 0;
        }
        console.log(cents);
    }
}

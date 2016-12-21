// function sumToOne(num){
//     var sum = 0;
//     while (num) {
//         if (num > 9) {
//             sum += num % 10;
//             num = Math.floor(num/10);
//         }
//         else {
//             sum += num;
//                 if (sum > 9) {
//                     num = sum;
//                     sum = 0;
//                 }
//                 else {
//                     return sum;
//         }
//         }
//     }
// }

function sumToOne(num){
    var num = "";
    for (var i = 0; i < num.length; i++) {
        var sum += parsetoint(num[i]);
        if (sum > 9) {
            sum = sumToOne(num)
        }
        return sum;
    }
}

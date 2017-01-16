function reverseArr(arr){
//     var length = (arr.length - 1)/2
//     for(var idx = 0; idx < length; idx++){
//         var hold = arr[arr.length - 1 - idx];
//         arr[idx] = arr[end];
//         arr[arr.length - 1 - idx] = hold;
//         end--;
//     }
// return arr;
// }


//     for(var i = 0; i < arr.length/2; i++){
//         var temp = arr[arr.length - 1 - i];
//         arr[arr.length - 1 - i] = arr[i];
//         arr[i] = temp;
//     }
// }


    var right = arr.length - 1;
    for(var left = 0; left < Math.floor(arr.length/2); left++){
        var temp = arr[right];
        arr[right] = arr[left];
        arr[left] = temp;
        right--;
    }
}

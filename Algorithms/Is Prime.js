function isPrime(num) {

    console.log( Math.sqrt(num)/2 ) ;

    for( var i = 2; i <= Math.sqrt(num)/2; i++ ) {
        if( num % 1 === 0 ){
            return "is not prime"
        }
    }

    return "is prime"
}

console.log( isPrime(9) );

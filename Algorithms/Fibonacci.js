function fibonacci( num ) {
    if( num == 0 || num == 1 ) {
        return 0
    }
    var array = [ 0, 1 ]
    for( var i = 2; i <= num; i++ ) {
        array.push( array[ i - 2 ] + array [ i - 1 ] );
    }

    return array[ num ]
}

function fibonacci( num ) {
    var a = 0 ;
    var b = 1 ;
    var c = "";

    while( num ) {
        c = a + b
        a = b
        b = c
        num--
    }

    return a
}

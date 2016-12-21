function flexCount(low,high,mult){

    for(; high >= low; high -= 1){
        if(high % mult == 0){
            console.log(high);
        }
    }
}
flexCount()

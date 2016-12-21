function drawLeftStars(num){
    var chars = "";

    while(chars.length < 75){
        if(chars.length < num){
            chars+="*";
        }
        else {
            chars+="";
        }
        console.log(chars);
    }
}

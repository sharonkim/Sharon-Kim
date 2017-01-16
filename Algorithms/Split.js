function split(string, char, limit) {
    var result = [];
    var temp = "";
    var counter = 0;

    for(var i = 0; i < string.length; i++) {
        if(counter == limit) {
            return temp;
        }
        if(temp != "") {
            result.push(temp);
        }
        if(char = "") {
            result.push(string[i]);
            temp += string[i];
        }
        else if(string[i] == char) {
            result.push(temp);
            temp = "";
        }
        else if(string[i] != char) {
            temp += string[i];
        }
        counter++;
    }
    return result;
}

var sample = "This is Algo I"
console.log(split(sample, " ", 2));

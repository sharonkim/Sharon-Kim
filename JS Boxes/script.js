// console.log("got document")
// console.log(element);

var $ = function(param){
    var functions = {
        'ready': function(callback){
            document.addEventListener("DOMContentLoaded", function(){
                console.log("hitting this");
                callback();
            })
        },
        'click': function(callback) {
            document.getElementById(param).addEventListener("click", callback)
        },
        'changecolor': function(){
            document.getElementById(param).style.background = "green"
        }
    }
    return functions
}

//functions.ready(function(){})
$(document).ready(function(){
    console.log("Ready!");
    $('button').click($('blue-box').change-color)
})

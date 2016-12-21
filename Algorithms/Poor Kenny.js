function whatHappensToday(){
    var events = []

    if(chance(1100) <= 10){
        events.push("VOLCANO!");
    }
    if(chance(1100) <= 15){
        events.push("TSUNAMI!");
    }
    if(chance(1100) <= 20){
        events.push("EARTHQUAKE!")
    }
    if(chance(1100) <= 25){
        events.push("BLIZZARD!")
    }
    if(chance(1100) <= 30){
        events.push("METEOR!")
    }
    if(events.length === 0){
        return "Puppies and Rainbows";
    }
}

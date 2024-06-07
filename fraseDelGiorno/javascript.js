var frasi= [
    "Take a shower and shake it off",
    "What's good will come",
    "Pay attention",
    "Too much coffee",
    "Maybe tomorrow",
    "Go code",
    "So what about studying",
    "Cash Cash Cash"
]
function newQuote(){
    var randomNumber = Math.floor(Math.random()*(frasi.length));
    document.getElementById('quoteDisplay').innerHTML = frasi[randomNumber];
}
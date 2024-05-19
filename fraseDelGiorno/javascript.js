var frasi= [
    "Fatti una bella doccia",
    "Non lo fare",
    "Si puo fare vha",
    "Ciao dottore",
    "Facciamo domani",
    "Continua cosi",
    "Andra' sempre meglio",
    "Cash Cash Cash"
]
function newQuote(){
    var randomNumber = Math.floor(Math.random()*(frasi.length));
    document.getElementById('quoteDisplay').innerHTML = frasi[randomNumber];
}
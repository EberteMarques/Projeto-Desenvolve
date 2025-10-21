function chamaPrimeiro() {
    console.log('Chama essa Primeiro')
}

function ChamaDepois() {
    console.log('entrou na segunda função');
    chamaPrimeiro();
}

ChamaDepois();


function recebePrimeira(primeiraFuncao) {
    primeiraFuncao()
}

recebePrimeira(chamaPrimeiro);
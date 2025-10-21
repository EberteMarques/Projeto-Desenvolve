const fibonacci = [1,1,2,3,5,8,13,21,34,55];

function iteraSobreArrey() {
  for (let i = 0; i < fibonacci.length; i++) {
    console.log(i +1, 'o item é:', fibonacci[i]);
  }
}

iteraSobreArrey();

console.log('----------------------------------------------------------------------------')

function contaAte(numero) {
  for (let conta = 1; conta <= numero; conta++) {
    console.log('Mariana conta ', conta);
  }
}

contaAte(10);

console.log('----------------------------------------------------------------------------')

function verificarArray(listaDeNumeros){
    for (let indice of listaDeNumeros) {
        console.log(listaDeNumeros)
    }
}

verificarArray(fibonacci);

console.log('----------------------------------------------------------------------------')

function verificaItemPorIndice(listaDeNumeros){
    for (let indice in listaDeNumeros) {
        console.log(listaDeNumeros[indice] );
    }
}

verificaItemPorIndice(fibonacci);
console.log('----------------------------------------------------------------------------')

function contaPeloMenosUmAte(numeroLimite){
    let numero = 0;
    do {
        numero++;
        console.log(numero);
    } while (numero <= numeroLimite);
}

contaPeloMenosUmAte(1);
console.log('----------------------------------------------------------------------------')

function verificaSePodeAteNumeroLimite(numeroLimite){
    let numero = 0;
    while (numero <= numeroLimite) {
        console.log(numero);
        numero++;
    }
}   
verificaSePodeAteNumeroLimite(3);
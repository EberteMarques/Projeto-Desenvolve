const meusDados = {
    nome: 'Eberte',
    sobrenome: 'Marques',
    moraNoBrasil: true,
    idade: 47,
}
console.log(meusDados);

console.log(meusDados.nome)

console.log(meusDados['sobrenome'])

function retornaDadoPessoal(dadoPessoal){
    return meusDados[dadoPessoal];
}

console.log(retornaDadoPessoal('sobrenome'))
console.log(retornaDadoPessoal('moraNoBrasil'))
console.log(retornaDadoPessoal('idade'))


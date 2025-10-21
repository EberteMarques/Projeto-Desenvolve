const meusDados = {
    nome: 'Eberte',
    sobrenome: 'Marques',
    moraNoBrasil: true,
    idade: 47,
    pegaDocumento: () => {
        console.log('CPF: 123.456.789-00');
    }
};
 //verificando se o objeto possui determinado valor

function objetoPossuiValor(valorDaChave) {
    const valoresDoObjeto = Object.values(meusDados);
    return valoresDoObjeto.includes(valorDaChave);

}
console.log(objetoPossuiValor("Eberte") );
console.log(objetoPossuiValor(47) );
console.log(objetoPossuiValor("Marques") );
console.log(objetoPossuiValor(true) );
console.log('----------------------------------------------------------------------------')
console.log(objetoPossuiValor("maria") );
console.log(objetoPossuiValor(36) );
console.log(objetoPossuiValor("santos") );
console.log(objetoPossuiValor(false) );
console.log('----------------------------------------------------------------------------')
function objetoPossuiChave(nomeDaChave) {
    const chavesDoObjeto = Object.keys(meusDados);
    //console.log(chavesDoObjeto);
    return chavesDoObjeto.includes(nomeDaChave);
}
console.log(objetoPossuiChave("nome"));
console.log(objetoPossuiChave("idade"));
console.log(objetoPossuiChave("sobrenome"));
console.log(objetoPossuiChave("moraNoBrasil"));
console.log('----------------------------------------------------------------------------')

meusDados.pegaDocumento();

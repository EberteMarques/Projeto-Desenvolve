function eDeDiaOuDeNoite(hora){
    let periodo = ' ';
    if(hora <=18)
        periodo = 'É de dia';
    else
        periodo = 'É de noite';
    return periodo

}

console.log(eDeDiaOuDeNoite());
console.log(eDeDiaOuDeNoite(11));
console.log(eDeDiaOuDeNoite('dia'));
console.log(eDeDiaOuDeNoite(21));
console.log ('----------------------------------------------------------------------------')

function eMaiorDeIdade(idade) {
    if(idade<18)
        console.log('Menor de Idade');
    else
        console.log('Maior de Idade')
}

eMaiorDeIdade(18);
eMaiorDeIdade('2');

console.log ('----------------------------------------------------------------------------')

function periodoDoDia(hora){
    if(hora <12)
        console.log('Manha')
    else if (hora >=12 && hora <=18)
        console.log('Tarde')
    else
        console.log('Noite')
}
periodoDoDia(2);
periodoDoDia(14);
periodoDoDia(20);
periodoDoDia(-30);

console.log ('----------------------------------------------------------------------------')

function periodoComRegra(hora){
    if(hora >=0 && hora <=24)
        periodoDoDia(hora);
    else
        console.log('Você informou uma hora inexistente')
}
periodoComRegra(3);
periodoComRegra(17);
periodoComRegra(21);
periodoComRegra(-30);

console.log ('----------------------------------------------------------------------------')

function menuEscolha(opcaoDoMenu){
    switch(opcaoDoMenu){
        case 1:
            console.log('Você escolheu a primeira opção');
            break;
         case 2:
            console.log('Você escolheu a segunda opção');
            break;
            default:
                console.log('Você não escolheu uma das opções válidas!!')
        
    }
}

menuEscolha(1);
menuEscolha(2);
menuEscolha(90);

console.log ('----------------------------------------------------------------------------')

function MaiorDeIdadeSimples(idade){
    let condicaoDeIdade = idade >= 18 ? 'Maior de idade' : 'Menor de idade'
    return condicaoDeIdade

}
console.log(MaiorDeIdadeSimples(18));
console.log(MaiorDeIdadeSimples(3));

console.log ('----------------------------------------------------------------------------')

function maiorDeIdadeUnario(idade){

    return idade >= 18 && 'Maior de Idade'
}
console.log(maiorDeIdadeUnario(18));
console.log(maiorDeIdadeUnario(3));

console.log ('----------------------------------------------------------------------------')

function maiorDeIdadeCondicao(idade){

    return idade >= 18
}
console.log(maiorDeIdadeCondicao(18));
console.log(maiorDeIdadeCondicao(3));

console.log ('----------------------------------------------------------------------------')
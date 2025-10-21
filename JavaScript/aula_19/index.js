/*const verificaSeExisteElemento= (seletor) => {
    const elemento = document.querySelector(seletor);
    return !! elemento;
}
const  contaElementosSeletor = (seletor) => {
    if(verificaSeExisteElemento(seletor)){
        const todosOselementos = document.querySelectorAll(seletor);
        console.log(`Existem ${todosOselementos.length} elementos do seletor ${seletor}`);
    } else{
        console.log(`Não existem elementos do seletor ${seletor}`);
    }
}

contaElementosSeletor('li.menu-item');
contaElementosSeletor('li.menu-items');

const elementoEspecifico = document.querySelectorAll('li')[2];
console.log(elementoEspecifico);*/

const elemento = document.getElementsByTagName('ul');
console.log(elemento);

const elementoPorId = document.getElementById('titulo-principal');
console.log(elementoPorId.innerText);

const elementoPorClasse = document.getElementsByClassName('paragrafo');
console.log(elementoPorClasse[0].innerText);

const elementoPorNome = document.getElementsByName('meu-botao');
console.log(elementoPorNome[0].innerText);

const verificaSeExisteTag=(elemento) =>document.getElementsByTagName(elemento).length > 0;

const verificaSeExisteId=(elemento) =>!!document.getElementById(elemento);

const verificaSeExisteClasse=(elemento) =>document.getElementsByClassName(elemento).length > 0;

const verificaSeExisteNome=(elemento) =>document.getElementsByName(elemento).length > 0;

console.log(verificaSeExisteTag('main'));   
console.log(verificaSeExisteId('meu-botao'));
console.log(verificaSeExisteClasse('paragrafo'));
console.log(verificaSeExisteNome('meu-botao'));

const listaDeElementos = ['header', 'ul', 'meu-botao', 'titulo-principal', 'elemento_que_não_existe'];
const descobreTipoDeElemento = (lista) => {
           if(listaDeElementos.length=== 0){
                console.log('Você não passou uma lista de elementos');
           }else{
            for(let nome of lista){
                if(verificaSeExisteTag(nome)){
                    console.log(`${nome} é uma tag`);
                } else if(verificaSeExisteId(nome)){
                    console.log(`${nome} é um id`);
                } else if(verificaSeExisteClasse(nome)){
                    console.log(`${nome} é uma classe`);
                } else if(verificaSeExisteNome(nome)){
                    console.log(`${nome} é um nome`);
                } else{
                    console.log(`O elemento ${nome} não foi encontrado no DOM`);
                }
            }
         }
    }
descobreTipoDeElemento(listaDeElementos);

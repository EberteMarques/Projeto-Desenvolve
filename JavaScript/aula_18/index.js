const verificaSeExisteElemento= (seletor) => {
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
console.log(elementoEspecifico);
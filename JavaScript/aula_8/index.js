const todoMundoVe = ' Todo Mundo Vê Essa Variável De Escopo Global'
function executaEscopoGlobal() {
    console.log(todoMundoVe);
}

function executaEscopoLocal (){
    const visivelEmEscopoLocal = 'Só quem esta dentro do bloco da função vê essa variavel de escopo local'
    console.log(visivelEmEscopoLocal)

    function chamaDentroDoEscopo () {
        console.log('dentro do escopo =>', visivelEmEscopoLocal)
        const dentroLocal = false;
        console.log(dentroLocal)

    }
    chamaDentroDoEscopo()
}

executaEscopoGlobal();


executaEscopoLocal();

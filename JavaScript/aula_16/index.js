function chamar(segundosDeAtraso){
    console.log(`atrasou ${segundosDeAtraso} segundos`)
}
function chamaAtrasado(funcaoDeAtraso, quantidadeDeAtraso) {
    setTimeout(() => funcaoDeAtraso(quantidadeDeAtraso), quantidadeDeAtraso * 1000)
    }
    chamaAtrasado(chamar, 1)
    function chamaComIntervalo(funcaoDeIntervalo, intervalo) {
        setInterval(() => funcaoDeIntervalo(intervalo), intervalo * 1000)
    }
    chamaComIntervalo(chamar, 2)
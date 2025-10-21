const cores = ['preto', 'branco']
/*console.log(cores)
console.log(cores [0])
console.log(cores[1])
console.log('Quantidade de elementos',cores.length)

console.log(cores.lastIndexOf('branco'))
console.log(cores.lastIndexOf('preto'))

console.log(cores.lastIndexOf('vermelho')) //toda vez que o usuário faz a chamada de um item inexistente o sistema retorna '-1'*/

cores.push('vermelho')
console.log(cores)
console.log(cores.length)
console.log(cores.lastIndexOf('vermelho'))
console.log(cores.lastIndexOf('azul'))
console.log('----------------------------------------------------------------------------')
cores.push('azul')
console.log(cores)
console.log(cores.length)

console.log('----------------------------------------------------------------------------')
cores.shift()
console.log(cores)

console.log('----------------------------------------------------------------------------')
cores.unshift('preto')
console.log(cores)
cores.pop()
console.log(cores)

console.log('----------------------------------------------------------------------------')

function removeCor(nomedaCor){
    const posicaoDaCor = cores.indexOf(nomedaCor)
    if (posicaoDaCor >= 0) {
        cores.splice(posicaoDaCor, 1)
    }
    console.log(cores)

}
 removeCor('branco')
 removeCor('vermelho')
removeCor('vermelho')
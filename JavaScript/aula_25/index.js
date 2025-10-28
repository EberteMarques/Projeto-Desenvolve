/*const botao = document.getElementById('meu-botao');
const inputText = document.getElementById('texto');
const titulo = document.createElement('h1')

botao.addEventListener('click', () => {
    const nomeSalvo = JSON.stringify(titulo.innerText)
    localStorage.setItem('dadosUsuario', nomeSalvo)
    document.body.appendChild(titulo)
})

inputText.addEventListener('keyup', (e) => {
     
    titulo.innerText = e.target.value
})

addEventListener('load', () => {
    const meuNome = JSON.parse(localStorage.getItem('dadosUsuario'))
    if (meuNome){
        titulo.innerText = `Olá ${meuNome}, seja bem vindo!!`
        
    }else{
        titulo.innerText='Olá Usuário!'
    }
    document.body.appendChild(titulo)
})*/

const frutas = ['Maçã', 'Laranja', 'Melancia']
for (let fruta in frutas){
    localStorage.setItem(`Fruta ${fruta}`, frutas[fruta])
} 
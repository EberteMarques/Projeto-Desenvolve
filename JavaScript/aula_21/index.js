const botao = document.getElementById('meu-botao')
const inputText = document.getElementById('texto')
const alertaOla = () => alert('Olá estudante!')
botao.addEventListener('click', () => {
    const titulo = document.getElementById('titulo-principal')
    titulo.innerText = 'Mudou apos o clique'
})

inputText.addEventListener('keypress', (e) => {
    const titulo = document.getElementsByTagName('h1')[0]
    titulo.innerText = e.target.value
})
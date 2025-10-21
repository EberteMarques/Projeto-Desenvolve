const selecionaTag  = (elemento) => document.getElementsByTagName(elemento)
const selecionaId = (elemento) => document.getElementById(elemento)
const selecionaClasse = (elemento) => document.getElementsByClassName(elemento) 
const selecionaNome = (elemento) => document.getElementsByName(elemento).length



const tituloH1 = selecionaTag('h1')
tituloH1[0].innerText = "Mudou título"
console.log (tituloH1[0].classList)

const atrasaMudancaDeCor = () =>
    setTimeout (() => {
        const listaClasses = tituloH1[0].classList.value
        tituloH1[0].classList = listaClasses + ' alterado-cor-bg '
        console.log(tituloH1[0].classList)
    },3000);


atrasaMudancaDeCor()



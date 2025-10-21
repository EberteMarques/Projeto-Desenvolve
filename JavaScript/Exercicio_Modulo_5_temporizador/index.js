function calcularTempoRestante(dataFutura) {
  const agora = new Date();
  const diferenca = dataFutura - agora;

  if (diferenca <= 0) {
    return null; // Tempo esgotado
  }

  const segundos = Math.floor((diferenca / 1000) % 60);
  const minutos = Math.floor((diferenca / 1000 / 60) % 60);
  const horas = Math.floor((diferenca / (1000 * 60 * 60)) % 24);
  const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));

  return { dias, horas, minutos, segundos };
}
function atualizarTemporizador() {
  const tempo = calcularTempoRestante(dataFutura);

  if (!tempo) {
    document.getElementById("temporizador").textContent = "Tempo esgotado!";
    clearInterval(intervalo);
    return; 
  }

  document.getElementById("temporizador").textContent =
    `${tempo.dias}d ${tempo.horas}h ${tempo.minutos}m ${tempo.segundos}s`;
}
const dataFutura = new Date("2025-12-31T23:59:59"); // Altere para a data desejada
const intervalo = setInterval(atualizarTemporizador, 1000);

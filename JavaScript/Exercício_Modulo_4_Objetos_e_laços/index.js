// 1 - Array de objetos para armazenar os livros
let estoque = [];

// 2 - Funções para gerenciar o estoque

function adicionarLivro(titulo, autor, quantidade) {
  // Verifica se o livro já existe
  const livroExistente = estoque.find(livro => livro.titulo === titulo);
  if (livroExistente) {
    console.log(`O livro "${titulo}" já está no estoque.`);
  } else {
    estoque.push({ titulo, autor, quantidade });
    console.log(`Livro "${titulo}" adicionado com sucesso.`);
  }
}

function removerLivro(titulo) {
  const indice = estoque.findIndex(livro => livro.titulo === titulo);
  if (indice !== -1) {
    const removido = estoque.splice(indice, 1);
    console.log(`Livro "${removido[0].titulo}" removido do estoque.`);
  } else {
    console.log(`Livro "${titulo}" não encontrado no estoque.`);
  }
}

function atualizarQuantidade(titulo, novaQuantidade) {
  const livro = estoque.find(livro => livro.titulo === titulo);
  if (livro) {
    livro.quantidade = novaQuantidade;
    console.log(`Quantidade do livro "${titulo}" atualizada para ${novaQuantidade}.`);
  } else {
    console.log(`Livro "${titulo}" não encontrado no estoque.`);
  }
}

function listarLivros() {
  if (estoque.length === 0) {
    console.log("O estoque está vazio.");
  } else {
    console.log("Livros disponíveis no estoque:");
    for (const livro of estoque) {
      console.log(`- ${livro.titulo} | Autor: ${livro.autor} | Quantidade: ${livro.quantidade}`);
    }
  }
}
adicionarLivro("Dom Casmurro", "Machado de Assis", 5);
adicionarLivro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 3);
listarLivros();
atualizarQuantidade("Dom Casmurro", 10);
removerLivro("O Pequeno Príncipe");
listarLivros();
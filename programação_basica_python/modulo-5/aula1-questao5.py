emojis_disponiveis = {
    ":sorriso:": "😊",
    ":coracao:": "❤️",
    ":polegar_para_cima:": "👍",
    ":estrela:": "⭐",
    ":sol:": "☀️",
    ":lua:": "🌙",
    ":flor:": "🌸",
    ":cafe:": "☕",
    ":pizza:": "🍕",
    ":carro:": "🚗",
    ":aviao:": "✈️",
    ":casa:": "🏠",
    ":aperto_de_maos:": "🤝",
    ":fogo:": "🔥",
    ":agua:": "💧",
    ":piscando:": "😉",
    ":chorando:": "😢",
    ":raiva:": "😡",
    ":pensando:": "🤔",
    ":medo:": "😨",
    ":dinheiro:": "💰",
    ":presente:": "🎁",
    ":livro:": "📚",
    ":computador:": "💻",
    ":telefone:": "📞",
    ":musica:": "🎶",
    ":ok:": "👌",
    ":bandeira_br:": "🇧🇷"
}

print("Bem-vindo ao Emojizador de Frases!")
print("---")

print("Aqui está a lista de emojis disponíveis e seus códigos:")
for codigo, emoji in emojis_disponiveis.items():
    print(f"{codigo} : {emoji}")
print("---")

frase_codificada = input("\nDigite sua frase usando os códigos (ex: Oi :sorriso:): ")
frase_decodificada = frase_codificada
for codigo, emoji in emojis_disponiveis.items():
    frase_decodificada = frase_decodificada.replace(codigo, emoji)

print("\nSua frase emojizada:")
print(frase_decodificada)
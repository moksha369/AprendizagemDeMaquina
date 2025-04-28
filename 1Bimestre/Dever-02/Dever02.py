def contar_vogais_consoantes(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vogais = sum(1 for letra in frase if letra in vogais)
    num_consoantes = sum(1 for letra in frase if letra in consoantes)
    return num_vogais, num_consoantes

def maior_palavra(frase):
    palavras = frase.split()
    if palavras:
        return max(palavras, key=len)
    return ""


def exibir_informacoes(frase_atual):
    palavras = frase_atual.split()
    vogais, consoantes = contar_vogais_consoantes(frase_atual)
    maior_palavra_encontrada = maior_palavra(frase_atual)

# inverter a frase por meio dos caracteres
    frase_invertida = frase_atual[::-1]

# inverte a frase por meio das palavras 
    frase_palavras_invertida = " ".join(palavras[::-1])  

# cria uma tupla de palavras
    palavras_tupla = tuple(palavras)

    print("\n🔹 Frase atualizada:", frase_atual)
    print("🔹 Maiúsculas:", frase_atual.upper())
    print("🔹 Minúsculas:", frase_atual.lower())
    print(f"🔹 Número de palavras: {len(palavras)}")
    print(f"🔹 Número de caracteres (com espaços): {len(frase_atual)}")
    print(f"🔹 Número de caracteres (sem espaços): {len(frase_atual.replace(' ', ''))}")
    
    print(f"🔹 Número de vogais: {vogais}")
    print(f"🔹 Número de consoantes: {consoantes}")
    print(f"🔹 Maior palavra: {maior_palavra_encontrada} ({len(maior_palavra_encontrada)} caracteres)")
    print(f"🔹 Frase invertida: {frase_invertida}")
    print(f"🔹 Frase com palavras invertidas: {frase_palavras_invertida}")
    print(f"🔹 Tupla de palavras: {palavras_tupla}")  

# solicita uma frase ao usuário com verificação
while True:
    frase = input("Digite uma frase: ").strip()
    if frase:
        break
    print("⚠️ Erro: Você precisa digitar uma frase!")

# exibe as informações iniciais
exibir_informacoes(frase)


# substituição de palavra e nova contagem
while True:
    palavra_antiga = input("\nDigite uma palavra para substituir: ").strip()
    if palavra_antiga in frase:
        palavra_nova = input("Digite a nova palavra: ").strip()
        frase = frase.replace(palavra_antiga, palavra_nova)  # Atualiza a frase

        # Exibe as novas informações da frase alterada
        exibir_informacoes(frase)
        
        break
    else:
        print("⚠️ Erro: A palavra digitada não está na frase. Tente novamente!")
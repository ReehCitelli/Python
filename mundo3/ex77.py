palavras = ("python", "programacao", "desenvolvimento", "linguagem", 
            "computador", "tecnologia", "software", "hardware", "internet", "rede")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
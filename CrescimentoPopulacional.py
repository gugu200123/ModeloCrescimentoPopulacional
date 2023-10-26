# Entradas do usuário
populacao_inicial = int(input("População inicial: "))
taxa_de_crescimento = float(input("Taxa de crescimento (em decimal): "))
t = int(input("Número de períodos de tempo: "))

# Inicialização de variáveis
contador = 0

# Loop while para simular o crescimento populacional
while contador < t:
    populacao_nova = populacao_inicial * (1 + taxa_de_crescimento)
    print(f"População no período {contador + 1}: {int(populacao_nova)}")
    populacao_inicial = populacao_nova
    contador += 1
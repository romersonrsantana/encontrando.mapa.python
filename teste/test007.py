N = int(input('\nInforme o número de testes que gostaria de realizar: --> '))
i = 0

while i < N:

   valor_entrada_usuario = input('Informe dois valores, separando cada um por espaço: --> ').split()

   a = valor_entrada_usuario[0]

   b = valor_entrada_usuario[1]

   if len(b) > len(a):

       print("nao encaixa")

   elif a.endswith(b):

       print("encaixa")

   else:

       print("nao encaixa")

   i += 1

"""N = int(input())": Lê um número inteiro "N" da entrada padrão. Este valor representa o número de casos de teste que serão executados.
"i = 0": Inicializa a variável "i" com o valor 0. Ela será usada para controlar o número de casos de teste já processados.
"while i < N:": Inicia um loop "while" que continua executando enquanto o valor de "i" for menor que "N". Isso significa que o bloco de código dentro do loop será repetido "N" vezes, uma vez para cada caso de teste.
"v = input().split()": Lê uma linha da entrada padrão e a divide em uma lista de strings usando o método "split()". Aqui, espera-se que o usuário insira dois valores separados por espaço.
"a = v[0]" e "b = v[1]": Atribuem os valores lidos às variáveis "a" e "b". Esses valores correspondem aos dois números que serão comparados para verificar se "encaixam".
"if len(b) > len(a):": Verifica se o comprimento de "b" é maior que o comprimento de "a". Se isso for verdadeiro, significa que "b" não pode encaixar em "a", e então imprime "nao encaixa".
"elif a.endswith(b):": Se o bloco anterior não for executado, então verifica se o número "a" termina com o número "b". Se for o caso, isso significa que "b" encaixa em "a".
"print("encaixa")": Se a condição acima for verdadeira, imprime "encaixa".
"else:": Se nenhuma das condições acima for atendida, isso significa que "b" não encaixa em "a", então imprime "nao encaixa".
"i += 1": Incrementa o valor de "i" para que o loop avance para o próximo caso de teste.
Resumindo, o código lê um número "N" de casos de teste. Para cada caso, lê dois valores "a" e "b" e verifica se "b" pode encaixar em "a" seguindo as condições especificadas. O resultado é impresso na saída padrão. O loop é repetido "N" vezes para processar todos os casos de teste."""
      

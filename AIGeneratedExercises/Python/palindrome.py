entrada = input("Informe a palavra: ")
checker = list(entrada)

validation = [ ]

for letter in range(len(checker) -1, -1, -1):
   validation.append(checker[letter])

if validation == checker:
   print(f"A palavra informada é um palíndromo!\n{''.join(checker)} = {''.join(validation)}!")

else:
   print("A palavra digitada não é um palíndromo.")

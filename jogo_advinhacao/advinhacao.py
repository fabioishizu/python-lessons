print('**********************************************************')
print('*				Jogo	da	adivinhação					*')
print('**********************************************************')

chute = int(input("Chute um número: "))
print("Você digitou: ", chute)

num_secreto = 42;
maior = (chute > num_secreto)
menor = (chute < num_secreto)
acertou = (num_secreto == chute)

if(acertou):
    print("ACERTOU!")
elif(maior):
    print("Você errou, o número que escolheu é maior que o número secreto.")
elif(menor):
    print("Você errou, o número que escolheu é menor que o número secreto.")


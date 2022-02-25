'''
Sistema de PDV v1 - gera um arquivo chamado
transactions.txt para registrar as vendas
dos produtos

formatação anterior -> 
file.write("%16s%07d%s\n" % (price * 100, credit_card,  description))
'''


from transactions import *

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose a option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])

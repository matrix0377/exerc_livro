""" 
Programa da TVN codificando
"""
# importar o módulo
import pygame.mixer

# a função "wait_finish()" faz um laço até o método "get_busy()"
# do canal retornar False


def wait_finish(channel):
    while channel.get_busy():
        pass


# cria um objeto mixer e inicializa o sistema de som de pygame
sounds = pygame.mixer
sounds.init()

# carrega cada som requerido em sua própria variável
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

# é o que você pergunta a cada vez
prompt = "Press 1 for Correct, 2 for Wrong or 0 to Quit: "

# iniciando valores
number_asked = 0
number_correct = 0
number_wrong = 0

# solicite ao apresentador
choice = input(prompt)


while choice != "0":
    # Se a resposta for correta, aumente os contadores e então
    # reproduza o devido som.
    if choice == "1":
        number_asked = number_asked + 1
        number_correct = number_correct + 1
        wait_finish(correct_s.play())

    # Se a resposta for incorreta, aumente os contadores e então
    # reproduza o efeito sonoro
    if choice == "2":
        number_asked = number_asked + 1
        number_wrong = number_wrong + 1
        wait_finish(wrong_s.play())
    choice = input(prompt)

print("==" * 25)
print("You asked " + str(number_asked) + " questions.")
print("  -->>>> " + str(number_correct) + " were correctly answered.")
print("  -->>>> " + str(number_wrong) + " were answered incorrectly.")
print("-=*" * 25)

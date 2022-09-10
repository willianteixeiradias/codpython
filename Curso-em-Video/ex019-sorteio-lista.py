import random

aluno1 = str (input( 'rimero aluno: '))
aluno2 = str (input('Segundo Aluno:'))
aluno3 = str (input('terceiro aluno:'))
aluno4 = str (input('quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('o aluno escolhi foi {}'.format(escolhido))

"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

num = int(input('Digite um numero entre 0 e 20: '))
while num not in range(0, 21):
    print('Numero Inválido')
    num = int(input('Digite um numero entre 0 e 20: '))
print(f'O número {num} escrito em extenso é {extenso[num]}')

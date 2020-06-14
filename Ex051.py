"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
décimo = a1 + (10-1) * r
for c in range(a1, décimo+r, r):
    print(c)

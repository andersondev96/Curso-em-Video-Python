# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

medida = float(input('Digite uma distancia em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {} corresponde a '
      '\n{:.2f}km'
      '\n{:.2f}hm'
      '\n{:.2f}dam'
      '\n{:.2f}dm'
      '\n{:.2f}cm'
      '\n{:.2f}mm'
      .format(medida,km,hm,dam,dm,cm,mm))

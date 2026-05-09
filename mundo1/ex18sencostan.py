from math import radians,sin,cos,tan

angulo =  float(input('Digite o angulo: '))

seno = sin(radians(angulo))
print('O seno é {:.2f}'.format(seno)) 

cosseno = cos(radians(angulo))
print('O cosseno é {:.2f}'.format(cosseno)) 

tangente = tan(radians(angulo))
print('O tangente é {:.2f}'.format(tangente)) 

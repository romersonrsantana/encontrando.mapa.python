nota1 = float(input('\n\n Digite sua nota da primeira etapa: '))
nota2 = float(input('Digite sua nota da segunda etapa '))
media = (nota1 + nota2)/2

print('\n As notas digitadas foram:\n {:-> 16} \n e \n {:-> 16} \n respectivamente. \n\n A média entre elas será de {} pontos\n\n' .format( nota1, nota2, media))
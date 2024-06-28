import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'É certo'
    elif answer_number == 2:
        return 'É decididamente assim'
    elif answer_number == 3:
        return 'Sim'
    elif answer_number == 4:
        return 'Responder, nebuloso, tentar novamente'
    elif answer_number == 5:
        return 'Perguntar novamente mais tarde'
    elif answer_number == 6:
        return 'Concentre-se e pergunte novamente'
    elif answer_number == 7:
        return 'Minha resposta é não'
    elif answer_number == 8:
        return 'A perspectiva não é tão boa'
    elif answer_number == 9:
        return 'Muito duvidoso'

r = random.randint(1, 9)
fortune = get_answer(r)
print('\n',fortune,'\n')
print('O número pelo computador foi {}\n'.format(r))
from random import randint


def krug1(firstname):
    fil = [


        f'Вау , {firstname}\nЭто очень круто🤤\n',
        f'{firstname}, Я официально заявляю, что это лучший круг, который у меня получался🤤\n',
        f'{firstname}, надеюсь ты так же рад как и я❤️\n',
        f'Мы смогли придумать что-то крутое!\n{firstname}, уверен тебе нравится😍\n'
    ]

    dis = "@CCircle_bot создает кастомизированные круги, но не под глазами😏\n\nПоделись со своими друзьями @CCircle_bot"

    i = randint(0, 3)

    full = (str(fil[i]) + "\n" + dis)
    return full

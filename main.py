import pyautogui
from time import sleep


# game resolution must be 1024 x 720
# image max resolution 40 x 30


def get_monitor_size():
    screenwidth, screenheight = pyautogui.size()
    return screenwidth, screenheight


def load_images(file, gray=True):
    buttons = pyautogui.locateOnScreen(file, confidence=.90, grayscale=gray)
    return buttons


def click_on_image(coordinates):
    pyautogui.moveTo(coordinates)
    pyautogui.click()


def times_10(image):
    click_on_image(image)
    sleep(0.15)
    plus = load_images('images/relative_buttons/plus.png', False)
    for i in range(1, 10):
        click_on_image(plus)
        sleep(0.1)


def check_ticket(ticket):
    if ticket == "nada":
        return
    elif ticket in ["comprar", "pegar_da_giftbox"]:
        if ticket == "comprar":
            buy = load_images('images/relative_buttons/buy_ticket.png')
            if buy is not None:
                buy = load_images('images/relative_buttons/force_start.png')
                click_on_image(buy)

        elif ticket == "pegar_da_giftbox":
            ticket_out = load_images('images/relative_buttons/buy_ticket.png')
            if ticket_out is not None:
                i = 0
                sequence = ["images/relative_buttons/cancel.png", "images/relative_buttons/menu.png",
                            "images/relative_buttons/giftbox.png", "images/relative_buttons/gift_ticket.png",
                            "images/relative_buttons/collect.png", 'images/relative_buttons/ok.png',
                            "images/relative_buttons/warn_close.png", "images/relative_buttons/gift_close.png"]
                while i < len(sequence):
                    if load_images(sequence[i]) is not None:
                        click = load_images(sequence[i])
                        click_on_image(click)
                        i += 1
                        sleep(0.2)


def macro(image_list: list, times=0, is_chronicle=False, ticket=str()):
    search = True
    counter = 0
    cycles = 0
    quest = 1
    while search:
        sleep(0.1)
        check_ticket(ticket)
        tickets = load_images('images/relative_buttons/tickets.png')

        if tickets is not None:
            times_10(tickets)

        auto = load_images('images/relative_buttons/auto.png')

        if auto is not None:
            sleep(0.1)
            click_on_image(auto)

        buttons = [load_images(image_list[i]) for i in range(len(image_list))]
        if counter <= len(buttons) - 1:
            if buttons[counter] is not None:
                click_on_image(buttons[counter])
                sleep(0.1)
                if load_images('images/point_event/close_reward.png') is not None:
                    click_on_image(load_images('images/point_event/close_reward.png'))
                counter += 1

        if counter > len(buttons) - 1:
            print('first')
            if cycles == times and is_chronicle is False:
                search = False
            elif cycles == times - 1:
                print('second')
                if quest == 3:
                    print('fourth')
                    search = False
                else:
                    print('third')
                    image_list[0] = image_list[0].replace(str(quest), str(quest + 1))
                    print(image_list[0])
                    back = load_images("images/chronicle/back.png", True)
                    if back is not None:
                        sleep(0.1)
                        click_on_image(back)
                        quest += 1
                        cycles = 0
                        counter = 0
            else:
                cycles += 1
                counter = 0


def init(macro_, ticket_, vezes_):
    macros = {'friend_coin': ['images/kon_coin/10x_times.png', 'images/kon_coin/ok.png', 'images/kon_coin/close.png'],
              'evento_de_pontos': ['images/point_event/start.png', 'images/point_event/continue.png',
                                   'images/point_event/result.png',
                                   'images/point_event/continue.png', 'images/point_event/close.png',
                                   'images/point_event/retry.png'],
              'chronicle_quest': ['images/chronicle/quest1.png', 'images/chronicle/normal.png',
                                  'images/chronicle/character.png',
                                  'images/chronicle/ok.png', 'images/chronicle/start.png',
                                  'images/chronicle/continue.png',
                                  'images/chronicle/result.png', 'images/chronicle/retry.png']}
    macro(macros[macro_], vezes_, macro_ == "chronicle_quest", ticket_)


def question(lista):
    c = 1
    for i in lista:
        print(f'{c}: {i}')
        c += 1
    return int(input(''))-1


macros = ['friend_coin', 'evento_de_pontos', 'chronicle_quest']
tickets = ['pegar_da_giftbox', 'comprar', 'nada']
respostas = []

try:
    respostas.append(question(macros))
    respostas.append(question(tickets))
except ValueError:
    print('precisam ser numeros inteiros')

vezes = int(input('quantas vezes de 10x voce quer jogar:'))

try:
    init(macros[respostas[0]], tickets[respostas[1]], vezes)
except IndexError:
    print('voce tem que escolher um dos numeros que estão nas opções')
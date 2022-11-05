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


def macro(image_list: list, times=0, is_chronicle=False):
    """
    type image_list: list
    type times: int
    """
    search = True
    counter = 0
    cycles = 0
    quest = 1
    while search:
        sleep(0.1)

        tickets = load_images('images/relative_buttons/tickets.png')
        buy = load_images('images/relative_buttons/buy_ticket.png')

        if buy is not None:
            buy = load_images('images/relative_buttons/force_start.png')
            click_on_image(buy)

        if tickets is not None:
            times_10(tickets)

        auto = load_images('images/relative_buttons/auto.png')

        if auto is not None:
            sleep(0.1)
            click_on_image(auto)

        buttons = [load_images(image_list[i]) for i in range(len(image_list))]
        if counter <= len(buttons)-1:
            if buttons[counter] is not None:
                click_on_image(buttons[counter])
                counter += 1

        if counter > len(buttons) - 1:
            print('first')
            if cycles == times and is_chronicle is False:
                search = False
            elif cycles == times-1:
                print('second')
                if quest == 3:
                    print('fourth')
                    search = False
                else:
                    print('third')
                    image_list[0] = image_list[0].replace(str(quest), str(quest+1))
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


kon_coin = ['images/kon_coin/10x_times.png', 'images/kon_coin/ok.png', 'images/kon_coin/close.png']

point_event = ['images/point_event/start.png', 'images/point_event/continue.png', 'images/point_event/result.png',
               'images/point_event/continue.png', 'images/point_event/close.png', 'images/point_event/retry.png']

chronicle_quest = ['images/chronicle/quest1.png', 'images/chronicle/normal.png', 'images/chronicle/character.png',
                   'images/chronicle/ok.png', 'images/chronicle/start.png', 'images/chronicle/continue.png',
                   'images/chronicle/result.png', 'images/chronicle/retry.png']

import pyautogui
from time import sleep


# image max resolution 40 x 30


def get_monitor_size():
    screenWidth, screenHeight = pyautogui.size()
    return screenWidth, screenHeight


def load_images(file):
    buttons = pyautogui.locateOnScreen(file, confidence=.90)
    return buttons


def click_on_image(coordinates):
    pyautogui.moveTo(coordinates)
    pyautogui.click()
    sleep(1)


# spend the kon's coins
def kon_coin(times=0):
    """
    :type times: int
    """
    search = True
    counter = 0
    cycles = 0
    image_list = ['images/kon_coin/10x_times.png', 'images/kon_coin/ok.png', 'images/kon_coin/close.png']
    while search:
        sleep(0.3)
        buttons = [load_images(image_list[i]) for i in range(len(image_list))]

        if buttons[counter] is not None:
            click_on_image(buttons[counter])
            counter += 1

        if counter > len(buttons) - 1:
            counter = 0
            cycles += 1
            if cycles == times:
                search = False




from PIL import Image
import numpy as np
from datetime import datetime
import os


def list_to_input_img(array, username=None):
    """Функция отрисовки узора на машинном коде вязальной машины
    Принимает на вход двумерный список(массив) и имя юзера,
    писок отрисовывается попиксельнов цикле c помощью библиотеки
    PIL. Юзернейм используется для формирования названия файла.
    После работы функция возвращает адрес картинки.
    """

    # список условных обозначений, порядок важен, так как берём индекс значения
    color_list = ["K", "P", "T", "M", "FR1", "FR2", "FL1", "FL2", "BR1", "BR2",
                  "BL1", "BL2", "XRp", "XRm", "XLp", "XLm", "BL", "S"]

    # палитра используемых цветов в картинкеЗ, порядок важен
    pallete = np.array(
        [(255, 0, 16),  # red 'K'
         (43, 206, 72),  # green 'P'
         (255, 255, 128),  # pale yellow 'T'
         (94, 241, 242),  # turquoise 'M'
         (0, 129, 69),  # bright green 'FR1'
         (0, 92, 49),  # green 'FR2'
         (255, 0, 190),  # bright pink 'FL1'
         (194, 0, 136),  # pink 'FL2'
         (126, 0, 149),  # bright purple 'BR1'
         (96, 0, 112),  # purple 'BR2'
         (179, 179, 179),  # brght grey 'BL1'
         (128, 128, 128),  # grey 'BL2'
         (255, 230, 6),  # yellow 'XRp'
         (255, 164, 4),  # orange 'XRm'
         (0, 164, 255),  # bright blue 'XLp'
         (0, 117, 220),  # blue 'XLm'
         (117, 59, 59)], dtype=np.uint8
    )
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(dir_path + '/images/66.png')
    height = len(array)
    width = len(array[0])
    new_size = (width, height)
    image = image.resize(new_size)
    a, b = image.size
    print(a, b)
    image.putpalette(pallete)

    for x, row in enumerate(array):
        for y, value in enumerate(row):
            if value not in color_list:
                ValueError(f'{value} Value not in dict')
            image.putpixel((y, x), color_list.index(value))

    directory = (
        dir_path  + '/images/'
        f'{username}-{datetime.now().strftime("%y:%m:%d-%H:%M:%S")}.png'
    )
    image.save(directory)
    return directory, width, height

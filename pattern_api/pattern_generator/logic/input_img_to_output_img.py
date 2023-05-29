import os
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'{end_time - start_time} SECOOOONDS')
        print(f'{end_time - start_time} SECOOOONDS')
        print(f'{end_time - start_time} SECOOOONDS')
        print(f'{end_time - start_time} SECOOOONDS')
    return wrapper

DIR_RENDER_PY = os.path.realpath(__file__)
levels_up = 4
for _ in range(levels_up):
    DIR_RENDER_PY = os.path.dirname(DIR_RENDER_PY)
DIR_RENDER_PY += '/neural_inverse_knitting/render.py'
print(DIR_RENDER_PY)

# @timer_decorator
def input_img_output_img(width, height, directory):
    """
    Функция, получающая на вход путь до картинки с машинным(вязальным) кодом,
    преобразует эту картинку в визуализацию вязанноого(настоящего) узора.
    Для запуска преобразования используется нейросеть, которая вызывается
    из DIR_RENDER_PY.
    """
    output_dir = os.path.dirname(os.path.realpath(__file__)) + '/images/'
    command = (f'CUDA_VISIBLE_DEVICES="-1" python3 '
               f'{DIR_RENDER_PY} --width {width} --height {height} '
               f'--output_dir={output_dir} {directory}')
    print(command)
    os.system(command)
    return output_dir

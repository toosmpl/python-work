import time
from datetime import datetime
from threading import Thread
import multiprocessing
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf-8') as file:
        data = file.readline()
        while data:
            all_data.append(data)
            data = file.readline()


file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
filenames = [rf'C:\Users\user\Desktop\python\DeZe\file{number}.txt' for number in range(1, 5)]


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = time.time()
    for name in filenames:
        read_info(name=name)
    print(f'Линейный: {time.time() - start:.6f} секунд')

    start = time.time()
    with Pool(processes=4) as p:
        p.map(read_info, filenames)
    print(f'Многопроцессорный: {time.time() - start:.6f} секунд')




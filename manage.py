# -*- coding：utf8 -*-
# @Project : read-file
# @Author : qxq
# @Time : 2022/3/14 17:55
import csv
import logging
import os
import sys
import time

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'rlfpure_bin_stat.csv')
    while True:
        f = csv.reader(open(file_path, 'r'))
        for idx, i in enumerate(f):
            if idx == 0:
                continue
            logging.info(i)
            time.sleep(2)
        time.sleep(2)


if __name__ == '__main__':
    main()

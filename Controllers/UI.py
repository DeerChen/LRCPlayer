'''
Description: 
Author: Senkita
Date: 2021-04-16 18:53:58
LastEditors: Senkita
LastEditTime: 2021-04-16 20:48:53
'''
from pathlib import Path
from typing import List
from .Player import Player
import os
from random import shuffle


class UI:
    def __init__(self) -> None:
        self.lrc_dir = Path('./lrc')
        self.lrc_files = self.__list_lrc_files()

    def __list_lrc_files(self) -> List[str]:
        lrc_files = []
        for file in self.lrc_dir.iterdir():
            if file.suffix == '.lrc':
                lrc_files.append(file.stem)
        return lrc_files

    def __choose(self) -> None:
        print('顺序播放输入A，随机播放输入B，退出请按Ctrl+C')
        print('请输入操作，并以回车结束：', end='')

        choice = input()

        if choice in ('A', 'a'):
            os.system('cls')
            Player(self.lrc_files).play()
        elif choice in ('B', 'b'):
            os.system('cls')
            lrc_files = self.lrc_files
            shuffle(lrc_files)
            Player(lrc_files).play()
        else:
            print('输入有误，请重新输入')
            self.__choose()

    def display(self) -> None:
        print('歌词保存在"lrc/"目录下，现有歌词{}份：'.format(len(self.lrc_files)))

        count = 0
        for file in self.lrc_files:
            count += 1
            print('{}. {}'.format(count, file))
        self.__choose()

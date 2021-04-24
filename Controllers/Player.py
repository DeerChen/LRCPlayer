'''
Description: 
Author: Senkita
Date: 2021-04-16 17:57:01
LastEditors: Senkita
LastEditTime: 2021-04-16 20:25:03
'''
import time
import re
from pathlib import Path
from typing import List


class Player:
    def __init__(self, lrc_files) -> None:
        self.lrc_files = lrc_files
        self.lrc_dir = Path('./lrc')

    def __read_lrc_content(self, file_name) -> List[str]:
        with open(
            Path.joinpath(self.lrc_dir, file_name + '.lrc'), 'r', encoding='utf-8'
        ) as f:
            return f.readlines()

    def __create_lrc_dict(self, lrc_list) -> dict:
        lrc_dict = {}
        time_pattern = re.compile(r'\d{2}:\d{2}.\d{2}')

        for lrc in lrc_list:
            lrc_time = re.findall(time_pattern, lrc)
            if lrc_time != []:
                lrc_dict[lrc_time[0]] = lrc.split(']')[-1].replace('\n', '').strip()
        return lrc_dict

    def play(self) -> None:
        for file_name in self.lrc_files:
            lrc_list = self.__read_lrc_content(file_name)
            lrc_dict = self.__create_lrc_dict(lrc_list)

            temp = 0
            for t in lrc_dict.keys():
                m = float(t.split(':')[0])
                s = float(t.split(':')[-1])
                time2num = m * 60 + s

                time.sleep(time2num - temp)
                temp = time2num
                print(lrc_dict[t].ljust(40), end='\r')
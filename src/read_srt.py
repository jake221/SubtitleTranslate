# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     read_srt
   Description :
   Author :       liuying
   date：          2019-07-25
-------------------------------------------------
   Change Activity:
                   2019-07-25:
-------------------------------------------------
"""
__author__ = 'liuying'

import srt

# read plain text
def read_txt(text_file):
    tmp_str = ''
    with open(text_file, 'r') as f:
        for line in f:
            tmp_str += line.strip()
    return tmp_str

input_txt_file = '../input_txt/read.cn.txt'
input_srt_file = "../input_srt/read.cn.srt"
srt_file = open(input_srt_file, encoding='UTF-8-sig')
subtitle = list(srt.parse(srt_file.read()))
plain_txt = read_txt(input_txt_file)

def obtain_dialog_idx(origin_sub, plain_text):
    current_idx = 0
    dialog_idx = []
    for sub in origin_sub:
        sub.content = sub.content.replace('\n', ' ')
        current_idx += len(sub.content)
        while(sub.content[-1] != plain_text[current_idx-1]):
            current_idx += 1
        dialog_idx.append(current_idx)
    return dialog_idx

dialog_idx = obtain_dialog_idx(subtitle, plain_txt)




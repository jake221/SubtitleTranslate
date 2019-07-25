from src.utils import translate_and_compose

input_srt_file = "../input_srt/read.cn.srt"
input_txt_file = '../input_txt/read.cn.txt'
output_srt_file = "../output_srt/read_en_cn_both.srt"


# read plain text
def read_txt(text_file):
    tmp_str = ''
    with open(text_file, 'r') as f:
        for line in f:
            tmp_str += line.strip()
    return tmp_str

plain_txt = read_txt(input_txt_file)

# Translate the subtitle into English
# save both English and Chinese to the output input_srt file
translate_and_compose(input_srt_file, output_srt_file, plain_txt, 'zh-CN', 'en', encoding='UTF-8-sig')

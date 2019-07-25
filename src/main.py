from src.utils import translate_and_compose

input_file = "../input_srt/read.cn.input_srt"
output_file = "../output_srt/read_en_cn_both.input_srt"

# Translate the subtitle into English
# save both English and Chinese to the output input_srt file
translate_and_compose(input_file, output_file, 'zh-CN', 'en', encoding='UTF-8-sig')

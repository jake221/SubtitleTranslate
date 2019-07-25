from src.utils import translate_and_compose
from src.utils import read_txt

input_srt_file = "../input_srt/wengkai.srt"
input_txt_file = '../input_txt/wengkai.txt'
output_srt_file = "../output_srt/wengkai_en.srt"
#
# read plain text translation of the video
plain_txt = read_txt(input_txt_file)

# Translate the subtitle into English
# save both English and Chinese to the output input_srt file
# translate_and_compose(input_srt_file, output_srt_file, plain_txt, 'zh-CN', 'en', encoding='UTF-8-sig', space=True)
#
translate_and_compose(input_srt_file, output_srt_file, plain_txt, 'zh-CN', 'en', encoding='UTF-8-sig', space=True, both=False)

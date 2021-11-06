# python -m venv env 가상화폴더 생성
# env\Scripts\activate.bat 가상화 실행
print("워드 클라우드")

from konlpy.tag import Okt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

with open('test.txt','r',encoding="UTF-8") as f:
  reply = f.readlines()

# 크롤링한 댓글파일 가져와서 리스트 변수에 저장
# 반드시 문자 사이 공백을 넣어야지 wordcloud에서 분석 가능!!
ok_twitter = Okt()
text = ''
for sentence in reply:
  for noun in ok_twitter.nouns(sentence):
    text += noun+' '
print(text)

# 크롤링한 댓글파일 가져와서 리스트 변수에 저장
# 배경이 흰색인 마스크 이미지
mask_image = np.array(Image.open('alice_mask.png'))
wc = WordCloud(
    font_path='font/Binggrae.ttf', # 사용할 폰트
    background_color='white', # 배경색
    max_words=100, # 최대 빈도수를 기준으로 출력할 단어 수
    mask=mask_image, # 마스크 이미지
    max_font_size=70, # 최대 폰트 크기
    colormap='hsv' # 컬러 스타일 ex)'Accent', 'Accent_r', 'Blues', 'Blues_r' 등등
).generate(text)
wc.to_file('./drive/MyDrive/machine_learning_data/wc_result.png')
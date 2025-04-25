import re 
from konlpy.tag import Mecab, Okt

def normalize(text):
    # 같은 글자 3번 이상 반복 축소 (정규화)
    text = re.sub(r'(\w)\1{2,}', r'\1', text)
    return text.strip()

def cleaning_text(text):
      "특수 문자를 제거"
      result = re.sub(r'[^a-z가-힣0-9\s]', '', text)

      return result if result.strip() != '' else None

def remove_stopwords(tokens, stopwords):
    return [token for token in tokens if token not in stopwords]
  
def mecab_tokenizer(text):
    mecab = Mecab()
    return mecab.morphs(text)

def basic_tokenizer(text):
    return text.split()

def get_tokenizer(name):
    
    if name == "mecab":
        mecab = Mecab()
        return mecab.morphs
    elif name == "okt": 
        okt = Okt()
        return okt.morphs
    else:
        return basic_tokenizer
# 폰트 설정을 위해 언제든지 사용 가능

import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 시스템에서 사용할 수 있는 한글 폰트 확인
for font in fm.findSystemFonts():
    if 'Nanum' in font or 'Malgun' in font or 'AppleGothic' in font:
        print(font)

# 한글 폰트 경로 설정 
import platform
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')  # Windows의 기본 한글 폰트 (맑은 고딕)
elif platform.system() == 'Darwin':  # macOS
    rc('font', family='AppleGothic')  # macOS의 기본 한글 폰트 (애플 고딕)
else:  # Linux
    rc('font', family='NanumGothic')  # Linux에서는 나눔고딕을 사용 (설치 필요)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.titlepad'] = 10
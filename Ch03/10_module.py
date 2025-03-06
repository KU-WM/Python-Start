import dataRead as data

# import 하는 경우 파일이 크기 때문에 기본적으로 캐시를 가진다.
# 따라서 import 이후에 모듈을 수정해도 수정된 함수를 불러오지 못할 수있다.
# importlib의 reload를 실행하면 해결
# import importlib
# importlib.reload()

data.preprocess()
data.load_file()
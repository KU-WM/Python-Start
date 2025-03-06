# 03장의 슬라이드 31p
# 훈연집합과 테스트집합이 도일하여 100퍼
# 10개를 빼서 테스트집합으로 사용시 전부 3으로 예측
#       => gamma를 0.1에서 0.0001로 낮추니 해결됨

# gamma를 0.0001로 낮추니 훈련데이터 = 테스트데이터 임에도 틀리는 오류가 발생
#                                                  => 훈련이 정확히 되지 않음
#                                                  => C의 값을 50으로 늘려 해결
# 
# gamma  : 각 데이터 사이의 경계
#           => 너무 크면 복잡해져서 과적합(overfitting), 너무 작으면 경계가 모호해져 언더피팅(underfitting)
# C(cost): 각 데이터의 경계의 마진 너비와 오분류 데이터간의 균형을 결정
#           => 즉 특정 아이템 경계의 마진이 클수록 해당 아이템으로 분류될 가능성이 증가 => 일부의 오분류를 허용
#           => C가 작을수록 마진이 커짐 => 일부 오분류 허용
#                   데이터의 일반적인 패턴을 더 잘 일반화 가능 / 다만 언더피팅 가능성 상승
#           => C가 클수록 마진이 작아짐 => 오분류에 엄격해짐, 정확도 상승, 
#                   데이터의 특이케이스 구분에 적합 / 다만 오버피팅 가능성 상승

from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import GridSearchCV


digit = datasets.load_digits()

# C값을 찾는 방법
# param_grid = {'C': [0.01, 0.1, 1, 10, 50, 100]}
# st = svm.SVC(gamma=0.0001)
# grid = GridSearchCV(st, param_grid, cv=6)
# grid.fit(digit.data, digit.target)
# print("Best C value:", grid.best_params_['C'])

# C와 Gamma를 둘다 찾는 방법
# train데이터를 임의로 나누어 test로 사용하기 때문에 교차검증을 통해 찾아줌
# param_grid = {
#     'C': [0.1, 0.5, 1, 5, 10, 50, 100],
#     'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
# }
# grid = GridSearchCV(svm.SVC(), param_grid, cv=5, scoring='accuracy')
# grid.fit(digit.data, digit.target)
# print("Best Parameters:", grid.best_params_)


s = svm.SVC(gamma=0.0005, C=10)
s.fit(digit.data[:1790], digit.target[:1790])
print(len(digit.data))

new_d = digit.data[1790:]
res = s.predict(new_d)
print("Predict:", res)
print("True:", digit.target[1790:])

res = s.predict(digit.data)
correct = [i for i in range(len(res)) if res[i] == digit.target[i]]
wrong = [i for i in range(len(res)) if res[i] != digit.target[i]]
print(wrong)
accuracy = len(correct)/len(res)
print("Correct Percent: ", accuracy * 100, "%", sep="")
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import numpy as np

# 문자열 레이블 데이터
y_train = ["cat", "dog", "bird", "cat", "dog"]

# 문자열 레이블 → 정수형으로 변환
label_encoder = LabelEncoder()
y_train_int = label_encoder.fit_transform(y_train)  # 정수형 레이블

# 정수형 레이블 → 원-핫 인코딩
y_train_one_hot = to_categorical(y_train_int)

print("Original Labels:", y_train)
print("Integer Encoded:", y_train_int)
print("One-Hot Encoded:\n", y_train_one_hot)

# 4. 원-핫 인코딩 → 정수형 복원
#     argmax => 배열에서 가장 큰 값의 인덱스를 반환
#     axis => 최대값을 계산할 리스트의 차원을 지정
#           1차원배열 axis = 0인 경우
#              [0, 0, 1, 0]  =>  2
#           2차원 배열 axis = 1인 경우
#               [[0, 1], [1, 0]] => [1, 0]
integer_decoded = np.argmax(y_train_one_hot, axis=1)

# 5. 정수형 → 원래 문자열 레이블 복원
restored_labels = label_encoder.inverse_transform(integer_decoded)

print("\nDecoded Integer Labels:", integer_decoded)
print("Restored Original Labels:", restored_labels)

############################################################################################
# Tensorflow의 경우는 자체 내장 함수인 StringLookup을 활용해 사용 가능

import tensorflow as tf

# 문자열 레이블 예시
original_labels = ["cat", "dog", "bird"]

# 문자열을 정수로 변환하는 StringLookup

# num_oov_indices => OOV(Out Of Vocabulary)추후 예측시 훈련 lable에 없는 레이블의 처리방식 설정
# num_oov_indices=0으로 설정하면 OOV 처리를 하지 않으며, 입력 값이 학습한 문자열 범위 내에 있어야 합니다.
string_lookup = tf.keras.layers.StringLookup(num_oov_indices=0)
# 문자열을 학습해서 각 문자열을 숫자와 매핑함
# 기본적으로 0은 사용되지 않으며 1부터 시작
string_lookup.adapt(original_labels)  # 문자열 학습

# 문자열 -> 정수 인코딩
# 숫자 레이블로 변환
encoded_labels = string_lookup(original_labels)
print("Encoded labels:", encoded_labels.numpy())  # 예: [1, 2, 3]

# 정수 -> 문자열 복원용 StringLookup
reverse_lookup = tf.keras.layers.StringLookup(num_oov_indices=0, invert=True)
reverse_lookup.adapt(original_labels)  # 원래 문자열 복원에 사용

# 복원: 정수 레이블을 문자열 레이블로 변환
# Tensorflow의 기본 형식이 byte라 b'cat'으로 출력
decoded_labels = reverse_lookup(encoded_labels)
print("Decoded labels:", decoded_labels.numpy())  # 예: [b'cat', b'dog', b'bird']

# byte 타입을 인코딩
decoded_labels = [label.decode('utf-8') for label in decoded_labels.numpy()]
print("Decoded2 labels:", decoded_labels)  # ['cat', 'dog', 'bird']


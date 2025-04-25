import numpy as np

def get_basis_num(tokenized_corpus, percentile=90):# 기준이되는 숫자 가져오는 함수
  lengths = [len(tokens) for tokens in tokenized_corpus]
  basis_num = int(np.percentile(lengths, percentile))

  print(f'최대 길이: {max(lengths)}')
  print(f'평균 길이: {np.mean(lengths)}')
  print(f'중앙값: {np.median(lengths)}')

  return basis_num
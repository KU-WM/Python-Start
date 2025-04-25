def build_vocab(tokenized_corpus, min_freq=2):
    from collections import Counter
    
    counter = Counter()
    # 중복 단어 없이 단어 사전 만들기 + 최소 등장 횟수를 반영하기
    for doc in tokenized_corpus:
      counter.update(doc)
    vocab = {word: idx for idx, (word, count) in enumerate(counter.items(), start=2) if count > min_freq}
    vocab['<PAD>'] = 0
    vocab['<UNK>'] = 1

    return vocab

def encode(tokens, vocab, max_len):
  # 단어 사전을 참고해서 tokens의 단어를 정수로 치환 하기
  # 최대 개수(max_len)을 초과하지 않게 자르고, 길이가 최대 개수에 못 미치면 <PAD>의 라벨을 가져와서 뒤에 추가
  labeled_tokens = [vocab.get(token, vocab['<UNK>']) for token in tokens] 

  if len(labeled_tokens) < max_len:
    labeled_tokens += [vocab['<PAD>']] * (max_len - len(labeled_tokens))
  else:
    labeled_tokens = labeled_tokens[:max_len]

  return labeled_tokens
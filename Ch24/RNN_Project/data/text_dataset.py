import re

import torch
from torch.utils.data import Dataset

class NSMCDataset(Dataset): # 장점
    def __init__(self, corpus, label, tokenizer, max_len, vocab=None, stopwords=None):
      self.inputs = corpus
      self.labels = label

      self._tokenizer = tokenizer
      self.stopwords = stopwords
      self.vocab = vocab or self._build_vocab(corpus)
      self.max_len = max_len

    def __getitem__(self, index): # 필요할 때마다 인덱스로 데이터 접근
      document = self.inputs[index]
      label = self.labels[index]

      # 전처리
      tokens = self._preprocess_tokens(document)
      # 인코딩
      encoded_tokens = self._encode(tokens, self.vocab, self.max_len)

      # 벡터화
      return torch.tensor(encoded_tokens, dtype=torch.long), torch.tensor(label, dtype=torch.long)

    def __len__(self):
      return len(self.inputs)


    def _cleaning_text(self, text):
      "특수 문자를 제거"
      result = re.sub(r'[^a-z가-힣0-9\s]', '', text)

      return result if result.strip() != '' else None


    def _normalize(self, text):
        # 같은 글자 3번 이상 반복 축소 (정규화)
        text = re.sub(r'(\w)\1{2,}', r'\1', text)
        return text.strip()

    def _remove_stopwords(self, tokens):
      return [token for token in tokens if token not in self.stopwords]


    def _tokenize(self, document):
      return self._tokenizer(document)


    def _preprocess_tokens(self, document):
      # clean_doc = self._cleaning_text(document)
      norm_doc = self._normalize(document)
      tokenized_doc = self._tokenize(norm_doc)

      if self.stopwords:
        tokens = self._remove_stopwords(tokenized_doc)
        return tokens

      return tokenized_doc

    def _build_vocab(self, corpus, min_freq=2):
      from collections import Counter

      counter = Counter()
      # 중복 단어 없이 단어 사전 만들기 + 최소 등장 횟수를 반영하기
      for doc in corpus:
        tokens = self._preprocess_tokens(doc)
        counter.update(tokens)
      vocab = {word: idx for idx, (word, count) in enumerate(counter.items(), start=2) if count > min_freq}
      vocab['<PAD>'] = 0
      vocab['<UNK>'] = 1

      return vocab

    def _encode(self, tokens, vocab, max_len):
      labeled_tokens = [vocab.get(token, vocab['<UNK>']) for token in tokens] # [3, 5, 7, 299]

      if len(labeled_tokens) < max_len:
        labeled_tokens += [vocab['<PAD>']] * (max_len - len(labeled_tokens)) # # [3, 5, 7, 299, 0]
      else:
        labeled_tokens = labeled_tokens[:max_len]

      return labeled_tokens
"""
CSV読み込みのコードをここに書く
"""

data = [[]]  # CSVデータを格納するリスト(2次元配列)

gen = 1  # 何つ前まで見るか

chain = {}

for sentence in data:
    sentence = ["[BOS]"] + sentence + ["[EOS]"]
    for i in range(len(sentence) - gen):
        if "".join(sentence[i:i + gen]) not in chain:
            chain["".join(sentence[i:i + gen])] = []
        chain["".join(sentence[i:i + gen])].append(sentence[i + gen])

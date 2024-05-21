import random

maxLength = 1000
markov_chain = {}
generation = 1

length = 0

sentence = ["[BOS]"]
index = 0

while length < maxLength:
    endAt = min(len(sentence), index + generation)
    # 存在しない場合は終了
    if "".join(sentence[index:endAt]) not in markov_chain:
        break
    sentence.append(random.choice(
        markov_chain["".join(sentence[index:endAt])]))
    index += 1
    length += len(sentence[-1])
    # 　終了文字が出たら終了
    if sentence[-1] == "[EOS]":
        break

print("".join(sentence[1:-1]))

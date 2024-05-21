from csv import reader as r
from json import dumps, loads
from os import path
from random import choice


def createChain(fileName: str, gen: int):
    with open(fileName, "r", encoding="utf_8_sig") as f:
        reader = r(f)
        wakati = [row for row in reader]
    chain = {}

    for sentence in wakati:
        sentence = ["[BOS]"] + sentence + ["[EOS]"]
        for j in range(1, min(gen + 1, len(sentence) - 1)):
            if "".join(sentence[:j]) not in chain:
                chain["".join(sentence[:j])] = []
            chain["".join(sentence[:j])].append(sentence[j])
        for j in range(gen + 1, len(sentence) - gen):
            index = j + gen
            if "".join(sentence[j:index]) not in chain:
                chain["".join(sentence[j:index])] = []
            chain["".join(sentence[j:index])].append(sentence[index])

    return chain


def save_to_json(chain: dict, fileName: str):
    with open(fileName, "w", encoding="utf_8_sig") as f:
        f.write(dumps(chain, indent=4))


def genText(chain: dict, generation: int, maxLength: 1000) -> str:
    if not chain:
        return ""
    
    length = 0

    result = []
    sentence = ["[BOS]"]
    index = 0

    while True:
        endAt = min(len(sentence), index + generation)
        # 存在しない場合は適当に選ぶ(要改善)
        if "".join(sentence[index:endAt]) not in chain:
            # result += sentence
            # sentence = ["[BOS]"]
            break
            # sentence.append(
            #     choice(chain[choice(list(chain.keys()))]))
        else:
            sentence.append(choice(
                chain["".join(sentence[index:endAt])]))
        index += 1
        length += len(sentence[-1])
        # 　終了文字が出た場合
        if sentence[-1] == "[EOS]" and length < maxLength:
            result += sentence
            sentence = ["[BOS]"]
        # 最大文字数を超えた場合
        if length >= maxLength:
            break

    return "".join(sentence[1:-1])


def read_json(fileName: str) -> dict:
    if path.exists(fileName) == False:
        return {}
    with open(fileName, "r", encoding="utf_8_sig") as f:
        return loads(f.read())


if __name__ == "__main__":
    name = "musuka"
    depth = 1
    # chain = createChain(f"data/{name}.csv", depth)
    # save_to_json(chain, f"data/{name}_{depth}.json")
    chain = read_json(f"data/{name}_{depth}.json")
    print("\n".join([genText(chain, 1, 100) for i in range(30)]))

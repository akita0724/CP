import sys
from fugashi import Tagger, GenericTagger
import csv

name = "meigen"
ext = "txt"

fileName = f"/Users/yohei/Git/markov_CP/rawData/{name}.{ext}"
output = f"/Users/yohei/Git/markov_CP/data/{name}.csv"

result = []

# 古文用
# with open(fileName, "r") as f:
#     data = f.read().replace("\n", "").replace("。", "。\n").replace("「", "\n").replace("」", "\n").split("\n")

# # 普通文用
data = []
sentence = ""

with open(fileName, "r") as f:
    data = f.read().replace("。", "。\n").split("\n")

# # 英文用
# data = []
# with open(fileName, "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[0] != "spam":
#             continue
#         data = data + row[1].split(" ")

# # 名詞Only用
# data = []
# with open(fileName, "r") as f:
#     data = f.read().replace('"', "").split("\n")
# for row in data:
#     result.append([w for w in row])
# with open(output, "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(result)
# sys.exit()

wakati = GenericTagger("-d /Users/yohei/Downloads/unidic-chuko")
wakati = Tagger("-Owakati")

for sentence in data:
    result.append(wakati.parse(sentence).split())

with open(output, "w") as f:
    writer = csv.writer(f)
    writer.writerows(result)

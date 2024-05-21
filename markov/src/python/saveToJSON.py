import json

# マルコフのチェーンデータ
chain = {}

# 保存先のファイルパス
file_path = "/path/to/save.json"

# JSONファイルに保存
with open(file_path, "w") as json_file:
    json.dump(chain, json_file)

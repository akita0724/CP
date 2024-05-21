import csv

data = []

# CSVファイルを開く
with open('/path/to/your/file.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        data.append(row)

# 最初の行を表示
print(data[0])

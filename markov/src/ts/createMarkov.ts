/*
CSV読み込みのコードをここに書く
*/

let data: string[][] = [[]];  // CSVデータを格納するリスト(2次元配列)

let gen: number = 1;  // 何つ前まで見るか

let chain: { [key: string]: string[] } = {};

for (let sentence of data) {
  sentence = ["[BOS]", ...sentence, "[EOS]"];
  for (let i = 0; i < sentence.length - gen; i++) {
    const key = sentence.slice(i, i + gen).join("");
    if (!(key in chain)) {
      chain[key] = [];
    }
    chain[key].push(sentence[i + gen]);
  }
}

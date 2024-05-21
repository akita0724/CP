const maxLength = 1000;
const markov_chain: { [key: string]: string[] } = {};
let generation = 1;

let len = 0;

const sentence = ["[BOS]"];
let index = 0;

while (length < maxLength) {
  const endAt = Math.min(sentence.length, index + generation);
  // キーが存在しない場合は終わる
  if (!markov_chain[sentence.slice(index, endAt).join("")]) {
    break;
  }
  sentence.push(
    markov_chain[sentence.slice(index, endAt).join("")][
      Math.floor(Math.random() * markov_chain[sentence.slice(index, endAt).join("")].length)
    ]
  );
  index += 1;
  length += sentence[sentence.length - 1].length;
  // 終了文字が出た場合
  if (sentence[sentence.length - 1] === "[EOS]") {
    break;
  }
}

console.log(sentence.slice(1, -1).join(""));

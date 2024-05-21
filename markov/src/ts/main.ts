import { readFileSync, writeFileSync, existsSync } from 'fs';
import { randomInt } from 'crypto';

interface Chain {
  [key: string]: string[];
}

function createChain(fileName: string, gen: number): Chain {
  const content = readFileSync(fileName, 'utf-8');
  const wakati = content.split('\n').map((row) => row.split(','));

  const chain: Chain = {};

  for (const sentence of wakati) {
    sentence.unshift('[BOS]');
    sentence.push('[EOS]');
    for (let j = 1; j < Math.min(gen + 1, sentence.length - 1); j++) {
      const key = sentence.slice(0, j).join('');
      if (!chain[key]) {
        chain[key] = [];
      }
      chain[key].push(sentence[j]);
    }
    for (let j = gen + 1; j < sentence.length - gen; j++) {
      const key = sentence.slice(j, j + gen).join('');
      if (!chain[key]) {
        chain[key] = [];
      }
      chain[key].push(sentence[j + gen]);
    }
  }

  return chain;
}

function saveToJson(chain: Chain, fileName: string): void {
  const content = JSON.stringify(chain, null, 4);
  writeFileSync(fileName, content, 'utf-8');
}

function genText(chain: Chain, generation: number, maxLength: number): string {
  if (!chain) {
    return '';
  }

  let length = 0;
  const result: string[] = [];
  const sentence = ['[BOS]'];
  let index = 0;

  while (true) {
    const endAt = Math.min(sentence.length, index + generation);
    if (!chain[sentence.slice(index, endAt).join('')]) {
      break;
    } else {
      sentence.push(
        chain[sentence.slice(index, endAt).join('')][randomInt(0, chain[sentence.slice(index, endAt).join('')].length)]
      );
    }
    index++;
    length += sentence[sentence.length - 1].length;
    if (sentence[sentence.length - 1] === '[EOS]' && length < maxLength) {
      result.push(...sentence);
      sentence.length = 1;
    }
    if (length >= maxLength) {
      break;
    }
  }

  return result.slice(1, -1).join('');
}

function readJson(fileName: string): Chain {
  if (!existsSync(fileName)) {
    return {};
  }
  const content = readFileSync(fileName, 'utf-8');
  return JSON.parse(content);
}

const name = 'musuka';
const depth = 1;
// const chain = createChain(`data/${name}.csv`, depth);
// saveToJson(chain, `data/${name}_${depth}.json`);
const chain = readJson(`data/${name}_${depth}.json`);
console.log(Array.from({ length: 10 }, () => genText(chain, 1, 20)).join('\n'));

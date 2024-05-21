import * as fs from 'fs';

// マルコフのチェインデータ
const chain: Record<string, any> = {};

// 保存先のファイルパス
const file_path = "/path/to/save.json";

// JSONファイルに保存
fs.writeFileSync(file_path, JSON.stringify(chain));

import * as csv from 'csv-parser';
import * as fs from 'fs';

const data: any[] = [];

// CSVファイルを開く
fs.createReadStream('/path/to/your/file.csv')
  .pipe(csv())
  .on('data', (row: any) => {
    data.push(row);
  })
  .on('end', () => {
    // 最初の行を表示
    console.log(data[0]);
  });

var readline = require('readline');
var rl = readline.createInterface({
 input: process.stdin,
 output: process.stdout
});

process.stdin.on('end', () => { console.log(total); process.exit(0); });

rl.on('line', function (data) {
  const wordsArray = data

  let result = wordsArray.split(' ').filter((a) => {
    const reverseArrayWord = a.split('').reverse().join('')
    if (reverseArrayWord === a) {
      return true
    }

    return false
  })
  console.log(result)
});


// 2
console.clear();
const enterData = "мадам собака анна радар яблоко";

const result = enterData
  .split(" ")
  .filter(([...word] = word) => {
    return word.every((f, dex) => f === word[word.length - 1 - dex]);
  })
  .join(" ");

console.log("result", result);




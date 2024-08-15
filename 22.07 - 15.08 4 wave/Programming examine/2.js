var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let total = 0;

process.stdin.on('end', () => { console.log(total); process.exit(0); });

rl.on('line', function (data) {
  let [a, b, c] = data.split(' ').map(a => +a);
  d = Math.pow(b, 2) - 4 * a * c;

  if (d < 0) {
    return
  } else if (d === 0) {
    console.log(-b / (2 * a));
  } else {
    console.log((Math.sqrt(d) - b) / (2 * a));
    console.log((-Math.sqrt(d) - b) / (2 * a));
  }

});
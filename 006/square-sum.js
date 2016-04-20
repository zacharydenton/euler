let sum = 0, sumSquares = 0
for (let i = 1; i <= 100; i++) {
  sum += i
  sumSquares += i * i
}
console.log(sum * sum - sumSquares)

let n = 600851475143
let limit = Math.ceil(Math.sqrt(n))
for (var i = 3; i <= limit; i += 2) {
  while (n % i === 0) {
    n = Math.floor(n / i)
    limit = Math.ceil(Math.sqrt(n))
  }
}
console.log(n)

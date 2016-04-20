const sieve = {}
let n = 0
for (var q = 2; n < 10001; q++) {
  if (sieve[q]) {
    sieve[q].forEach((p) => {
      const list = sieve[p + q] || []
      list.push(p)
      sieve[p + q] = list
    })
  } else {
    sieve[q * q] = [q]
    n++
  }
}
console.log(q - 1)

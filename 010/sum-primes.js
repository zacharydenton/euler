const sieve = {}
let s = 0
for (let q = 2; q < 2000000; q++) {
  if (sieve[q]) {
    sieve[q].forEach((p) => {
      const list = sieve[p + q] || []
      list.push(p)
      sieve[p + q] = list
    })
    delete sieve[q]
  } else {
    s += q
    sieve[q * q] = [q]
  }
}
console.log(s)

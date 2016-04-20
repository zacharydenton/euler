let s = 0
let f = [1, 1]
while (f[0] < 4e6) {
  if (f[0] % 2 === 0) s+= f[0]
  f = [f[1], f[0] + f[1]]
}
console.log(s)

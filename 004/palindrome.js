const isPalindrome = (s) => s === s.split("").reverse().join("")
let max = 0
for (let i = 100; i < 1000; i++) {
  for (let j = 100; j < 1000; j++) {
    const s = (i * j)
    if (s > max && isPalindrome(s.toString())) {
      max = s
    }
  }
}
console.log(max)

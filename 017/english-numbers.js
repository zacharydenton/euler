const ones = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen'
}

const tens = {
  2: 'twenty',
  3: 'thirty',
  4: 'forty',
  5: 'fifty',
  6: 'sixty',
  7: 'seventy',
  8: 'eighty',
  9: 'ninety'
}

function english(number) {
  let parts = []

  if (number >= 1000) {
    parts.push(ones[Math.floor(number / 1000)])
    parts.push("thousand")
    number %= 1000
  }

  if (number >= 100) {
    parts.push(ones[Math.floor(number / 100)])
    parts.push("hundred")
    if (number % 100 !== 0) {
      parts.push("and")
    }
    number %= 100
  }

  if (number >= 20) {
    parts.push(tens[Math.floor(number / 10)])
    number %= 10
  }

  if (ones[number]) {
    parts.push(ones[number])
  }

  return parts.join("")
}

const words = []
for (let i = 1; i <= 1000; i++) {
  words.push(english(i))
}
console.log(words.join("").length)

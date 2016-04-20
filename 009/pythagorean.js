for (let a = 1; a < 1000; a++) {
  for (let b = a, lb = 1000 - a; b < lb; b++) {
    const c = 1000 - (a + b)
    if (a * a + b * b === c * c) {
      return console.log(a * b * c)
    }
  }
}

function permutate(n, array) {
  const al = array.length
  for (let i = 0; i < n - 1; i++) {
    let k, l
    for (let j = 0; j < al - 1; j++) {
      if (array[j] < array[j + 1]) {
        k = j
      }
    }
    for (let j = k; j < al; j++) {
      if (array[k] < array[j]) {
        l = j
      }
    }
    let tmp = array[k]
    array[k] = array[l]
    array[l] = tmp
    let begin = k + 1
    let end = al - 1
    while (begin < end) {
      tmp = array[begin]
      array[begin] = array[end]
      array[end] = tmp
      begin += 1
      end -= 1
    }
  }
  return array
}
console.log(permutate(1000000, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).join(""))

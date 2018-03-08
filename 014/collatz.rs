fn main() {
    let mut collatz: Vec<usize> = vec![0; 1000000];
    collatz[1] = 1;
    let max = (2..collatz.len())
        .max_by_key(|&i| {
            let mut j: usize = i;
            let mut len = 0;
            loop {
                if j < collatz.len() && collatz[j] != 0 {
                    break;
                }
                len += 1;
                if j % 2 == 0 {
                    j /= 2;
                } else {
                    j = 3 * j + 1;
                }
            }
            len += collatz[j];
            collatz[i] = len;
            len
        })
        .unwrap();
    println!("{}", max);
}

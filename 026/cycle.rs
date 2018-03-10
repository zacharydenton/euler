fn cycle_length(n: usize) -> usize {
    let mut remainder = 10;
    let mut seen = vec![0; 10 * n + 1];
    for i in 0.. {
        if remainder == 0 {
            return 0;
        } else if seen[remainder] != 0 {
            return i - seen[remainder];
        }
        seen[remainder] = i;
        remainder = 10 * (remainder % n);
    }
    0
}

fn main() {
    let max: usize = (1..1000).max_by_key(|&n| cycle_length(n)).unwrap();
    println!("{}", max);
}

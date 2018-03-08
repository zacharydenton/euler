fn choose(n: u64, k: u64) -> u64 {
    (0..k).fold(1, |acc, i| acc * (n - i) / (i + 1))
}

fn main() {
    println!("{}", choose(40, 20));
}

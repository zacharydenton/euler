fn main() {
    let sum = (1..501)
        .map(|i| {
            let n = 2 * i + 1;
            4 * n * n - 6 * n + 6
        })
        .sum::<u64>() + 1;
    println!("{}", sum);
}

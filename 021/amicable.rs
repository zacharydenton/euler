fn sum_divisors(n: u64) -> u64 {
    let mut result = 0;
    let max = (n as f64).sqrt() as u64;
    for i in 2..max {
        if n % i == 0 {
            let x = n / i;
            if x == i {
                result += i;
            } else {
                result += i + x;
            }
        }
    }
    1 + result
}

fn main() {
    let sum: u64 = (1..10000)
        .filter(|&n| {
            let x = sum_divisors(n);
            (n != x) && (sum_divisors(x) == n)
        })
        .sum();
    println!("{}", sum);
}

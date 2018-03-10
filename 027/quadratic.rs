fn is_prime(n: i64) -> bool {
    if n < 1 {
        return false;
    }
    let max = (n as f64).sqrt() as i64;
    for d in 2..max {
        if n % d == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let mut best = (0, 0);
    let mut best_count = 0;
    let bs = (0..1000).filter(|&b| is_prime(b)).collect::<Vec<_>>();
    for a in -999..1000 {
        for &b in &bs {
            let count = (0..)
                .take_while(|n| is_prime(n * n + a * n + b))
                .map(|_| 1)
                .sum::<i64>();
            if count > best_count {
                best = (a, b);
                best_count = count;
            }
        }
    }
    println!("{}", best.0 * best.1);
}

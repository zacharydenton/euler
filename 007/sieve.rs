fn eratosthenes(limit: usize) -> Vec<usize> {
    let mut sieve = vec![true; limit];
    let mut p = 2;
    loop {
        // Eliminate multiples of p.
        let mut i = 2 * p - 1;
        while i < limit {
            sieve[i] = false;
            i += p;
        }
        // Find the next prime.
        if let Some(n) = (p..limit).find(|&n| sieve[n]) {
            p = n + 1;
        } else {
            break;
        }
    }
    sieve
        .iter()
        .enumerate()
        .filter(|&(_, &is_prime)| is_prime)
        .skip(1)
        .map(|(i, _)| i + 1)
        .collect()
}

fn main() {
    let primes = eratosthenes(1000000);
    println!("{}", primes[10000]);
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let t = a;
        a = b;
        b = t % b;
    }
    a
}

fn main() {
    let lcm = (2..21).fold(1, |acc, i| {
        acc * i / gcd(i, acc)
    });
    println!("{}", lcm);
}

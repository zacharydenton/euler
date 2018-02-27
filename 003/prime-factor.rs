fn main() {
    let mut n: u64 = 600851475143;
    let mut limit = n / 2;
    let mut i = 3;
    while i < limit {
        while n % i == 0 {
            n = n / i;
            limit = n / 2;
        }
        i += 2;
    }
    println!("{}", n);
}

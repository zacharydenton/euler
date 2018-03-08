fn num_divisors(n: u64) -> u64 {
    let mut result = 0;
    let max = (n as f64).sqrt() as u64;
    for i in 1..max + 1 {
        if n % i == 0 {
            if n / i == i {
                result += 1;
            } else {
                result += 2;
            }
        }
    }
    return result;
}

fn main() {
    let triangles = (1..).scan(0, |triangle, n| {
        *triangle += n;
        Some(*triangle)
    });
    let first = triangles
        .skip_while(|&triangle| num_divisors(triangle) <= 500)
        .next()
        .unwrap();
    println!("{}", first);
}

fn main() {
    for a in 1..1000 {
        for b in a..(1000 - a) {
            let c = 1000 - (a + b);
            if a * a + b * b == c * c {
                return println!("{}", a * b * c);
            }
        }
    }
}

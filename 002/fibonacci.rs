fn main() {
    let mut sum = 0;
    let mut a = 1;
    let mut b = 2;
    let mut tmp;
    while b <= 4000000 {
        if b % 2 == 0 {
            sum += b;
        }
        tmp = a + b;
        a = b;
        b = tmp;
    }
    println!("{}", sum);
}

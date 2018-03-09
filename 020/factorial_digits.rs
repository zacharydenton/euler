fn main() {
    let mut decimal = [0; 200];
    decimal[0] = 1;
    for n in 1..101 {
        let mut carry = 0;
        for i in 0..decimal.len() {
            let mut digit = decimal[i];
            digit = n * digit + carry;
            carry = digit / 10;
            decimal[i] = digit % 10;
        }
    }
    println!("{}", decimal.iter().sum::<u64>());
}

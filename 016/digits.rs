fn main() {
    let mut decimal = vec![1];
    for _ in 0..1000 {
        let mut carry = 0;
        for i in 0..decimal.len() {
            let mut digit = decimal[i];
            digit = 2 * digit + carry;
            carry = digit / 10;
            decimal[i] = digit % 10;
        }
        if carry > 0 {
            decimal.push(carry);
        }
    }
    println!("{}", decimal.iter().sum::<u64>());
}

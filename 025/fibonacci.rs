fn main() {
    let mut a = vec![0];
    let mut b = vec![1];
    let mut n = 1;
    while b.len() < 1000 {
        let tmp = b.clone();
        let mut carry = 0;
        for i in 0..b.len() {
            if i >= a.len() {
                a.push(0);
            }
            let mut digit = a[i];
            digit = b[i] + digit + carry;
            carry = digit / 10;
            a[i] = digit % 10;
        }
        if carry > 0 {
            a.push(carry);
        }
        b = a;
        a = tmp;
        n += 1;
    }
    println!("{}", n);
}

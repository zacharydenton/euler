fn is_palindrome(number: u64) -> bool {
    let mut n = number;
    let mut reversed = 0;
    while n > 0 {
        let digit = n % 10;
        reversed = reversed * 10 + digit;
        n /= 10;
    }
    number == reversed
}

fn main() {
    let mut largest = 0;
    for a in 100..1000 {
        for b in 100..1000 {
            let product = a * b;
            if product > largest && is_palindrome(product) {
                largest = product;
            }
        }
    }
    println!("{}", largest);
}

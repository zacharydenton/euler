fn main() {
    let bytes = include_str!("numbers.txt");
    let digits: Vec<u64> = bytes
        .chars()
        .filter_map(|c| c.to_digit(10))
        .map(|c| c as u64)
        .collect();
    let max: u64 = digits
        .windows(13)
        .map(|digits| digits.iter().product())
        .max()
        .unwrap();
    println!("{}", max);
}

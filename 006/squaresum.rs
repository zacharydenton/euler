fn main() {
    let sum_squares = (1..101).map(|x| x*x).sum::<u64>();
    let square_sum = (1..101).sum::<u64>().pow(2);
    println!("{}", square_sum - sum_squares);
}

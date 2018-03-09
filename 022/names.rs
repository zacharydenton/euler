fn main() {
    let mut names: Vec<&str> = include_str!("names.txt").split(',').collect();
    names.sort();
    let sum: usize = names
        .iter()
        .enumerate()
        .map(|(i, name)| {
            let value: usize = name.chars()
                .skip(1)
                .take(name.len() - 2)
                .map(|c| 1 + (c as usize) - ('A' as usize))
                .sum();
            (i + 1) * value
        })
        .sum();
    println!("{}", sum);
}

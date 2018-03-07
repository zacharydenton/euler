fn main() {
    let grid: Vec<u64> = include_str!("grid.txt")
        .split(|c| c == ' ' || c == '\n')
        .filter_map(|n| n.parse().ok())
        .collect();
    let grid_length = grid.len() as isize;
    let intervals: [isize; 4] = [1, 20, 21, -19];
    let max_product: u64 = grid.iter()
        .enumerate()
        .map(|(i, _)| {
            intervals
                .iter()
                .filter_map(|interval| {
                    let last = (i as isize) + 3 * interval;
                    if last >= 0 && last < grid_length {
                        let product = (0..4)
                            .map(|x| grid[((i as isize) + x * interval) as usize])
                            .product();
                        Some(product)
                    } else {
                        None
                    }
                })
                .max()
                .unwrap()
        })
        .max()
        .unwrap();
    println!("{}", max_product);
}

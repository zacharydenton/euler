use std::cmp::max;

fn main() {
    let triangle = include_str!("triangle.txt");
    let mut graph: Vec<Vec<u64>> = triangle
        .lines()
        .map(|line| line.split(' ').map(|s| s.parse::<u64>().unwrap()).collect())
        .collect();
    for row in (0..(graph.len() - 1)).rev() {
        for i in 0..graph[row].len() {
            graph[row][i] += max(graph[row + 1][i], graph[row + 1][i + 1]);
        }
    }
    println!("{}", graph[0][0]);
}

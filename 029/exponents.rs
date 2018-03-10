use std::collections::HashSet;

fn main() {
    let mut seen = HashSet::new();
    for a in 2..101 {
        for b in 2..101 {
            let term = (a as f64).powf(b as f64);
            let bits: u64 = unsafe { std::mem::transmute(term) };
            seen.insert(bits);
        }
    }
    println!("{}", seen.len());
}

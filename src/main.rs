use std::fs::File;
use std::io::{BufReader, Error, ErrorKind};
use std::io::prelude::*;


fn day1p1() -> Result<u32, Error> {
    let f = File::open("./data/input1.txt")?;
    let br = BufReader::new(f);

    let depths: Result<Vec<u32>, Error> = br.lines()
        .map(|line| line.and_then(|v| v.parse().map_err(|e| Error::new(ErrorKind::InvalidData, e)))).collect();
    let depths = depths.unwrap();
    Ok(depths.iter().zip(depths.iter().skip(1)).map(|(&x, &y)| if y > x {1} else {0}).sum())
}

fn day1p2() -> Result<u32, Error> {
    let f = File::open("./data/input1.txt")?;
    let br = BufReader::new(f);

    let depths: Result<Vec<u32>, Error> = br.lines()
        .map(|line| line.and_then(|v| v.parse().map_err(|e| Error::new(ErrorKind::InvalidData, e)))).collect();
    let depths = depths.unwrap();
    let triplets: Vec<u32> = depths.windows(3).map(|v| v[0]+v[1]+v[2]).collect();
    let smoothe_depths: u32 = triplets.windows(2).map(|x| if x[1] > x[0] {1} else {0}).sum();
    Ok(smoothe_depths)
}

fn main() -> () {
    println!("Day 1 part 1 result: {}", day1p1().unwrap());
    println!("Day 1 part 2 result: {}", day1p2().unwrap());
}

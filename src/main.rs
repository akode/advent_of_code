use std::fs::File;
use std::io::{BufReader, Error, ErrorKind};
use std::io::prelude::*;
use std::ops;

#[derive(Debug)]
struct Pos {
    h: i32,
    d: i32
}

impl ops::Add<Pos> for Pos {
    type Output = Pos;
    fn add(self, rhs: Pos) -> Pos {
        Pos {
            h: self.h + rhs.h,
            d: self.d + rhs.d
        }
    }
}

fn parse_line(line: std::io::Result<String>) -> Pos {
    let l = line.unwrap();
    let mut iter = l.split_whitespace();
    let direction = iter.next().unwrap().to_string();
    let amount = iter.next().unwrap().parse().unwrap();
    match direction.as_ref() {
        "forward" => Pos {h: amount, d: 0},
        "up" => Pos {h: 0, d: -amount},
        "down" => Pos {h: 0, d: amount},
        _ => panic!("Unknown direction")
    }
}

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

fn day2p1() -> Result<i32, Error> {
    let f = File::open("./data/input2.txt");
    let br = BufReader::new(f.unwrap());

    let final_pos = br.lines().map(|item| parse_line(item)).fold(Pos{h:0,d:0}, |acc, x| acc + x);
    Ok(final_pos.h * final_pos.d)
}

fn main() -> () {
    println!("Day 1 part 1 result: {}", day1p1().unwrap());
    println!("Day 1 part 2 result: {}", day1p2().unwrap());
    println!("Day 2 part 1 result: {}", day2p1().unwrap());
}

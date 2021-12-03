use std::fs::File;
use std::io::{BufReader, Error};
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

pub fn result() -> Result<i32, Error> {
    let f = File::open("./data/input2.txt");
    let br = BufReader::new(f.unwrap());

    let final_pos = br.lines().map(|item| parse_line(item)).fold(Pos{h:0,d:0}, |acc, x| acc + x);
    Ok(final_pos.h * final_pos.d)
}

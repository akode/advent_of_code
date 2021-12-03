use std::fs::File;
use std::io::{BufReader, Error};
use std::io::prelude::*;
use std::ops;


enum Dir {
    Forward,
    Down,
    Up
}

struct Inst {
    dir: Dir,
    amount: i32
}

#[derive(Debug)]
struct Pos {
    h: i32,
    d: i32,
    a: i32
}

impl Pos {
    fn zero() -> Pos {
        Pos{h: 0, d: 0, a: 0}
    }
}

impl ops::Add<Inst> for Pos {
    type Output = Pos;
    fn add(self, rhs: Inst) -> Pos {
        match rhs.dir {
            Dir::Forward => Pos {
                h: self.h + rhs.amount,
                d: self.d + self.a*rhs.amount,
                a: self.a
            },
            Dir::Down => Pos {
                h: self.h,
                d: self.d,
                a: self.a + rhs.amount
            },
            Dir::Up => Pos {
                h: self.h,
                d: self.d,
                a: self.a - rhs.amount
            }
        }

    }
}

fn parse_line(line: std::io::Result<String>) -> Inst {
    let l = line.unwrap();
    let mut iter = l.split_whitespace();
    let dir = iter.next().unwrap().to_string();
    let amount = iter.next().unwrap().parse().unwrap();
    match dir.as_ref() {
        "forward" => Inst {dir: Dir::Forward, amount: amount},
        "up" => Inst {dir: Dir::Up, amount: amount},
        "down" => Inst {dir: Dir::Down, amount: amount},
        _ => panic!("Unknown direction")
    }
}

pub fn result() -> Result<i32, Error> {
    let f = File::open("./data/input2.txt");
    let br = BufReader::new(f.unwrap());

    let final_pos = br.lines().map(|item| parse_line(item)).fold(Pos::zero(), |acc, x| acc + x);
    Ok(final_pos.h * final_pos.d)
}

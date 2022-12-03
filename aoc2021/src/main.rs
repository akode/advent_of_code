mod day1;
mod day2;


fn main() -> () {
    println!("Day 1 part 1 result: {}", day1::p1().unwrap());
    println!("Day 1 part 2 result: {}", day1::p2().unwrap());
    println!("Day 2 part 1 result: {}", day2::p1::result().unwrap());
    println!("Day 2 part 2 result: {}", day2::p2::result().unwrap());
}

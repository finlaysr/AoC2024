use std::fs;

fn main() {
  // --snip--
  let file_path = "src/test.txt";
  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  let mut stones: Vec<i32> = contents
  .split(" ")
  .map(|s| s.parse::<i32>().unwrap())
  .collect();

  let mut new: Vec<i32>;
  for i in 0..75{
    print!("{i}: ");
    new = Vec::new();
    for s in &stones{
      if *s == 0 as i32{
        new.push(1)
      } else if s.to_string().len()%2 == 0 {
        let ss = s.to_string();
        let l = ss.len();
        new.push(ss[..l/2].parse::<i32>().unwrap());
        new.push(ss[l/2..].parse::<i32>().unwrap());
      } else {
        new.push(s*2024)
      }
    }
    stones = new.clone();
    //println!("{:?}", stones);
    println!("{}", stones.len());
  }

}
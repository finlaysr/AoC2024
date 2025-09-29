use std::fs;

fn main() {
    println!("Hello, world!");

    let file_path = "src/input.txt";
    let file = fs::read_to_string(file_path).expect("failed to read file");

    let data = file
        .trim()
        .split("\n")
        .collect::<Vec<&str>>()
        .iter()
        .map(|x| x.split(" ").map(|y| y.parse::<isize>().unwrap()).collect())
        .collect::<Vec<Vec<isize>>>();
    //println!("{:?}", data);

    let mut total = 0;
    for line in data {
        let mut valid = true;
        let increasing = line[1] > line[0];
        for x in 0..line.len() - 1 {
            let diff = if increasing {
                line[x + 1] - line[x]
            } else {
                line[x] - line[x + 1]
            };
            if !(diff >= 1 && diff <= 3) {
                valid = false;
            }
        }
        if valid {
            total += 1;
        }
    }
    println!("{total}")
}

use std::fs;

fn main() {
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
        if is_valid(&line) {
            total += 1;
        } else {
            let mut i = 0;
            let mut done = false;
            while i < line.len() && !done {
                let mut temp = line.clone();
                temp.remove(i);
                done = is_valid(&temp);
                if done {
                    total += 1;
                }
                i += 1;
            }
        }
    }
    println!("Answer: {total}");
}

fn is_valid(array: &Vec<isize>) -> bool {
    let mut valid = true;
    let increasing = array[1] > array[0];
    for x in 0..array.len() - 1 {
        let diff = if increasing {
            array[x + 1] - array[x]
        } else {
            array[x] - array[x + 1]
        };
        if !(diff >= 1 && diff <= 3) {
            valid = false;
        }
    }
    valid
}

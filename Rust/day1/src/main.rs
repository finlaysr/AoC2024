use std::fs;

fn main() {
    println!("Hello, world!");

    let file_path = "src/test.txt";
    let data = fs::read_to_string(file_path).expect("File should have been read");
    let data1: Vec<&str> = data.split("\r\n").collect();
    
    println!("{:?}", &data);

    pub fn print_message(message: String) {
        println!("{}", message)
    }



    //let data2: Vec<Vec<&str> = data.iter().map(|s| s.split(" ").collect()).collect();
    
    //println!("{:?}", &data2);
    //let data2: Vec<i32> = data.split("  ").map(|s| s.parse::<i32>().unwrap()).collect();
    //println!("{:?}", data2);

    let mut line1: Vec<i32>;
    let mut line2: Vec<i32>;


}

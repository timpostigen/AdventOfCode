use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;

pub fn day_1(a: i32, b: i32) -> i32 {
    a + b
}

pub fn read_file(path: &Path) -> std::io::Result<String> {
	let file = File::open(path)?;
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents)?;

	Ok(contents)
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_day_1() {
        assert_eq!(day_1(1, 2), 3);
    }
}

fn main(){
	let path = Path::new("./day_1.txt");
    let age_result = read_file(path);

    if let Ok(description) = &age_result {
        println!("{}", description);
    }
}

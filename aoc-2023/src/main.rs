use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;

// trivial to use map reduce after structuring the data then sort
pub fn day_1(calibration_document: &String) -> i32 {
	let calibration_lines = calibration_document.lines();

	// https://rust-lang-nursery.github.io/rust-cookbook/concurrency/parallel.html
	// https://github.com/nikomatsakis

	let mut affixes_sum = 0;

	for calibration_line in calibration_lines {
		println!("{calibration_line}");

		affixes_sum += 1;
	}

	return affixes_sum;
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
		let path = Path::new("./data/day_1_example.txt");
    	let result = read_file(path);

		if let Ok(contents) = &result {
			assert_eq!(day_1(contents), 24000);
		}
	}
}

fn main(){
	// Day 1
	let path = Path::new("./data/day_1_example.txt");
	let result = read_file(path);

	if let Ok(contents) = &result {
		let sum = day_1(contents);
		println!("{sum}");
	}
}

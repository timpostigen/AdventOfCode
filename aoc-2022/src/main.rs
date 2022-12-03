use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;

// trivial to use map reduce after structuring the data then sort
pub fn day_1(rough_food_list: &String) -> i32 {
	let food_list = rough_food_list.lines();

	let mut elf_calories = 0;
	let mut most_calories = vec![1, 2, 3];

	for food_item_calories in food_list {
		let calories = food_item_calories.trim();

		if calories.is_empty() {
			for total in most_calories.iter() {
				if elf_calories > *total {
					most_calories.push(elf_calories);
					most_calories.sort_unstable();
					most_calories.reverse();
					most_calories.pop();

					break;
				}
			}
			
			elf_calories = 0;
			continue;
		}

		elf_calories += calories.trim().parse::<i32>().unwrap();	
	}

	most_calories.iter().sum()
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
	let path = Path::new("./data/day_1_input.txt");
	let result = read_file(path);

	if let Ok(contents) = &result {
		let max = day_1(contents);
		println!("{max}");
	}
}

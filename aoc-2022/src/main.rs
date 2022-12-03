use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;

pub fn day_1(food_list: &String) -> i32 {
	let mut elf_inventories = food_list.split("\n\n");
	let mut most_calories = -1;

	for elf_inventory in elf_inventories {
		let mut food_items = elf_inventory.split("\n");

		let mut elf_calories = 0;
		
		for calories in food_items {
			print!("{calories}");
			elf_calories += calories.parse::<i32>().unwrap();

			if elf_calories > most_calories {
				most_calories = elf_calories;
			}
		}

	}

	most_calories
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
		let path = Path::new("./day_1.txt");
    	let result = read_file(path);

		if let Ok(contents) = &result {
			assert_eq!(day_1(contents), 24000);
		}
	}
}

fn main(){
	println!("Add call.")
}

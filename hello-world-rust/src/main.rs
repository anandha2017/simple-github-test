// fn main() {
//     println!("Hello, world!");
// }


//write a function that takes a string and returns the first word it finds in that string. If the function doesn’t find a space in the string, the whole string must be one word, so the entire string should be returned.
// Path: src/main.rs

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() { //enumerate returns a tuple
        if item == b' ' { //b' ' is byte literal syntax
            return &s[0..i]; //return a slice
        }
    }
    &s[..] //return a slice
}

// Path: src/main.rs
fn main() {
    let mut s = String::from("hello world");
    let word = first_word(&s); //word will get the value 5
    s.clear(); //this empties the String, making it equal to ""
    println!("the first word is: {}", word);
}

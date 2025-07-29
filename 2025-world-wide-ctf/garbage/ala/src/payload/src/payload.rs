use magic::magic;
use magic::address_of_return_address;

fn clear_value<T>(x: &mut Vec<T>) {
    let _ = std::mem::take(x); // x is now an empty String
}

pub fn payload() {
    let mut x = 0x69;
    let (a, b) = magic(&mut x);
    
    
    let (d, c) = magic(a);




    // ret addr
    let addr = address_of_return_address!();
    


}   


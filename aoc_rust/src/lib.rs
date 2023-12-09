pub fn add(left: usize, right: usize) -> usize {
    left + right
}

pub fn day1() -> u32{
    let s = include_str!("../input/day1.input");
    let mut sum = 0;
    for line in s.lines(){
        let mut l_found = false;
        let mut r_found = false;
        for (l,r) in line.chars().zip(line.chars().rev()){
            if l.is_numeric() && !l_found {
                sum += 10*l.to_digit(10).unwrap();
                l_found = true;
            }
            if r.is_numeric() && !r_found {
                sum += r.to_digit(10).unwrap();
                r_found = true;
            }
        }
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}

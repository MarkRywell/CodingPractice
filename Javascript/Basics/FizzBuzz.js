for(let i = 0; i <= 100; i++) {

    let out = "";
    
    if(i % 3 == 0 && i % 5 == 0)
        out += "FizzBuzz"
    if(i % 3 == 0)
        out += "Fizz"
    if(i % 5 == 0) 
        out += "Buzz"
    if(i % 7 == 0)
        out += "Bazz"
    

    console.log(out || i);
}
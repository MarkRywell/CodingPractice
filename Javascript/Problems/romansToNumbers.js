// Convert Romans to Numbers

const romansToNumber = (input) => {
    const romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M':1000
    }

    const splitInput = input.split('');
    let value = 0;
    let romanValue = '';

    for(let roman of splitInput) {
        
        if(romanValue == '') {
            value += romans[roman];
            romanValue = roman;
            continue;
        };
        if(romans[roman] <= romans[romanValue]) {
            value+=romans[roman];
        }
        else {
            value = (value - romans[romanValue]) + (romans[roman] - romans[romanValue]);
        }
        romanValue = roman;
    }
    return value;
}

console.log(romansToNumber('CDXIV'))




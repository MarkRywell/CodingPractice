// Convert Romans to Numbers

const romansToNumber1 = (input) => {
    const romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    let value = 0;

    for(let x = 0; x < input.length; x ++) {        
        if(romans[input[x]] > 0 && romans[input[x]] > romans[input[x - 1]]) {
            value += romans[input[x]] - (romans[input[x - 1]] * 2);
        }
        else {
            value += romans[input[x]]
        }
    }
    return value;
}

const romansToNumber2 = (input) => {
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

console.log(romansToNumber1('CDXIV')) // 414
console.log(romansToNumber2('CDXIV')) // 414
console.log(romansToNumber1('CLI')) // 151
console.log(romansToNumber2('CLI')) // 151
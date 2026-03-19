/**
 * 
 * 
 Evaluate mathematical expressions written in English words.

Input: A string containing a math expression in English words

Output: A number result, or null if the input cannot be evaluated
 */



const evaluate = (input) => {

    const numberMap = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'dozen': 12,
        'score': 20
    }

    const scalesMap = {
        'hundred': 100,
        'thousand': 1000,
    }

    const operatorMap = {
        'plus': '+',
        'minus': '-',
        'times': '*',
        'divided_by': '/',
        'multiplied_by': '*',
        'and': '+'
    }

    const multiWordOperators = ["divided by", "multiplied by"];
    
    let tokens = input.toLowerCase().replace(/-/g, ' ');

    multiWordOperators.forEach(op => {
        const regex = new RegExp(op, "g");
        tokens = tokens.replace(regex, op.replace(' ', '_'));
    });

    tokens = tokens.split(' ').filter(Boolean);

    const parseNumber = (tokens, startIndex) => {
        let numericValue = 0;
        let nextIndex;
        let currentValue = 0;
        let isNegative = false;

        if (["negative", "minus"].includes(tokens[startIndex])) {
            isNegative = true;
            startIndex++;
        }

        for(let i = startIndex; i < tokens.length;) {
            nextIndex = i + 1;
            
            if (tokens[i] in numberMap) {
                currentValue += numberMap[tokens[i]]
            }
            else if (scalesMap.hasOwnProperty(tokens[i])) {
                if (tokens[i] === "hundred") {
                    currentValue = currentValue || 1;
                    currentValue *= 100;
                } else if (tokens[i] === "thousand") {
                    currentValue = currentValue || 1;
                    currentValue *= 1000;
                    numericValue += currentValue;
                    currentValue = 0;
                }
            }
            else if (tokens[i] == "and") {
                continue;
            }
            else {
                break;
            }
        }

        numericValue += currentValue;

        if (isNegative) {
            numericValue *= -1
        }

        return { numericValue, nextIndex }
    }

    let result = null;;
    let currentOperator = null;

    for (let i = 0; i < tokens.length; i++) {
        console.log(tokens[i]);

        let prefixMultipler = 1;

        if (tokens[i] == 'half' && tokens[i + 1] == 'of') {
            prefixMultipler = 0.5;
            i += 2
        } else if (tokens[i] == 'double') {
            prefixMultipler = 2;
            i++
        } else if (tokens[i] == 'percent' && tokens[i + 1] == 'of') {
            prefixMultipler = 0.01;
            i += 2
        }

        let { numericValue, nextIndex } = parseNumber(tokens, i);

        numericValue *= prefixMultipler;

        
        if (result === null) {
            result = numericValue;
        } else if (currentOperator) {
            switch(currentOperator) {
                case '+':
                    result += numericValue;
                    break;
                case '-':
                    result -= numericValue;
                    break;
                case '*':
                    result *= numericValue;
                    break;
                case '/':
                    result /= numericValue;
                    break;
            }
        }
        

        i = nextIndex;


        if (i < tokens.length) {
            if (tokens[i] === "and") {
                currentOperator = '+';
                i += 1;
            } else if (operatorMap.hasOwnProperty(tokens[i])) {
                currentOperator = operatorMap[tokens[i]];
                i += 1;
            }
        }
    }

    console.log(result);

}

evaluate('five hundred fifty eight plus two dozen')
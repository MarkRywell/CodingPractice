/* 
You will be given a string of English digits "stuck" together, like this:
zeronineoneoneeighttwoseventhreesixfourtwofive
Your task is to split the string into separate digits:
zero nine one one eight two seven three six four two five

*/

const collapse = (digits) => {
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    const splitDigits = digits.split('');
    let collapsed = "";

    let word = "";

    for(let digit of splitDigits) {
        
        word+=digit;
        if(numbers.includes(word)) {
            collapsed += `${word} `;
            word = "";
        }
    }

    collapsed = collapsed.replace(/\s$/, '');
    return collapsed;
}

console.log(collapse("fivethreefivesixthreenineonesevenoneeight"))

/*
The main idea is to count all the occurring characters in a string. If you have a string like aba, 
then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
*/

function count(string) {
    let counts = {}
    if(string == '') return counts;
    for(let letter of string) {
        counts.hasOwnProperty(letter) ? counts[letter] += 1 : counts = { ...counts, [letter]: 1 }        
    }
    return counts;
}

console.log(count('wtsdas'))


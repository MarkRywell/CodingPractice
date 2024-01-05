/*
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
*/

function solution(str){
    const splittedStrings = [];
    for(let index in str) {
        if(index % 2 == 1) splittedStrings.push(`${str[index - 1]}${str[index]}`)
        if(str.length - 1 == index && index % 2 == 0) splittedStrings.push(`${str[index]}_`)
    }
    return splittedStrings;
}

solution("hello")
// Create a function that will count and return the number of vowels in a given string;

function getCount(str) {
    const vowels = 'aeiou';
    let count = 0;
    str.split('').forEach((letter) => {
      if(vowels.includes(letter)) count++;
    })
    return count;
}
// Write a function that takes an array of numbers (integers for the tests) 
// and a target number. It should find two different items in the array that, when added together, 
// give the target value. The indices of these items should then be returned in a tuple / list 
// (depending on your language) like so: (index1, index2).

const twoSum = (numbers, target) => {
    const indeces = [];
    for(let i = 0; i <= numbers.length; i++) {
        for(let j = i + 1; j <= numbers.length; j++) {
            if(numbers[i] != numbers[j]) {
                if(numbers[i] + numbers[j] == target) indeces.push([i, j])
            }
        }
    }

    return indeces;
}

console.log(twoSum([1, 2, 3], 4))
// Complete the square sum function so that it squares each number passed into it and then sums the results together.

function squareSum(numbers){
    let sum = 0;
    if(numbers.length == 0) return 0;
    numbers.forEach((number) => sum += number ** 2)
    return sum;
  }
  
squareSum([1, 2, 2])
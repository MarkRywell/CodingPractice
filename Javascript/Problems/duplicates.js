// Return true if there is a duplicate and false if there isnt

function containsDuplicate (nums) {
    const numbers = [];
    for(let i = 0; i < nums.length; i++) {
     if(i == 0) {
         numbers.push(nums[i]);
         continue;
     }
     if(numbers.includes(nums[i])) return true;
     numbers.push(nums[i]);
    }
    return false;
 }
 
 function containsDuplicate1 (nums) {
     for(let i = 0; i < nums.length; i++) {
         for(let j = i + 1; j < nums.length; j++) {
             if(nums[i] == nums[j]) return true;
         }
     }
     return false;
 }
 
 console.log(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 14, 45, 46, 47, 48, 49, 50]))
 console.log(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]))
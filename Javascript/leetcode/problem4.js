/**
 * Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 * 
 * Example 1:

    Input: nums = [1,2,3,1]

    Output: true

    Explanation:

    The element 1 occurs at the indices 0 and 3.
 */


const nums = [1,1,2,4]

const containsDuplicate = (nums) => {
    const counter = {}
    let hasDuplicate = false;

    for (let num of nums) {
        counter[num] = (counter[num] || 0) + 1;

        if (counter[num] > 1) {
            hasDuplicate = true;
            break;
        }
    }
    return hasDuplicate
}

console.log(containsDuplicate(nums))
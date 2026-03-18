/**
 * 
Two Sum (Easy / Medium)

Problem

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation: nums[0] + nums[1] = 2 + 7 = 9
 */


const twoSum = (nums, target) => {
    
    for(let i = 0; i < nums.length; i++) {
        for(let j = 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j]
            }
        }
    }
    return "No match"
}

const twoSumOptimized = (nums, target) => {
    const map = new Map();

    for(let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];

        if (map.has(complement)) {
            return [map.get(complement), i];
        }

        map.set(nums[i], i);
    }

    return "No match"
}

const nums = [2,7,11,15]
const target = 26
console.log(twoSumOptimized(nums, target))
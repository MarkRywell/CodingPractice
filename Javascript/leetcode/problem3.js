/**
 * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 * 
 * Example 1:

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
 */

const nums = [0,1,2,3,4,5, 6, 7, 8]

const rotate = (nums, k) => {

    n = nums.length;

    if (n == 0) return;
    console.log("Input K: ", k, " - Input N: ", n)
    k = k % n;
    console.log("Updated K: ", k)

    if (k == 0) return;

    const reverse = (start, end) => {
        while (start < end) {
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++;
            end--;
        }
    }

    reverse(0, n - 1)
    console.log(nums, "Reverse whole array")
    reverse(0, k - 1)
    console.log(nums, "Reverse Selected elements")
    reverse(k, n - 1)
    console.log(nums, "Reverse Remaining elements")
    
}

rotate(nums, 2)

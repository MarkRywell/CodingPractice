const search = (arr, target) => {
    let left = 0;
    let right = arr.length - 1;

    while(left <= right) {
        const mid = Math.floor((left + right) / 2);

        console.log(`left ${left} - mid ${mid} - right ${right}`);

        if(arr[mid] == target) {
            return mid;
        }
        else if(target < arr[mid]) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    return null;
}

const array = [2, 3, 5, 8, 10, 13, 15];

const target = 5;

console.log(search(array, target));
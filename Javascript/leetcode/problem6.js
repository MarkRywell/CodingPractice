/**
 * Fibonacci Sequence
 */


/**
 * Generates a list of fibonacci sequence until end sequence value is not less than input end
 * @param {*} end 
 * @returns sequence
 */
const fibonacciSequence = (end) => {
    if (end == 0) return [end];
    if (end == 1) return [0, end];

    const sequence = [0, 1]
    while((sequence[sequence.length - 1] + sequence[sequence.length - 2]) < end) {
        sequence.push(sequence[sequence.length - 1] + sequence[sequence.length - 2])
    }

    return sequence
}

/**
 * Generates fibonacci sequence with exactly n terms
 * @param {*} n 
 * @returns sequence
 */
const fibonacciSequenceTerms = (n) => {
    if (n == 0) return [];
    if (n == 1) return [n];

    const sequence = [0, 1];
    while(sequence.length != n) {
        sequence.push(sequence[sequence.length - 1] + sequence[sequence.length - 2])
    }

    return sequence
}

/**
 * Returns the fibonnaci nth term value
 * @param {*} n 
 * @returns term value
 */
const fibonacciTermValue = (n) => {
    if (n == 0 || n == 1) return n;

    const sequence = [0, 1];

    while(sequence.length < n) {
        sequence.push(sequence[sequence.length - 1] + sequence[sequence.length - 2])
    }

    return sequence[sequence.length - 1]
}

const fibonacciTermValueOptimized = (n) => {
    if (n <= 1) return n;

    let first = 1;
    let second = 1;

    for(let i = 2; i < n; i++) {
        let current = first + second;

        first = second;
        second = current;
    }

    return second
}

const checkIfPrimeNumber = (n) => {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for(let i = 3; i * i <= n; i++) {
        if (n % i == 0) {
            return false
        }
    }

    return true
}

console.log(fibonacciTermValue(5))
console.log(fibonacciTermValueOptimized(5))
// fibonacciTermValueOptimized(5)

const stepsCombinationArray = (n) => {
    const dp = Array(n + 1).fill(0)

    dp[0] = 1;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }
    return dp[n]
}

const stepsCombinationNum = (n) => {
    if (n <= 1) return 1;

    let first = 1;
    let second = 1;

    for (let i = 2; i <= n; i++) {
        let current = first + second;
        first = second;
        second = current;
    }

    return second
}

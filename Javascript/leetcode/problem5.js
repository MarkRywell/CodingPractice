/**
 * Palindrome String, Number
 */

const validatePalindromeString = (s) => {
    const formattedString = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase()

    const reverseString = formattedString.split("").reverse().join("")

    return formattedString == reverseString
} 


const validatePalindromeNumber = (x) => {

    const reversedNumber = x.toString().split("").reverse().join("")

    return x == Number(reversedNumber)
}
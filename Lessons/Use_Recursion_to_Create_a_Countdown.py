function countdown(n) {
  // Base case: If n is less than 1, return an empty array
  if (n < 1) {
    return [];
  } else {
    // Recursive case: Call the countdown function with n - 1
    const countArray = countdown(n - 1);
    // Add the current value of n to the array
    countArray.unshift(n); // Use unshift to add 'n' to the beginning of the array
    return countArray;
  }
}

console.log(countdown(10)); // Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

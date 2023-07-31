function rangeOfNumbers(startNum, endNum) {
  // Base case: If startNum is greater than endNum, return an empty array
  if (startNum > endNum) {
    return [];
  } else {
    // Recursive case: Call the rangeOfNumbers function with endNum - 1
    const rangeArray = rangeOfNumbers(startNum, endNum - 1);
    // Add the current value of endNum to the array
    rangeArray.push(endNum);
    return rangeArray;
  }
}

// Test the function with startNum = 1 and endNum = 4
console.log(rangeOfNumbers(1, 4));

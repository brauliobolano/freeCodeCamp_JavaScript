//One way to do it
function randomRange(myMin, myMax) {
  return Math.floor(Math.random()* (myMax - myMin +1) + myMin);
}
console.log(randomRange(5, 9))

/* Another Way to do it
function randomRange(myMin, myMax) {
  // Generate a random decimal between 0 (inclusive) and 1 (exclusive)
  const randomDecimal = Math.random();

  // Scale and shift the decimal to fit the desired range
  const randomNumber = Math.floor(randomDecimal * (myMax - myMin + 1)) + myMin;

  return randomNumber;
}
*/

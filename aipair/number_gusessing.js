// Number guessing game
// Use HTML form to take input from user and display output
// Use JavaScript to handle the game logic
// Write JavaScript here and create another HTML file number_guessing.html

let randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
function guessNumber() {
    const userGuess = parseInt(document.getElementById("userGuess").value);
    attempts++;
    
    if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
        document.getElementById("result").innerText = "Please enter a valid number between 1 and 100.";
        return;
    }

    if (userGuess < randomNumber) {
        document.getElementById("result").innerText = "Too low! Try again.";
    } else if (userGuess > randomNumber) {
        document.getElementById("result").innerText = "Too high! Try again.";
    } else {
        document.getElementById("result").innerText = `Congratulations! You've guessed the number ${randomNumber} in ${attempts} attempts.`;
    }
}



document.getElementById("quiz-form").addEventListener("submit", function(e) {
    e.preventDefault(); // Prevent form from submitting and page reload

    let isValid = true;
    const questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6','q7',];

    // Validate that all questions are answered
    questions.forEach(question => {
        const selectedOption = document.querySelector(`input[name="${question}"]:checked`);
        if (!selectedOption) {
            isValid = false;
            alert(`Please answer question ${question.charAt(1)}`);
        }
    });

    if (isValid) {
        // Disable the submit button while fetching the character
        document.getElementById("submit-button").disabled = true;

        fetch('/random-character')
            .then(response => response.json())
            .then(data => {
                // Display the result dynamically
                const resultDiv = document.getElementById("result");
                resultDiv.innerHTML = `
                    <h2>You are: ${data.character}</h2>
                    <img src="${data.image}" alt="${data.character}" style="width: 200px; border-radius: 10px; border: 2px solid #ffcc00;">
                    <br>
                    <button onclick="resetQuiz()">Try Again</button>
                    <br><br><a href="/">Back to Home</a>
                `;
            });
    }
});

function resetQuiz() {
    // Reset the form and make the submit button active again
    document.getElementById("quiz-form").reset();
    document.getElementById("submit-button").disabled = false;
    document.getElementById("result").innerHTML = ''; // Clear the result div
}

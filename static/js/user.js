document.addEventListener('DOMContentLoaded', () => {
    const questions = document.querySelectorAll('.question');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const submitButton = document.getElementById('submit');
    let currentQuestionIndex = 0;

    // Function to show the current question
    function showQuestion(index) {
        questions.forEach((question, i) => {
            question.style.display = i === index ? 'block' : 'none';
        });

        // Update button visibility
        prevButton.style.display = index === 0 ? 'none' : 'inline-block';
        nextButton.style.display = index === questions.length - 1 ? 'none' : 'inline-block';
        submitButton.style.display = index === questions.length - 1 ? 'inline-block' : 'none';
    }

    // Event listeners for navigation buttons
    nextButton.addEventListener('click', () => {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            showQuestion(currentQuestionIndex);
        }
    });

    prevButton.addEventListener('click', () => {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            showQuestion(currentQuestionIndex);
        }
    });

    // Initialize by showing the first question
    showQuestion(currentQuestionIndex);
});

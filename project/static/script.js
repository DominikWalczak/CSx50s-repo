const questions = [
    {
        question: "What kind of person are you?",
        answers: [
            { text: "Lazy", correct: true },
            { text: "Energetic", correct: true },
            { text: "Boring", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "Do you love anyone?",
        answers: [
            { text: "Yes", correct: true },
            { text: "No", correct: true },
            { text: "I love capybaras", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "What kind of food do you prefer?",
        answers: [
            { text: "Fruits", correct: true },
            { text: "Veggies🤮", correct: true },
            { text: "Meat", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "What kind of sentence do you hear the most from the others?",
        answers: [
            { text: "You are fat bro", correct: true },
            { text: "It's to late for treatment", correct: true },
            { text: "You do be really capybara lookin today", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "What's your favorite animal?",
        answers: [
            { text: "Dog", correct: true },
            { text: "Cat", correct: true },
            { text: "Lion", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "Which one are you?",
        answers: [
            { text: "Introvert", correct: true },
            { text: "Extrovert", correct: true },
            { text: "Ambivert", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "Where do u live?",
        answers: [
            { text: "Europe/Americas", correct: true },
            { text: "Africa/Asia", correct: true },
            { text: "Australia", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "Which movie series would u choose?",
        answers: [
            { text: "Pirates of the Caribbean", correct: true },
            { text: "Harry Potter", correct: true },
            { text: "John Wick", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "Who is your favorite actor/idol",
        answers: [
            { text: "Keanu Reeves", correct: true },
            { text: "Johhny Deep", correct: true },
            { text: "Amber Heard🤮", correct: true },
            { text: "Capybara", correct: true },
        ]
    },
    {
        question: "Which of these dishes would u choose",
        answers: [
            { text: "Lasagne", correct: true },
            { text: "Sushi", correct: true },
            { text: "Pizza", correct: true },
            { text: "Capybara", correct: true },
        ]
    }
];


var a = 0;
var b = 0;
var c = 0;
var d = 0;
var sum = 0;

const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btnd");

let currentQuestionIndex = 0;
let score = 0;

function startQuiz(){
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHTML = "Next";
    showQuestion();
}
function CapyType(clickedButtonId){
    console.log("clickedButtonId:", clickedButtonId);
    if(clickedButtonId === 'a')
    {
        a++;
        sum++;
    }
    else if(clickedButtonId === 'b')
    {
        b++;
        sum++;
    }
    else if(clickedButtonId === 'c')
    {
        c++;
        sum++;
    }
    else if(clickedButtonId === 'd')
    {
        d++;
        sum++;

    }
    else if(sum === 10)
    {
        if(d === 10)
        {
            return 25;
        }
        else if(a >= b && a >= c && a >= d)
        {
            if(b >= c && b >= d)
            {
                if(c > d)
                {
                    return 1;
                }
                else
                {
                    return 2;
                }
            }
            else if(c >= b && c >= d)
            {
                if(b > d)
                {
                    return 3;
                }
                else
                {
                    return 4;
                }
            }
            else if(d >= b && d >= c)
            {
                if(b >= c)
                {
                    return 5;
                }
                else
                {
                    return 6;
                }
            }

        }
        else if(b >= a && b >= c && b >= d)
        {
            if(a >= c && a >= d)
            {
                if(c > d)
                {
                    return 7;
                }
                else
                {
                    return 8;
                }
            }
            else if(c >= a && c >= d)
            {
                if(a > d)
                {
                    return 9;
                }
                else
                {
                    return 10;
                }
            }
            else if(d >= a && d >= c)
            {
                if(a > c)
                {
                    return 11;
                }
                else
                {
                    return 12;
                }
            }
        }
        else if(c >= a && c >= b && c >= d)
        {
            if(a >= b && a >= d)
            {
                if(b > d)
                {
                    return 13;
                }
                else
                {
                    return 14;
                }
            }
            else if(b >= a && b >= d)
            {
                if(a > d)
                {
                    return 15;
                }
                else
                {
                    return 16;
                }
            }
            else if(d >= a && d >= b)
            {
                if(a > b)
                {
                    return 17;
                }
                else
                {
                    return 18;
                }
            }
        }
        else if(d >= a && d >= b && d >= c)
        {
            if(a >= b && a >= c)
            {
                if(b > c)
                {
                    return 19;
                }
                else
                {
                    return 20;
                }
            }
            else if(b >= a && b >= c)
            {
                if(a > c)
                {
                    return 21;
                }
                else
                {
                    return 22;
                }
            }
            else if(c >= a && c >= b)
            {
                if(a > b)
                {
                    return 23;
                }
                else
                {
                    return 24;
                }
            }
        }
    }
    else{
        return 26;
    }
}

function showQuestion(){
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex + 1;
    questionElement.innerHTML = questionNo + ". " + currentQuestion.
    question;

    const letters = ['a', 'b', 'c', 'd'];

    currentQuestion.answers.forEach((answer, index) => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btnd");
        button.id = letters[index];
        answerButtons.appendChild(button);
        button.addEventListener("click", selectAnswer);
        if(answer.correct){
            button.dataset.correct = answer.correct;
        }
    });
}


function resetState(){
    nextButton.style.display = "none";
    while(answerButtons.firstChild){
        answerButtons.removeChild(answerButtons.firstChild);
    }
}

function selectAnswer(e){
    const selectedBtn = e.target;
    const selectedBtnId = selectedBtn.id;
    CapyType(selectedBtnId);
    const isCorrect = selectedBtn.dataset.correct === "true";
    if(isCorrect){
        selectedBtn.classList.add("selected");

        }
    Array.from(answerButtons.children).forEach(button => {
        button.disabled = true;
    });
    nextButton.style.display = "block";
}

function showCapytype(){
    resetState();
    questionElement.innerHTML = `Check what kind of caypbara are you!`;
    nextButton.innerHTML = "Click here to check your capybara type!";
    nextButton.style.display = "block";

    nextButton.addEventListener("click", function (event) {
        var capybaraType = CapyType(event);
        console.log("capybaraType:", capybaraType);
        window.location.href = "/answer?type=" + encodeURIComponent(capybaraType);
    });
}

function handleNextButton(){
    currentQuestionIndex++;
    if(currentQuestionIndex < questions.length){
        showQuestion();
    }else{
        showCapytype();
    }
}

nextButton.addEventListener("click", ()=>{
    if(currentQuestionIndex < questions.length){
        handleNextButton();
    }
});
startQuiz();

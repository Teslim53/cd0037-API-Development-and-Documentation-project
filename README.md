# API Development and Documentation Final Project

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.

# API DOCUMENTATION
## INTRODUCTION
The Trivia API allows clients to view categories of questions, view questions(max. of 10 per page) post new
questions and so much more(more details in the endpoints' section)

## ENDPOINTS
### GET '/categories'
>Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
>Request Arguments: None
>Returns: An object with a single key, categories, that contains an object of id: category_string key: value pairs.

Example:
{"categories":[{"id":1,"type":"Science"},{"id":2,"type":"Art"},{"id":3,"type":"Geography"},{"id":4,"type":"History"},
{"id":5,"type":"Entertainment"},{"id":6,"type":"Sports"}],"success":true}

### GET '/questions'
>Fetches a dictionary of questions in which the keys are the ids and the value is the corresponding string of the question
>Request Arguments: None
>Returns: An object with a single key, questions, that contain an object of id: _string key: value pairs.

Example:
{"categories":[{"id":1,"type":"Science"},{"id":2,"type":"Art"},{"id":3,"type":"Geography"},{"id":4,"type":"History"},
{"id":5,"type":"Entertainment"},{"id":6,"type":"Sports"}],"current_category":"nil",
"questions":[{"answer":"Apollo 13","category":5,"difficulty":4,"id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},
{"answer":"Tom Cruise","category":5,"difficulty":4,"id":4,"question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},{"answer":"Maya Angelou","category":4,"difficulty":2,"id":5,"question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"},{"answer":"Edward Scissorhands","category":5,"difficulty":3,"id":6,"question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"},{"answer":"Muhammad Ali","category":4,"difficulty":1,"id":9,"question":"What boxer's original name is Cassius Clay?"},{"answer":"Brazil","category":6,"difficulty":3,"id":10,"question":"Which is the only team to play in every soccer World Cup tournament?"},{"answer":"Uruguay","category":6,"difficulty":4,"id":11,"question":"Which country won the first ever soccer World Cup in 1930?"},{"answer":"George Washington Carver","category":4,"difficulty":2,"id":12,"question":"Who invented Peanut Butter?"},{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"}],"success":true,"total_questions":19}

### GET '/questions?page=${integer}'
>Fetches a paginated set of questions, a total number of questions, all categories and current category string.
Request Arguments: page - integer
Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string

{"categories":[{"id":1,"type":"Science"},{"id":2,"type":"Art"},{"id":3,"type":"Geography"},{"id":4,"type":"History"},
{"id":5,"type":"Entertainment"},{"id":6,"type":"Sports"}],"current_category":"nil","questions":
[{"answer":"Agra","category":3,"difficulty":2,"id":15,"question":"The Taj Mahal is located in which Indian city?"},
{"answer":"Escher","category":2,"difficulty":1,"id":16,"question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"},{"answer":"Mona Lisa","category":2,"difficulty":3,"id":17,"question":"La Giaconda is better known as what?"},{"answer":"One","category":2,"difficulty":4,"id":18,"question":"How many paintings did Van Gogh sell in his lifetime?"},{"answer":"Jackson Pollock","category":2,"difficulty":2,"id":19,"question":"Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"},{"answer":"The Liver","category":1,"difficulty":4,"id":20,"question":"What is the heaviest organ in the human body?"},{"answer":"Alexander Fleming","category":1,"difficulty":3,"id":21,"question":"Who discovered penicillin?"},{"answer":"Blood","category":1,"difficulty":4,"id":22,"question":"Hematology is a branch of medicine involving the study of what?"},{"answer":"Scarab","category":4,"difficulty":4,"id":23,"question":"Which dung beetle was worshipped by the ancient Egyptians?"}],"success":true,"total_questions":19}




### GET '/categories/${id}/questions'
>Fetch questions for a cateogry specified by id request argument
Request Arguments: id - integer
Returns: An object with questions for the specified category, total questions, and current category string


{
    {"current_category":"Science","questions":[{"answer":"The Liver","category":1,"difficulty":4,"id":20,"question":"What is the heaviest organ in the human body?"},{"answer":"Alexander Fleming","category":1,"difficulty":3,"id":21,"question":"Who discovered penicillin?"},{"answer":"Blood","category":1,"difficulty":4,"id":22,"question":"Hematology is a branch of medicine involving the study of what?"}],"success":true,"total_questions":3}
}


### DELETE '/questions/${id}'
>Deletes a specified question using the id of the question
Request Arguments: id - integer
Returns:{"success":True}


### POST '/quizzes'
>Sends a post request in order to get the next question
Request Body:

Example:
{
    'previous_questions': [1, 4, 20, 15]
    quiz_category': 'current category'
 }
Returns: a single random question object in current category if provided
{
    'question': {
        'id': 1,
        'question': 'This is a question',
        'answer': 'This is an answer',
        'difficulty': 5,
        'category': 4
    }
}
### POST '/questions'
>Sends a post request in order to add a new question
Request Body:

Example:
{
    'question':  'A new question string',
    'answer':  'An answer string',
    'difficulty': 3,
    'category': 1,
}
Returns: Does not return any new data


### POST '/questions'
>Sends a post request in order to search for a specific question by search term(search is case-insensitive)
Request Body:
{
    'searchTerm': 'A set of characters'
} Returns: any array of questions, a number of totalQuestions that met the search term and the current category string

Example:
{
    'questions': [
        {
            'id': 1,
            'question': 'A question',
            'answer': 'An answer to the above question',
            'difficulty': 4,
            'category': 1
        },
    ],
    'totalQuestions': 19,
    'currentCategory': 'Science'
}

## ERROR HANDLING
This Trivia API handles errors gracefully and displays them in JSON format.

### ERRORS
>The errors that are returned when something goes wrong with the API are:
* 400(Bad request)
* 404(Not Found)
* 405(Method not allowed)
* 422(Unprocessable)
* 500(Internal Server error)

>Generally, errors are returned in this form:
{"error":<error_code>,
"message":"<error_message>,
"success":false}





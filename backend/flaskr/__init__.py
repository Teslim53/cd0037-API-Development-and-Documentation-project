from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random
import sys
from models import setup_db, Question, Category

sys.path.append(".")
print(sys.path)


QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """

    # This returns all available categories
    # (showing their id and type)
    @app.route('/categories', methods=['GET'])
    def show_categories():
        try:
            raw_categories = Category.query.all()
            if len(raw_categories) == 0:
                # if no category is in database a friendly
                # error message is shown to the user
                abort(404)
            categories_dic = {}
            for item in raw_categories:
                categories_dic[item.id] = item.type
            print(categories_dic)
            return jsonify({
                "success": True,
                "categories": categories_dic
            })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    # This route returns a list of ten questions
    # per page(organized in ascending order by question id)
    @app.route('/questions', methods=['GET'])
    def show_questions():
        try:
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * QUESTIONS_PER_PAGE
            end = start + QUESTIONS_PER_PAGE
            questions = Question.query.order_by(Question.id).all()
            if len(questions) == 0:
                abort(404)
            else:
                formatted_questions = [item.format() for item in questions]
                # current_category = [item.category() for item in questions]
                raw_categories = Category.query.all()
                categories = [item.format() for item in raw_categories]
                return jsonify({
                    "success": True,
                    "questions": formatted_questions[start:end],
                    "total_questions": len(questions),
                    "current_category": "All categories",
                    "categories": categories
                })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    # This endpoint deletes a specific question (by its id)
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        try:
            specific_question = Question.query.filter(Question.id == id).one_or_none()
            if specific_question is None:
                abort(404)
            else:
                specific_question.delete()
            return jsonify({
                "success": True
            })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    # To create a new question
    @app.route('/questions', methods=['POST'])
    def create_question():
        try:
            # get data from frontend
            body = request.get_json()
            question = body.get('question')
            answer = body.get('answer')
            difficulty = body.get('difficulty')
            category = body.get('category')
            # use data from frontend to create a new question
            new_question = Question(question=question, answer=answer, difficulty=difficulty, category=category)
            new_question.insert()
            return jsonify({
                "success": True
            })
        except:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    # This endpoint searches for questions
    # (case insensitive)
    @app.route('/questions/search', methods=['POST'])
    def search_question():
        try:
            body = request.get_json()
            search_term = body.get('search')
            print('search_term ' + search_term)
            search_result = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
            questions = [item.format() for item in search_result]
            return jsonify({
                "success": True,
                "questions": questions,
                "total_questions": len(Question.query.all()),
                "current_category": 'All Categories'

            })
        except:
            abort(422)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route('/categories/<int:id>/questions', methods=['GET'])
    def questions_by_category(id):
        try:
            raw_questions = Question.query.filter(Question.category == id).order_by(Question.id).all()
            if len(raw_questions) == 0:
                abort(404)
            else:
                questions = [item.format() for item in raw_questions]
                total_questions = len(raw_questions)
                current_category = Category.query.get(id).type
                return jsonify({
                    "success": True,
                    "questions": questions,
                    "total_questions": total_questions,
                    "current_category": current_category
                })
        except:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route('/quizzes', methods=['POST'])
    def show_quizzes():
        try:
            body = request.get_json()
            if body:
                past_questions_id = body.get('previous_questions')
                quiz_category = body.get('quiz_category')
                category = quiz_category['id']
                print(category)

            if body is not None:
                questions = Question.query.filter(Question.category == category).order_by(Question.id).all()
            else:
                questions = Question.query.order_by(Question.id).all()

            print(questions)

            current_questions_id = [item.format()['id'] for item in questions]
            current_questions_id_copy = current_questions_id.copy()

            if body is not None:
                if past_questions_id:
                    for item in current_questions_id:
                        if item in past_questions_id:
                            current_questions_id_copy.remove(item)

            length = len(current_questions_id_copy)
            random_position = random.randint(0, length - 1)
            random_id = current_questions_id_copy[random_position]
            random_question = (Question.query.get(random_id)).format()
            print(random_question)

            return jsonify({
                "success": True,
                "question": random_question
            })

        except:
            abort(422)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable request"
        }), 422

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    return app

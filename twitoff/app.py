from flask import Flask, jsonify

def create_app():
    """Create and configure and instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello TwitOff!'

    @app.route('/about')
    def about():
        return 'This is an app to guess who is more likely to say a ' \
               'user-created tweet between two existing twitter users' \
               ' by using their existing tweet history!'

    @app.route('/books')
    @app.route('/books.json')
    def list_books():
        books = [
            {'id': 1, 'title': 'book1'},
            {'id': 2, 'title': 'book2'}
        ]
        return jsonify(books)

    return app
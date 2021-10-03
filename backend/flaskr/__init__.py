import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy  # , or_
from flask_cors import CORS
import random
import sys

from sqlalchemy.sql.expression import select, true

from models import setup_db, Book, get_db

BOOKS_PER_SHELF = 8

# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    # @TODO: Write a route that retrivies all books, paginated.
    #         You can use the constant above to paginate by eight books.
    #         If you decide to change the number of books per page,
    #         update the frontend to handle additional books in the styling and pagination
    #         Response body keys: 'success', 'books' and 'total_books'
    # TEST: When completed, the webpage will display books including title, author, and rating shown as stars
    # curl http://127.0.0.1:5000/books
    @app.route('/books', methods=['GET'])
    def get_books():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        try:
            books = Book.query.order_by(Book.id).all()
            formatted_books = [book.format() for book in books]
        except:
            abort(500)
        finally:
            if len(formatted_books[start:end]) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'books': formatted_books[start:end],
                'total_books': len(formatted_books)
            })

    @app.route('/books/<int:book_id>', methods=['GET'])
    def get_book(book_id):
        try:
            book = Book.query.filter_by(id=book_id).first()
            if book is None:
                abort(404)
            else:
                return jsonify({'success': True,
                                'book': book.format,
                                'total_books': 1})
        except:
            abort(400)

    # @TODO: Write a route that will update a single book's rating.
    #         It should only be able to update the rating, not the entire representation
    #         and should follow API design principles regarding method and route.
    #         Response body keys: 'success'
    # TEST: When completed, you will be able to click on stars to update a book's rating and it will persist after refresh

    # curl http://127.0.0.1:5000/books/8 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'
    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_book(book_id):
        body = request.get_json()
        db = get_db()
        error = False
        try:
            book = Book.query.filter_by(id=book_id).one_or_none()

            if book is None:
                abort(404)

            if 'rating' in body:
                book.rating = int(body.get('rating'))
                book.update()
        except:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
            if not error:
                return jsonify({
                    'success': True,
                    'id': book_id
                })
            else:
                abort(400)

    # @TODO: Write a route that will delete a single book.
    #        Response body keys: 'success', 'deleted'(id of deleted book), 'books' and 'total_books'
    #        Response body keys: 'success', 'books' and 'total_books'

    # TEST: When completed, you will be able to delete a single book by clicking on the trashcan.

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        db = get_db()
        try:
            book = Book.query.filter_by(id=book_id).one_or_none()

            if book is None:
                abort(404)

            book.delete()
        except:
            db.session.rollback()
        finally:
            db.session.close()

            selection = Book.query.order_by(Book.id).all()
            formatted_books = [item.format() for item in selection]
            total_books = len(formatted_books)
            current_books = []

            previous_books = Book.query.filter(Book.id < book_id).count()
            page = int(previous_books/10) + 1
            start = (page - 1) * 10
            end = start + 10

            if(len(formatted_books[start:end]) > 0):
                current_books = formatted_books[start:end]

            return jsonify({
                'success': True,
                'deleted': book_id,
                'books': current_books,
                'total_books': total_books
            })

    # @TODO: Write a route that create a new book.
    #        Response body keys: 'success', 'created'(id of created book), 'books' and 'total_books'
    # TEST: When completed, you will be able to a new book using the form. Try doing so from the last page of books.
    #       Your new book should show up immediately after you submit it at the end of the page.
    @app.route('/books', methods=['POST'])
    def create_book():
        body = request.get_json()
        db = get_db()
        new_title = body.get('title', None)
        new_author = body.get('author', None)
        new_rating = body.get('rating', None)

        try:
            book = Book(title=new_title, author=new_author, rating=new_rating)
            book.insert()
            db.session.refresh(book)
        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()
            selection = Book.query.order_by(Book.id).all()
            formatted_books = [item.format() for item in selection]
            page = int(len(formatted_books)/10) + 1
            start = (page - 1) * 10
            end = start + 10
            total_books = len(formatted_books)
        print(book.id, file=sys.stderr)
        return jsonify({
            'success': True,
            'created': book.id,
            'books': formatted_books[start:end],
            'total_books': total_books
        })
        return app

    return app

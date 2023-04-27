from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'O Senhor dos Anéis - A sociedade do Anel',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter e a Pedra Filosofoal',
        'author': 'J.K Howling'
    },
    {
        'id': 3,
        'title': 'Clean Code',
        'author': 'Robert C. Martin'

    },
    {
        'id': 4,
        'title': 'Diário de um banana - Rodrick é o cara!',
        'author': 'Jeff Kinney'
    }
]


# Consultar (todos)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Consultar (id)
@app.route('/books/<int:id>', methods=['GET'])
def get_books_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


# Editar livro
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_id(id):
    modified_book = request.get_json()
    for indice, book in enumerate(books):
        if book.get('id') == id:
            books[indice].update(modified_book)
            return jsonify(books[indice])


# Criar livro
@app.route('/books/add-new', methods=['POST'])
def add_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book)


# Excluir
@app.route('/books/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    for indice, book in enumerate(books):
        if book.get('id') == id:
            del books[indice]
            return jsonify(books)


app.run(port=8080, host='localhost', debug=True)

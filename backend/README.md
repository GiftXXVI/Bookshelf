# Bookshelf API Documentation

## Introduction

The Bookshelf API is a virtual library of books. It enables a reader to search, retrieve, create, update and delete books. It was created to simplify the process of indexing and searching massive collections of books.

## Getting Started

- Base URL: At present the application can only be accessed locally at the following url: *http://127.0.0.1:5000/*

- Authentication: This version of the application does not require authentication or API keys.

## Errors

Errors are returned in the following JSON format:

```
{
    'success':False,
    'error':400,
    'message':'bad request'
}

```

The following HTTP Status Codes may be returned by the API in the event of an error:

- 404 - Not Found
- 400 - Bad Request
- 422 - Unprocessable
- 405 - Method Not Allowed

## Resource Endpoint Library

Books are the sole resource in the API. They can be accessed at the following endpoints:

### GET `/books`

- General: Used to retrieve a list of books, in pages, with each page consisting of 8 books. There is also an optional page number argument, which has a default value of 1. Returns success value, book objects and the total number of books available.

- Sample URL:

```bash
curl http://127.0.0.1:5000/books
```

```
{
  "books": [
    {
      "author": "Stephen King",
      "id": 1,
      "rating": 5,
      "title": "The Outsider: A Novel"
    },
    {
      "author": "Lisa Halliday",
      "id": 2,
      "rating": 4,
      "title": "Asymmetry: A Novel"
    },
    {
      "author": "Kristin Hannah",
      "id": 3,
      "rating": 4,
      "title": "The Great Alone"
    },
    {
      "author": "Tara Westover",
      "id": 4,
      "rating": 5,
      "title": "Educated: A Memoir"
    },
    {
      "author": "Jojo Moyes",
      "id": 5,
      "rating": 5,
      "title": "Still Me: A Novel"
    },
    {
      "author": "Leila Slimani",
      "id": 6,
      "rating": 2,
      "title": "Lullaby"
    },
    {
      "author": "Amitava Kumar",
      "id": 7,
      "rating": 5,
      "title": "Immigrant, Montana"
    },
    {
      "author": "Madeline Miller",
      "id": 8,
      "rating": 5,
      "title": "CIRCE"
    }
  ],
  "success": true,
  "total_books": 17
}
```

### GET `/books/search?search_term={search_term}`

- General: Used to retrieve books that match a search term, in pages, with each page consisting of 8 books. Returns a response in the same format as GET `/books`

- Sampe URL:

```bash
curl http://127.0.0.1:5000/books/search?search_term=circe
```

```
{
  "books": [
    {
      "author": "Madeline Miller",
      "id": 8,
      "rating": 5,
      "title": "CIRCE"
    }
  ],
  "success": true,
  "total_books": 1
}
```

### POST `/books`

- General : Used to create a new book using the submitted title, author and rating. Returns the id of the id of the created book, success value, total books, and book list based on the current page number.

* Sample URL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"The Midnight Library", "author":"Matt Haig", "rating":"5"}' http://127.0.0.1:5000/books
```

```
{
  "books": [
    {
      "author": "Stephen King",
      "id": 1,
      "rating": 5,
      "title": "The Outsider: A Novel"
    },
    {
      "author": "Lisa Halliday",
      "id": 2,
      "rating": 4,
      "title": "Asymmetry: A Novel"
    },
    {
      "author": "Kristin Hannah",
      "id": 3,
      "rating": 4,
      "title": "The Great Alone"
    },
    {
      "author": "Tara Westover",
      "id": 4,
      "rating": 5,
      "title": "Educated: A Memoir"
    },
    {
      "author": "Jojo Moyes",
      "id": 5,
      "rating": 5,
      "title": "Still Me: A Novel"
    },
    {
      "author": "Leila Slimani",
      "id": 6,
      "rating": 2,
      "title": "Lullaby"
    },
    {
      "author": "Amitava Kumar",
      "id": 7,
      "rating": 5,
      "title": "Immigrant, Montana"
    },
    {
      "author": "Madeline Miller",
      "id": 8,
      "rating": 5,
      "title": "CIRCE"
    }
  ],
  "created": 25,
  "success": true,
  "total_books": 18
}
```

### PATCH `/books/{book_id}`

- General : Used to update the rating of a book. Returns the success value of the operation and the id of the book whose rating has been modified.

- Sample URL:

```bash
curl http://127.0.0.1:5000/books/25 -X PATCH -H "Content-Type: application/json" -d '{"rating":"3"}'
```

```
{
  "id": 25,
  "success": true
}
```

### DELETE `/books/{book_id}`

- General : Used to delete a book by providing it's id. Returns the id of the deleted book, success value, total books and current list of books after completing the operation.

* Sample URL:
```bash
curl -X DELETE http://127.0.0.1:5000/books/23?page=2
```

```
{
  "books": [
    {
      "author": "Gina Apostol", 
      "id": 9, 
      "rating": 5, 
      "title": "Insurrecto: A Novel"
    }, 
    {
      "author": "Tayari Jones", 
      "id": 10, 
      "rating": 5, 
      "title": "An American Marriage"
    }, 
    {
      "author": "Jordan B. Peterson", 
      "id": 11, 
      "rating": 5, 
      "title": "12 Rules for Life: An Antidote to Chaos"
    }, 
    {
      "author": "Kiese Laymon", 
      "id": 12, 
      "rating": 1, 
      "title": "Heavy: An American Memoir"
    }, 
    {
      "author": "Emily Giffin", 
      "id": 13, 
      "rating": 4, 
      "title": "All We Ever Wanted"
    }, 
    {
      "author": "Jose Andres", 
      "id": 14, 
      "rating": 4, 
      "title": "We Fed an Island"
    }, 
    {
      "author": "Rachel Kushner", 
      "id": 15, 
      "rating": 1, 
      "title": "The Mars Room"
    }, 
    {
      "author": "Gregory Blake Smith", 
      "id": 16, 
      "rating": 2, 
      "title": "The Maze at Windermere"
    }
  ], 
  "deleted": 23, 
  "success": true, 
  "total_books": 17
}
```

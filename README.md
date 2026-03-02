# 📚 Library Management System API

A robust RESTful API developed with **Django** and **Django REST Framework (DRF)** for managing a library's catalog. This project provides full CRUD functionality for authors and books, featuring advanced server-side filtering, search, and pagination.

## ✨ Features

- **Relational Mapping**: Seamlessly links books to authors with `on_delete=models.CASCADE` protection.
- **Advanced Filtering**:
  - **Authors**: Filter by `country` or `birth_year`.
  - **Books**: Filter by `author_id`, `is_available`, `price` (min/max), and `year`.
- **Search & Ordering**:
  - Text-based search on book titles.
  - Custom ordering by `price`, `published_date`, `last_name`, etc.
- **Pagination**: Standardized 10-item-per-page results using `StandardResultsPagination`.
- **Validation**: Strict data validation via DRF Serializers.

## 🛠️ Tech Stack

- **Framework:** [Django](https://www.djangoproject.com/)
- **Toolkit:** [Django REST Framework](https://www.django-rest-framework.org/)
- **Language:** Python 3.x
- **Database:** SQLite (default) / PostgreSQL compatible

---



## 📋 API Endpoints

### ✍️ Author Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/authors/` | List authors (Supports `country`, `birth_year`, `ordering`) |
| `POST` | `/api/authors/` | Create a new author |
| `GET` | `/api/authors/{id}/` | Retrieve specific author details |
| `PUT` | `/api/authors/{id}/` | Update an existing author |
| `DELETE` | `/api/authors/{id}/` | Delete an author |

### 📖 Book Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/books/` | List books (Supports `search`, `min_price`, `max_price`, `is_available`, etc.) |
| `POST` | `/api/books/` | Add a new book |
| `GET` | `/api/books/{id}/` | Retrieve specific book details |
| `PUT` | `/api/books/{id}/` | Update book information |
| `DELETE` | `/api/books/{id}/` | Remove a book from catalog |

---

## 🔍 Query Parameter Examples

**Filter Books by Price and Availability:**
`GET /api/books/?min_price=15.00&max_price=50.00&is_available=true`

**Search Books & Order by Pages:**
`GET /api/books/?search=python&ordering=-pages`

**Filter Authors by Country:**
`GET /api/authors/?country=Azerbaijan&ordering=last_name`

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/saidaheyderli/library_project.git](https://github.com/saidaheyderli/library_project.git)
   cd library_project

# qa_python
Для тестирования класса BooksCollector
Использована фикстура collector: для каждого теста создаётся новый экземпляр класса BooksCollector с использованием фикстуры collector. Это гарантирует, что состояние коллекции книг будет очищаться между тестами.

Реализованы следующие тесты:
1. Тест test_add_new_book_add_two_books
Проверяет, что метод add_new_book корректно добавляет несколько книг в коллекцию.
Методы: add_new_book, get_books_genre

2. Тест test_add_new_book
Проверяет, что метод add_new_book корректно добавляет книгу в коллекцию и присваивает ей пустой жанр по умолчанию.
Методы: add_new_book, get_books_genre

3. Тест test_add_new_book_exceeds_max_length
Проверяет, что метод add_new_book не добавляет книгу, название которой превышает 40 символов.
Методы: add_new_book, get_books_genre

4. Тест test_set_book_genre_valid
Проверяет, что метод set_book_genre корректно присваивает жанр книге.
Методы: add_new_book, set_book_genre, get_book_genre

5. Тест test_set_book_genre_invalid
Проверяет, что метод set_book_genre не изменяет жанр книги, если указан неверный жанр.
Методы: add_new_book, set_book_genre, get_book_genre

6. Тест test_get_books_with_specific_genre
Проверяет, что метод get_books_with_specific_genre правильно возвращает книги определённого жанра.
Методы: add_new_book, set_book_genre, get_books_with_specific_genre

7. Тест test_get_books_for_children
Проверяет, что метод get_books_for_children правильно фильтрует книги, подходящие для детей.
Методы: add_new_book, set_book_genre, get_books_for_children

8. Тест test_add_book_in_favorites
Проверяет, что метод add_book_in_favorites правильно добавляет книгу в список избранных.
Методы: add_new_book, add_book_in_favorites, get_list_of_favorites_books

9.  Тест test_add_book_in_favorites_invalid
Проверяет, что метод add_book_in_favorites не добавляет книгу в избранное, если книга ещё не была добавлена в коллекцию.
Методы: add_book_in_favorites, get_list_of_favorites_books

10. Тест test_delete_book_from_favorites
Проверяет, что метод delete_book_from_favorites правильно удаляет книгу из списка избранных.
Методы: add_new_book, add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books

11. Тест test_get_books_genre (с параметризацией)
Проверяет, что метод get_books_genre корректно возвращает жанры для различных книг.
Методы: add_new_book, get_books_genre

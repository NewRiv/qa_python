# qa_python
Для тестирования класса BooksCollector
Использована фикстура collector: для каждого теста создаётся новый экземпляр класса BooksCollector с использованием фикстуры collector. Это гарантирует, что состояние коллекции книг будет очищаться между тестами.

Реализованы следующие тесты:
1. Тест test_add_new_book_add_two_books
Проверяет, что при добавлении двух книг их общее количество корректно.

2. Тест test_add_new_book
Проверяет, что после добавления новой книги она появляется в списке.

3. Тест test_add_new_book_exceeds_max_length
Проверяет, что книги с названием более 40 символов не добавляются

4. Тест test_set_book_genre_valid
Проверяет, что корректно присваивается жанр книге.

5. Тест test_set_book_genre_invalid
Проверяет, что установка некорректного жанра игнорируется.

6. Тест test_get_books_with_specific_genre
Проверяет, что метод возвращает только книги указанного жанра.

7. Тест test_get_books_for_children
Проверяет, что метод возвращает только детские книги.

8. Тест test_add_book_in_favorites
Проверяет добавление книги в список избранного.

9.  Тест test_add_book_in_favorites_invalid
Проверяет, что что нельзя добавить в избранное книгу, отсутствующую в библиотеке.

10. Тест test_delete_book_from_favorites
Проверяет удаление книги из списка избранного.

11. Тест test_get_books_genre (с параметризацией)
Проверяет, что метод возвращает корректный список всех добавленных книг и их жанров.

12. Тест get_book_genre
Проверяет, что метод возвращает None для книги, которой нет в коллекции.

13. Тест get_list_of_favorites_books:
Проверяет, что метод возвращает правильный список избранных книг (нескольких книг). 
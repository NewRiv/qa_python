import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
         # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()

    def test_add_new_book_exceeds_max_length(self, collector):
        collector.add_new_book("x" * 41)
        assert "x" * 41 not in collector.get_books_genre()

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Романтика")
        assert collector.get_book_genre("Гарри Поттер") == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Тёмная Башня")
        collector.set_book_genre("Тёмная Башня", "Фантастика")
        collector.add_new_book("Гордость и предубеждение")
        collector.set_book_genre("Гордость и предубеждение", "Романтика")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert "Гордость и предубеждение" not in books

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1

    def test_add_book_in_favorites_invalid(self, collector):
        collector.add_book_in_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert "Гарри Поттер" not in favorites

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 0

    @pytest.mark.parametrize("books", [
        ["Гарри Поттер", "Тёмная Башня"],
        ["Гордость и предубеждение", "1984"]
    ])
    def test_get_books_genre(self, collector, books):
        for book in books:
            collector.add_new_book(book)
        books_genre = collector.get_books_genre()
        for book in books:
            assert book in books_genre

    def test_get_book_genre_method(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Утес совы") is None

    def test_get_list_of_favorites_books_method(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Тёмная Башня")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]

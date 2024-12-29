import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        # collector = BooksCollector()

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
        assert collector.get_books_genre()["Гарри Поттер"] == ""

    def test_add_new_book_exceeds_max_length(self, collector):
        collector.add_new_book("x" * 41)  # Превышает 40 символов
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
        books = collector.get_books_with_specific_genre("Фантастика")
        assert len(books) == 2
        assert "Гарри Поттер" in books and "Тёмная Башня" in books

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1
        assert "Гарри Поттер" in books_for_children
        assert "Оно" not in books_for_children

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert "Гарри Поттер" in favorites

    def test_add_book_in_favorites_invalid(self, collector):
        collector.add_book_in_favorites("Гарри Поттер")  # Книга не добавлена в books_genre
        favorites = collector.get_list_of_favorites_books()
        assert "Гарри Поттер" not in favorites

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 0

    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "Тёмная Башня"])
    def test_get_books_genre(self, collector, book_name):
        collector.add_new_book(book_name)
        books_genre = collector.get_books_genre()
        assert book_name in books_genre
        assert books_genre[book_name] == ""

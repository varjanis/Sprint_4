import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_one_book(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    def test_add_new_book_add_same_book_twice_not_added(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book',
        [
            'Ю',
            'Мастер и Маргарита',
            'Длинное название внем ровно 39 символов',
            'Длинное название в нем ровно 40 символов'
        ]
    )
    def test_add_new_book_name_length_below41_success(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book',
        [
            '',
            'Длинное название в нем ровно 40+1 символ ',
            'Длинное название в нем ровно 40+2 символа',
            'Чудовищно длинное название в нем ровно 50 символов'
        ]
    )
    def test_add_new_book_name_length_over40_fail(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_book_adds_without_genre_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ловцы книг')
        assert collector.get_book_genre('Ловцы книг') == ''

    def test_set_book_genre_genre_of_new_book_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Мистер Вуду и дни недели': ''}
        collector.set_book_genre('Мистер Вуду и дни недели', 'Фантастика')
        assert collector.get_book_genre('Мистер Вуду и дни недели') == 'Фантастика'

    def test_get_book_genre_book_has_genre_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Мистер Вуду и дни недели': 'Фантастика'}
        assert collector.get_book_genre('Мистер Вуду и дни недели') == 'Фантастика'

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Мистер Вуду и дни недели': 'Фантастика', 'Арена': 'Фантастика',
                                 'Убийство в Восточном экспрессе': 'Детективы', 'Инфляция сегодня': 'Ужасы'}
        assert collector.get_books_with_specific_genre('Фантастика') == ['Мистер Вуду и дни недели', 'Арена']

    @pytest.mark.parametrize(
        'dictionary',
    [
        {
            'Мистер Вуду и дни недели': 'Фантастика',
            'Арена': 'Фантастика',
            'Убийство в Восточном экспрессе': 'Детективы',
            'Инфляция сегодня': 'Ужасы'
        },
        {
            'Стража! Стража!': 'Фантастика',
            'Тибетская книга мертвых': 'Комедии'
        },
        {
            'Пиши, сокращай': 'Детективы'
        }
    ]
    )
    def test_get_books_genre_get_current_dict_sucсess(self, dictionary):
        collector = BooksCollector()
        collector.books_genre = dictionary
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_current_dict_success(self):
        collector = BooksCollector()
        collector.books_genre = {
                                    'Мистер Вуду и дни недели': 'Фантастика',
                                    'Арена': 'Фантастика',
                                    'Убийство в Восточном экспрессе': 'Детективы',
                                    'Инфляция сегодня': 'Ужасы'
                             }

        assert collector.get_books_for_children() == ['Мистер Вуду и дни недели', 'Арена']

    def test_add_book_in_favorites_one_book_added_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Сказки старого Вильнюса': 'Фантастика'}
        collector.add_book_in_favorites('Сказки старого Вильнюса')
        assert 'Сказки старого Вильнюса' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_same_book_added_fail(self):
        collector = BooksCollector()
        collector.favorites = ['Сказки старого Вильнюса']
        collector.add_book_in_favorites('Сказки старого Вильнюса')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book_deleted_success(self):
        collector = BooksCollector()
        collector.favorites = ['Сказки старого Вильнюса']
        collector.delete_book_from_favorites('Сказки старого Вильнюса')
        assert 'Сказки старого Вильнюса' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_current_list_success(self):
        collector = BooksCollector()
        collector.favorites = ['Сказки старого Вильнюса', 'Тяжелый свет Куртейна', 'Ловцы книг']
        assert collector.get_list_of_favorites_books() == ['Сказки старого Вильнюса', 'Тяжелый свет Куртейна', 'Ловцы книг']



Для метода add_new_book: 

Метод test_add_new_book_add_two_books - проверяет добавление двух книг

Метод test_add_new_book_add_same_book_twice_not_added - проверяет проверка на то что нельзя два раза добавить книгу с одним и тем же названием

Метод test_add_new_book_name_length_below41_success - проверяет, что если длина названия добавляемой книги менее 41 символа, книга добавляется

Метод test_add_new_book_name_length_over40_fail проверяет, что название длиной более 40 символов не добавится

Метод test_add_new_book_book_adds_without_genre_empty_genre проверяет, что новая книга добавляется без жанра



Для метода set_book_genre

Метод test_set_book_genre_genre_of_new_book_success - проверяет, что книге можно присвоить жанр

Для метода get_book_genre

Метод test_get_book_genre_book_has_genre_success проверяет, что можно получить жанр книги по её названию

Для метода get_books_with_specific_genre

Метод test_get_books_with_specific_genre_success - проверяет, что по жанру можно получить список книг этого жанра

Для метода get_books_genre

Метод test_get_books_genre_get_current_dict_sucсess - проверяет, что можно получить словарь books_genre с названиями и жанрами книг

Для метода get_books_for_children

Метод test_get_books_for_children_current_dict_success - проверяет, что из словаря books_genre отфильтрованы книги с жанрами без возрастного рейтинга

Для метода add_book_in_favorites

Метод test_add_book_in_favorites_one_book_added_success проверяет, что можно добавить книгу в избранное

Метод test_add_book_in_favorites_same_book_added_fail проверяет, что нельзя добавить в избранное одну и ту же книгу дважды

Для метода delete_book_from_favorites

Метод test_delete_book_from_favorites_one_book_deleted_success - проверяет, что можно удалить книгу из избранного

Для метода get_list_of_favorites_books

Метод test_get_list_of_favorites_books_current_list_success проверяет, что можно получить текущий список книг в избранном




# qa_python

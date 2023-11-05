import pytest
from string_utils import StringUtils


string_utils_test = StringUtils()

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# Позитивные тесты
@pytest.mark.parametrize('input, result', [
    ("hello", "Hello"), 
    ("WORLD", "World"),
    ("skypro", "Skypro"),
    ("снег", "Снег"), #кириллица
    ("4 january", "4 January"),
    ("124", "124"),
    ("pOsItIvE", "Positive"),
    ("и долго ли, коротко шел он к своей суженной.","И долго ли, коротко шел он к своей суженной." ),
    ("Small", "Small")
    ])
def test_positive_capitalize(input, result):
    res = string_utils_test.capitilize(input)
    assert res == result

# Негативные тесты
@pytest.mark.negative
@pytest.mark.xfail(strict=True)(reason="Negative tests")
@pytest.mark.parametrize('input, result', [
    ("", ""),  
    ("  ", "  "),   
    (" skypro", " Skypro"), 
    (None, None)
    ])
def test_negative_capitalize(input, result):
    res = string_utils_test.capitilize(input)
    assert res == result

# Принимает на вход текст и удаляет пробелы в начале, если они есть
# Позитивные тесты
@pytest.mark.parametrize('input, result', [
    (" energy", "energy"),
    (" Skypro ", "Skypro "),
    (" 123", "123"),
    (" 12 February", "12 February"),
    (" no_spaces_here", "no_spaces_here"),
    (" is it true?!", "is it true?!"),
    (" and@gmail.com", "and@gmail.com"),
    (" $34.887", "$34.887"),
    (" и долго ли, коротко - шел он к своей суженной.","и долго ли, коротко - шел он к своей суженной."), 
    ("idilia", "idilia"),
    ])
def test_positive_trim(input, result):
    res = string_utils_test.trim(input)
    assert res == result

# Негативные тесты
@pytest.mark.negative
@pytest.mark.xfail(strict=True)(reason="Negative tests")
@pytest.mark.parametrize('input, result', [
    ("  ", " "),
    ([" Grom", 1, True], ["Grom", 1, True],), 
    ("", ""),
    ])
def test_negative_trim(input, result):
    res = string_utils_test.trim(input)
    assert res == result

# Принимает на вход текст с разделителем и возвращает список строк.
# Позитивные тесты
@pytest.mark.parametrize("input_string, expected_output", [
    ("a,b,c,d", ["a", "b", "c", "d"]),
    ("1:2:3", ["1", "2", "3"]),
    ("one two three", ["one", "two", "three"]),
])
def test_positive_to_list(input_string, expected_output):
    res = string_utils_test.to_list(input_string)
    assert res == expected_output

# Негативные тесты
@pytest.mark.negative
@pytest.mark.xfail(strict=True)(reason="Negative tests")
@pytest.mark.parametrize("input_string, expected_output", [
    ("", []),
    ("15.06.2023", ["15", "06", "23"]),
    ("   ", []),
    (None, []),
    ([], [])
])
def test_negative_to_list(input_string, expected_output):
    res = string_utils_test.to_list(input_string)
    assert res == expected_output

# Позитивный тест: символ присутствует в строке
@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "K", True),  
    ("14 January","a", True )
])
def test_positive_contains(string, symbol, expected_output):
    res = string_utils_test.contains(string, symbol)
    assert res == expected_output

# Негативный тест
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "C", False),
    ("", "", False),
    ("   ", " ", False)
])
def test_negative_contains(string, symbol, expected_output):
    res = string_utils_test.contains(string, symbol)
    assert res == expected_output

# Позитивный тест: удаление символа
@pytest.mark.parametrize("string, symbol_to_delete, expected_output", [
    ("SkyPro", "k", "SyPro"),
    ("Kot", "o", "Kt"),
    ("Maxim", "im", "Max"),
    ("12.01.23", ".01", "12.23")
])
def test_positive_delete_symbol_single_char(string, symbol_to_delete, expected_output):
    res = string_utils_test.delete_symbol(string, symbol_to_delete)
    assert res == expected_output

# Негативный тест: удаление символа
@pytest.mark.negative
@pytest.mark.xfail(strict=True)(reason="Negative tests")
@pytest.mark.parametrize("string, symbol_to_delete, expected_output", [
    ("SkyPro", "x", "SkyPro"),
    ("", "o", ""),
])
def test_negative_delete_symbol_single_char(string, symbol_to_delete, expected_output):
    res = string_utils_test.delete_symbol(string, symbol_to_delete)
    assert res == expected_output

# Возвращает `True`, если строка начинается с заданного символа
# Позитивный тест: строка начинается с символа
@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("Снег", "С", True),
    ("123", "1", True),
    ("14.01.22", "1", True),
    ])
def test_positive_starts_with(string, symbol, expected_output):
    res = string_utils_test.starts_with(string, symbol)
    assert res == expected_output

# Негативный тест: строка не начинается с символа
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "P", False),
    ("@#$!", "#", False),
    ("123", "2", False),
    ("","f", False),
    ("   ", " ", False)
])
def test_negative_starts_with(string, symbol, expected_output):
    res = string_utils_test.starts_with(string, symbol)
    assert res == expected_output

#Возвращает `True`, если строка заканчивается заданным символом
# Позитивный тест: строка заканчивается символом
@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "o", True),
    ("Сугроб", "б", True),
    ("123", "3", True),
    ("14/03/27", "7", True)
])
def test_positive_end_with(string, symbol, expected_output):
    res = string_utils_test.end_with(string, symbol)
    assert res == expected_output

# Негативный тест: строка не заканчивается символом
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "P", False),
    ("Hello", "H", False),
    ("123", "2", False),
    ("   ", " ", False)
])
def test_negative_end_with(string, symbol, expected_output):
    res = string_utils_test.end_with(string, symbol)
    assert res == expected_output

#Возвращает `True`, если строка пустая и `False` - если нет
# Позитивный тест: строка пустая
@pytest.mark.parametrize("string, expected_output", [
    ("", True),
    ("  ", True),
])
def test_positive_is_empty(string, expected_output):
    res = string_utils_test.is_empty(string)
    assert res == expected_output

# Негативный тест: строка не пустая
@pytest.mark.negative
@pytest.mark.parametrize("string, expected_output", [
    ("SkyPro", False),
    (" сугроб ", False),
    ("   /n   ", False)
])
def test_negative_is_empty(string, expected_output):
    res = string_utils_test.is_empty(string)
    assert res == expected_output

#Преобразование списка элементов в строку с указанным разделителем 
# Позитивный тест
@pytest.mark.parametrize("lst, joiner, expected_output", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    ([0, -1, 5, 10], " / ", "0 / -1 / 5 / 10"),
    (["Sky", "Pro"], " * ", "Sky * Pro"),
    (["Hello" "World"], " ! ", "Hello ! World"),
    ([1, 2, 3, 4], "-", "1-2-3-4"),
    ([-1, -2, -3, -4], " | ", "-1 | -2 | -3 | -4"),
])
def test_positive_list_to_string_with_default_joiner(lst, joiner, expected_output):
    res = string_utils_test.list_to_string(lst, joiner)
    assert res == expected_output

# Негативный тест
@pytest.mark.negative
@pytest.mark.xfail(strict=True)(reason="Negative tests")
@pytest.mark.parametrize("lst, joiner, expected_output", [
    ([], ", ", ""),
])
def test_negative_list_to_string_with_default_joiner(lst, joiner, expected_output):
    res = string_utils_test.list_to_string(lst, joiner)
    assert res == expected_output
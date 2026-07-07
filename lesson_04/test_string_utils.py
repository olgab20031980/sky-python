import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Полный набор тестов для класса StringUtils"""

    class TestCapitalize:
        """Тесты для метода capitalize"""

        def test_capitalize_positive_not_empty_string(self):
            utils = StringUtils()
            assert utils.capitalize("тест") == "Тест"

        def test_capitalize_positive_numbers_as_string(self):
            utils = StringUtils()
            assert utils.capitalize("123") == "123"

        def test_capitalize_positive_string_with_spaces(self):
            utils = StringUtils()
            assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"

        def test_capitalize_positive_english_text(self):
            utils = StringUtils()
            assert utils.capitalize("skypro") == "Skypro"

        def test_capitalize_positive_one_character(self):
            utils = StringUtils()
            assert utils.capitalize("a") == "A"

        def test_capitalize_positive_already_capitalized(self):
            utils = StringUtils()
            assert utils.capitalize("Skypro") == "Skypro"

        def test_capitalize_negative_empty_string(self):
            utils = StringUtils()
            assert utils.capitalize("") == ""

        def test_capitalize_negative_string_with_space(self):
            utils = StringUtils()
            assert utils.capitalize(" ") == " "

        def test_capitalize_negative_string_with_leading_space(self):
            utils = StringUtils()
            assert utils.capitalize(" текст") == " текст"

        def test_capitalize_negative_none_input(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Input must be a string"):
                utils.capitalize(None)

        def test_capitalize_negative_number_input(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Input must be a string"):
                utils.capitalize(123)

        def test_capitalize_negative_list_input(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Input must be a string"):
                utils.capitalize([])

    class TestTrim:
        """Тесты для метода trim"""

        def test_trim_positive_not_empty_string(self):
            utils = StringUtils()
            assert utils.trim("   тест") == "тест"

        def test_trim_positive_numbers_as_string(self):
            utils = StringUtils()
            assert utils.trim("   123") == "123"

        def test_trim_positive_string_with_spaces(self):
            utils = StringUtils()
            assert utils.trim("   04 апреля 2023") == "04 апреля 2023"

        def test_trim_positive_no_spaces(self):
            utils = StringUtils()
            assert utils.trim("skypro") == "skypro"

        def test_trim_positive_one_space(self):
            utils = StringUtils()
            assert utils.trim(" skypro") == "skypro"

        def test_trim_positive_multiple_spaces(self):
            utils = StringUtils()
            assert utils.trim("   skypro") == "skypro"

        def test_trim_positive_spaces_inside(self):
            utils = StringUtils()
            assert utils.trim("   sky pro") == "sky pro"

        def test_trim_negative_empty_string(self):
            utils = StringUtils()
            assert utils.trim("") == ""

        def test_trim_negative_string_with_space(self):
            utils = StringUtils()
            assert utils.trim(" ") == ""

        def test_trim_negative_only_spaces(self):
            utils = StringUtils()
            assert utils.trim("   ") == ""

        def test_trim_negative_none_input(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Input must be a string"):
                utils.trim(None)

        def test_trim_negative_number_input(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Input must be a string"):
                utils.trim(123)

        def test_trim_negative_list_input(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Input must be a string"):
                utils.trim([])

    class TestContains:
        """Тесты для метода contains"""

        def test_contains_positive_not_empty_string_found(self):
            utils = StringUtils()
            assert utils.contains("тест", "т") is True

        def test_contains_positive_not_empty_string_not_found(self):
            utils = StringUtils()
            assert utils.contains("тест", "а") is False

        def test_contains_positive_numbers_as_string(self):
            utils = StringUtils()
            assert utils.contains("123", "2") is True
            assert utils.contains("123", "4") is False

        def test_contains_positive_string_with_spaces(self):
            utils = StringUtils()
            assert utils.contains("04 апреля 2023", " ") is True
            assert utils.contains("04 апреля 2023", "я") is True
            assert utils.contains("04 апреля 2023", "x") is False

        def test_contains_positive_english_text(self):
            utils = StringUtils()
            assert utils.contains("SkyPro", "S") is True
            assert utils.contains("SkyPro", "U") is False

        def test_contains_positive_special_symbol(self):
            utils = StringUtils()
            assert utils.contains("Hello!", "!") is True

        def test_contains_positive_symbol_at_beginning(self):
            utils = StringUtils()
            assert utils.contains("SkyPro", "S") is True

        def test_contains_positive_symbol_at_end(self):
            utils = StringUtils()
            assert utils.contains("SkyPro", "o") is True

        def test_contains_negative_empty_string(self):
            utils = StringUtils()
            assert utils.contains("", "a") is False
            assert utils.contains("", "") is True

        def test_contains_negative_string_with_space(self):
            utils = StringUtils()
            assert utils.contains(" ", " ") is True
            assert utils.contains(" ", "a") is False

        def test_contains_negative_none_string(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="String must be a string"):
                utils.contains(None, "a")

        def test_contains_negative_none_symbol(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Symbol must be a string"):
                utils.contains("SkyPro", None)

        def test_contains_negative_number_as_string(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="String must be a string"):
                utils.contains(123, "2")

        def test_contains_negative_number_as_symbol(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Symbol must be a string"):
                utils.contains("SkyPro", 123)

        def test_contains_negative_list_as_string(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="String must be a string"):
                utils.contains([], "a")

        def test_contains_negative_symbol_longer_than_one(self):
            utils = StringUtils()
            with pytest.raises(
                    ValueError, match="Symbol must be a single character"
                    ):
                utils.contains("SkyPro", "ky")

    class TestDeleteSymbol:
        """Тесты для метода delete_symbol"""

        def test_delete_symbol_positive_not_empty_string(self):
            utils = StringUtils()
            assert utils.delete_symbol("тест", "т") == "ес"
            assert utils.delete_symbol("тест", "е") == "тст"

        def test_delete_symbol_positive_numbers_as_string(self):
            utils = StringUtils()
            assert utils.delete_symbol("123", "2") == "13"
            assert utils.delete_symbol("123", "5") == "123"

        def test_delete_symbol_positive_string_with_spaces(self):
            utils = StringUtils()
            assert utils.delete_symbol("04 апреля 2023", " ") == "04апреля2023"
            assert utils.delete_symbol(
                "04 апреля 2023", "а"
                ) == "04 преля 2023"

        def test_delete_symbol_positive_english_text(self):
            utils = StringUtils()
            assert utils.delete_symbol("SkyPro", "k") == "SyPro"
            assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

        def test_delete_symbol_positive_multiple_occurrences(self):
            utils = StringUtils()
            assert utils.delete_symbol("aaabbb", "a") == "bbb"
            assert utils.delete_symbol("aaabbb", "b") == "aaa"

        def test_delete_symbol_positive_special_symbol(self):
            utils = StringUtils()
            assert utils.delete_symbol("Hello! World!", "!") == "Hello World"

        def test_delete_symbol_positive_symbol_not_found(self):
            utils = StringUtils()
            assert utils.delete_symbol("SkyPro", "z") == "SkyPro"

        def test_delete_symbol_positive_delete_all(self):
            utils = StringUtils()
            assert utils.delete_symbol("aaa", "a") == ""

        def test_delete_symbol_negative_empty_string(self):
            utils = StringUtils()
            assert utils.delete_symbol("", "a") == ""
            assert utils.delete_symbol("", "") == ""

        def test_delete_symbol_negative_string_with_space(self):
            utils = StringUtils()
            assert utils.delete_symbol(" ", " ") == ""
            assert utils.delete_symbol(" ", "a") == " "

        def test_delete_symbol_negative_none_string(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="String must be a string"):
                utils.delete_symbol(None, "a")

        def test_delete_symbol_negative_none_symbol(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Symbol must be a string"):
                utils.delete_symbol("SkyPro", None)

        def test_delete_symbol_negative_number_as_string(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="String must be a string"):
                utils.delete_symbol(123, "2")

        def test_delete_symbol_negative_number_as_symbol(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Symbol must be a string"):
                utils.delete_symbol("SkyPro", 123)

        def test_delete_symbol_negative_list_as_string(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="String must be a string"):
                utils.delete_symbol([], "a")

        def test_delete_symbol_negative_list_as_symbol(self):
            utils = StringUtils()
            with pytest.raises(TypeError, match="Symbol must be a string"):
                utils.delete_symbol("SkyPro", [])

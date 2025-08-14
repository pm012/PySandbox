import pytest
from lab_4_3_10 import process_file, FileEmpty, BadLine
from os import path


@pytest.fixture
def res_dir():
    """Fixture to provide the path to the 'res' directory."""
    return path.join(path.dirname(path.abspath(__file__)), "res")


def test_correct_file(res_dir):
    file_path = path.join(res_dir, "lab_4_3_10_correct.txt")
    expected_output = {
        "Andrew Cox": 1.5,
        "Anna Boleyn": 15.5,
        "John Smith": 7.0,
    }
    assert process_file(file_path) == expected_output


def test_empty_file(res_dir):
    file_path = path.join(res_dir, "lab_4_3_10_empty.txt")
    with pytest.raises(FileEmpty, match="The file is empty."):
        process_file(file_path)


def test_bad_line_incorrect_data_type(res_dir):
    file_path = path.join(res_dir, "lab_4_3_10_bad_line_incorrectdatatype.txt")
    with pytest.raises(BadLine, match="Bad line detected"):
        process_file(file_path)


def test_bad_line_more_items(res_dir):
    file_path = path.join(res_dir, "lab_4_3_10_more_items.txt")
    with pytest.raises(BadLine, match="Bad line detected"):
        process_file(file_path)


def test_bad_line_not_enough_items(res_dir):
    file_path = path.join(res_dir, "lab_4_3_10_bad_line_not_enough_items.txt")
    with pytest.raises(BadLine, match="Bad line detected"):
        process_file(file_path)


def test_file_not_found(res_dir):
    file_path = path.join(res_dir, "non_existent_file.txt")
    with pytest.raises(FileNotFoundError, match="does not exist"):
        process_file(file_path)
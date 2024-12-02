import pytest
from app.utils import load_text

@pytest.fixture
def test_file(tmp_path):
    test_content = "Hello, World!"
    test_file = tmp_path / "test.txt"
    test_file.write_text(test_content, encoding="utf-8")
    return test_file, test_content

def test_load_text(test_file):
    test_file_path, test_content = test_file
    assert load_text(test_file_path) == test_content



import pytest
from app.app import dedupe_list

def test_dedupe_basic():
    """Test basic duplicate removal"""
    assert dedupe_list([1, 2, 2, 3]) == [1, 2, 3]

def test_dedupe_empty_list():
    """Test empty list input"""
    assert dedupe_list([]) == []

def test_dedupe_no_duplicates():
    """Test list with no duplicates"""
    assert dedupe_list([1, 2, 3]) == [1, 2, 3]

def test_dedupe_string_list():
    """Test list with string elements"""
    assert dedupe_list(["a", "b", "a", "c"]) == ["a", "b", "c"]
    import pytest
from app.app import dedupe_list, add_numbers

# 原有测试保留
def test_dedupe_basic():
    assert dedupe_list([1, 2, 2, 3]) == [1, 2, 3]
def test_dedupe_empty_list():
    assert dedupe_list([]) == []
def test_dedupe_no_duplicates():
    assert dedupe_list([1, 2, 3]) == [1, 2, 3]
def test_dedupe_string_list():
    assert dedupe_list(["a", "b", "a", "c"]) == ["a", "b", "c"]

# 新增测试：测试加法函数
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
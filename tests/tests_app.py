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
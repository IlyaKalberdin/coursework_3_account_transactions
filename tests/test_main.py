from src.main import main


def test_main():
    assert main("tests/test_operations.json") == None

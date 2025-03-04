import pytest
from generate_text import generate_random_text

def test_generate_random_text():
    result = generate_random_text()
    assert len(result) == 6
    assert result.isalpha()  # Ensure only letters

if __name__ == "__main__":
    pytest.main()
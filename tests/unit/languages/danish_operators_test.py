import pytest

from normalization.languages.danish.operators import DanishOperators
from normalization.languages.registry import get_language_registry


@pytest.fixture
def operators() -> DanishOperators:
    return DanishOperators()


def test_danish_is_registered() -> None:
    assert "da" in get_language_registry()


def test_danish_registry_produces_danish_operators() -> None:
    instance = get_language_registry()["da"]()
    assert isinstance(instance, DanishOperators)


def test_config_code(operators: DanishOperators) -> None:
    assert operators.config.code == "da"


def test_word_replacements(operators: DanishOperators) -> None:
    assert operators.get_word_replacements()["krone"] == "kroner"
    assert "euro" not in operators.get_word_replacements()

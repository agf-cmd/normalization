import pytest

from normalization.pipeline.loader import load_pipeline


@pytest.fixture
def pipeline():
    return load_pipeline("gladia-3", "de")


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("irgendwann einmal", "irgendwann mal"),
        ("irgendwann mal", "irgendwann mal"),
        ("noch eines sagen", "noch eins sagen"),
        ("noch eins sagen", "noch eins sagen"),
        ("nunmehr", "nunmehr"),
        ("nun mehr", "nunmehr"),
        ("können", "konnen"),
        ("könnt", "konnen"),
        (
            "handels und entwicklungspolitik",
            "handels und entwicklungspolitik",
        ),
        (
            "handelspolitik und entwicklungspolitik",
            "handels und entwicklungspolitik",
        ),
        ("cotonou", "cotonou"),
        ("kottonou", "cotonou"),
        ("zweitausendsieben", "2007"),
        ("zwotausendsieben", "2007"),
        ("2007", "2007"),
    ],
)
def test_voxpopuli_german_aliases(pipeline, raw, expected):
    assert pipeline.normalize(raw) == expected


def test_mal_particle_not_expanded_to_einmal(pipeline):
    """Colloquial particle 'mal' must stay when it is not 'einmal'."""
    assert pipeline.normalize("halt mal so") == "mal so"

import pytest
import main


@pytest.mark.parametrize(
    "index, item",
    [
        pytest.param(1, [80, 140, 230]),
        pytest.param(2, [80, 140, 230]),
        pytest.param(3, [80, 140, 230])
    ]
)
def test_print_item(index: int, item: list):
    assert item[index-1]*1.25 == main.print_item(index, item)


@pytest.mark.parametrize(
    "index, item, tax",
    [
        pytest.param(1, [80, 140, 230], 1.2)
    ]
)
def test_print_item_with_tax(index: int, item: list, tax):
    assert item[index-1]*1.2 == main.print_item(index, item, tax)

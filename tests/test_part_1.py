import pytest
from source import part_1


@pytest.mark.unittest
@pytest.mark.parametrize(
    argnames=["input_timestamp", "output_timestamp"],
    argvalues=[
        ("2021-12-03T16:15:30.235Z", "2021-12-03T16:15:30.235Z"),
        ("2021-12-03T16:15:30.235", "2021-12-03T16:15:30.235Z"),
        ("2021-10-28T00:00:00.000", "2021-10-28T00:00:00.000Z"),
        ("2011-12-03T10:15:30", "2011-12-03T10:15:30.000Z"),
        (1726668850124, "2024-09-18T14:14:10.124Z"),
        ("1726668850124", "2024-09-18T14:14:10.124Z"),
        (1726667942, "2024-09-18T13:59:02.000Z"),
        ("1726667942", "2024-09-18T13:59:02.000Z"),
        (969286895000, "2000-09-18T14:21:35.000Z"),
        ("969286895000", "2000-09-18T14:21:35.000Z"),
        (3336042095, "2075-09-18T14:21:35.000Z"),
        ("3336042095", "2075-09-18T14:21:35.000Z"),
        (3336042095000, "2075-09-18T14:21:35.000Z"),
        ("3336042095000", "2075-09-18T14:21:35.000Z"),
    ],
)
def test_part_1(input_timestamp: str | int, output_timestamp: str) -> None:
    result = part_1.parse_timestamp(input_timestamp)
    assert result == output_timestamp


@pytest.mark.unittest
def test_invalid_timestamp() -> None:
    with pytest.raises(ValueError):
        part_1.parse_timestamp("not a timestamp")

    with pytest.raises(ValueError):
        part_1.parse_timestamp("2021-13-03T25:61:61Z")

    with pytest.raises(ValueError):
        part_1.parse_timestamp([])  # type: ignore

    with pytest.raises(ValueError):
        part_1.parse_timestamp(None)  # type: ignore

import pandas as pd
from plt_temp import create_dataframe


def test_create_dataframe():
    hours = [
        "2026-09-30T12:00",
        "2026-09-30T10:00",
        "2026-09-30T11:00"
    ]
    temps = [18.5, 15.2, 16.1]

    df = create_dataframe(hours, temps)

    assert list(df.columns) == ["time", "temperature_c"]
    assert len(df) == 3
    assert df["time"].is_monotonic_increasing
    assert df["temperature_c"].tolist() == [15.2, 16.1, 18.5]
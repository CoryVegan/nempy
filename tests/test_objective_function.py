import pandas as pd
from pandas._testing import assert_frame_equal
from nempy import objective_function


def test_energy():
    bidding_ids = pd.DataFrame({
        'unit': ['A', 'A', 'B', 'B'],
        'capacity_band': ['1', '2', '1', '2'],
        'variable_id': [1, 2, 3, 4]
    })
    price_bids = pd.DataFrame({
        'unit': ['A', 'B'],
        '1': [16.0, 23.0],
        '2': [17.0, 18.0]
    })
    unit_info = pd.DataFrame({
        'unit': ['A', 'B'],
        'loss_factor': [0.85, 1.1]
    })
    output = objective_function.energy(bidding_ids, price_bids, unit_info)
    expected = pd.DataFrame({
        'unit': ['A', 'A', 'B', 'B'],
        'capacity_band': ['1', '2', '1', '2'],
        'variable_id': [1, 2, 3, 4],
        'cost': [16.0, 17.0, 23.0, 18.0]
    })
    expected.index = list(expected.index)
    assert_frame_equal(output, expected)
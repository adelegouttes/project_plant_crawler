import pytest
from project_plant_crawler.api.api_utilities import *


@pytest.mark.parametrize(
    "allowed_keys,required_values",
    [
        ([], {'c': 'c'}),
        (['a'], {'c': 'c'}),
        (['a'], {'a': 'a'}),
        (['a', 'b', 'c'], {'a': 'a', 'b': 'b'}),
     ]
)
def test_generate_filter_string(allowed_keys: list, required_values: dict):

    generated_filter_string = generate_filter_string(allowed_keys=allowed_keys, query_parameters=required_values)
    # Assert no unexpected key in final filter
    for key in required_values.keys():
        if key not in allowed_keys:
            assert key not in generated_filter_string
        else:
            assert key in generated_filter_string





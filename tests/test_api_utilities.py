import pytest
from project_plant_crawler.api.api_utilities import *


@pytest.mark.parametrize(
    "allowed_keys,required_values",
    [
        ([], {'c': 'c'}),
        (['a'], {'c': 'c'}),
        (['a', 'b'], {'a': 'a', 'c': 'c'}),
     ]
)
def test_generate_filter_string_raises_key_error(allowed_keys: list, required_values: dict):

    required_keys = required_values.keys()

    allowed_keys_string = ', '.join(str(i) for i in allowed_keys)
    expected_message = '<p>Please filter plants only with the following arguments: {}.</p>'.format(allowed_keys_string)

    for key in required_keys:
        if key not in allowed_keys:
            with pytest.raises(Exception) as e_info:
                raise KeyError(expected_message)
    assert e_info.value.args[0] == expected_message

@pytest.mark.parametrize(
    "allowed_keys,required_values",
    [
        (['a', 'b', 'c'], {'a': 'a', 'c': 'c'}),
        (['a', 'b', 'c'], {'a': 'a', 'b': 'b', 'c': 'c'}),
     ]
)
def test_generate_filter_string_raises_all_allowed_parameters_added(allowed_keys: list, required_values: dict):

    generated_filter_string = generate_filter_string(allowed_keys=allowed_keys, query_parameters=required_values)
    # Assert no unexpected key in final filter
    for key in required_values.keys():
        expected_string = " {}='{}'".format(key, required_values[key])
        assert expected_string in generated_filter_string








import yaml

"""
Method to read the config file
"""


def read_config(config_file_path) -> dict | None:
    try:
        with open(config_file_path, 'r') as configFileContent:
            config = yaml.safe_load(configFileContent)
            if config is not None and isinstance(config, dict):
                flattened_config = flatten_dict(config)

                if flattened_config is not None:
                    return flattened_config
                else:
                    raise Exception("Config tree is empty")

    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found in path: {config_file_path}")


"""
Flatten dictionary until config tree's leaf level reached
:raise NoConfigFoundException: if flattened dictionary is empty
:param dict_to_flatten: Dictionary to flatten
:param parent_key: Key till previous config tree level
:return: flattened dictionary
"""


def flatten_dict(dict_to_flatten, parent_key='', separator='.') -> dict:
    flattened_dict = {}
    for key, value in dict_to_flatten.items():
        updated_key = f'{parent_key}{separator}{key}' if parent_key else key

        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, updated_key, separator))
        else:
            flattened_dict[updated_key] = value

    if flattened_dict is None or not flattened_dict:
        raise Exception("Config tree is empty")

    return flattened_dict

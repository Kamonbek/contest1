def typeBasedTransformer(**kwargs):
    transformed = {}
    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Square numbers
            transformed[key] = value ** 2
        elif isinstance(value, str):  # Reverse strings
            transformed[key] = value[::-1]
        elif isinstance(value, bool):  # Invert booleans
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):  # Reverse lists/tuples
            transformed[key] = value[::-1]
        elif isinstance(value, dict):  # Swap keys and values in dictionaries
            if len(value) == len(set(value.values())):  # Ensure values are unique
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value  # Leave unchanged if values are not unique
        else:  # Leave unsupported types unchanged
            transformed[key] = value

    return transformed

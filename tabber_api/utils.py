def parse_bool_query_param(value):
    if isinstance(value, str):
        lower = value.lower()
        if lower == 'true':
            return True
        elif lower == 'false':
            return False
        
    return None
import re

def filter_datum(fields, redaction, message, separator):
    pattern = f"({'|'.join([f'{field}=[^\\{separator}]*' for field in fields])})"
    return re.sub(pattern, lambda m: m.group(0).split('=')[0] + f'={redaction}', message)


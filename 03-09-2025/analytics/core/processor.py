from .validator import validate_data

def process_data(data):
    if validate_data(data):
        return f'Processed Data :{data}'
    return 'invalid data'
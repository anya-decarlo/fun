EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 30

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
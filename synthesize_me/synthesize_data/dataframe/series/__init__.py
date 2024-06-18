from .decimal.add_normal_noise import add_normal_noise
from .integer.add_normal_noise_and_round import add_normal_noise_and_round
from .numberlist.random_shuffle import random_shuffle

def synthesize_series(series, metadata):
    
    datatype = metadata['datatype']
    method = metadata['method']

    if datatype == 'Decimal' and method == 'add_normal_noise':
        return add_normal_noise(series, metadata['dispersion_amount'])
    
    elif datatype == 'Integer' and method == 'add_normal_noise_and_round':
        return add_normal_noise_and_round(series, metadata['dispersion_amount'])
    
    elif datatype == 'NumberList' and method == 'random_shuffle':
        return random_shuffle(series, metadata['p_modify_number_list_val'])


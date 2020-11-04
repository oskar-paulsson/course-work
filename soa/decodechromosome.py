import numpy as np

class DecodingOperator:
    def __init__(self):
        pass

    def RangedBinaryDecoding(self, chromosome, n_variables, variable_range):

        x = np.zeros(n_variables)
        d = variable_range
        var_length = int(len(chromosome)/n_variables)
        k = np.linspace(1,var_length,var_length).astype('int')

        for i in range(n_variables):
            interval = np.linspace(i*var_length + 1, i*var_length + var_length, var_length).astype('int')

            term = np.sum(chromosome[interval-1]*(1/2**(k)))
            term2 = -variable_range + 2*variable_range*term/(1-(1/2**(var_length)))
            x[i] = np.copy(term2)

        return x

    def FractionalBinaryDecoding(self, chromosome, n_variables, coefficient):

        x = np.zeros(n_variables)
        d = coefficient
        var_length = int(len(chromosome)/n_variables)
        k = np.linspace(1, var_length, var_length).astype('int')

        for i in range(n_variables):
            interval = np.linspace(i*var_length + 1, i*var_length + var_length, var_length).astype('int')

            term = np.sum(chromosome[interval-1]*(1/2**(k)))
            x[i] = np.copy(coefficient*term)

        return x

def DecodeChromosome(chromosome, scheme='fractional', variable_range=0, n_variables=1, coefficient=1):
    """
    The DecodeChromosome method is used to decode a given individual, using a chosen
    decoding-scheme into a real-valued variable. The default scheme is FRACTIONAL
    which computes a finite geometric sum c/(2^k) where c is 1 by default.

    When using RANGED, the user MUST set the variable range, otherwise all evaluations
    will be 0.

        # Arguments:
            chromosome: is a list of elements, binary or real valued
            scheme: string, select FRACTIONAL or RANGED
            variable_range: single digit, float or otherwise, denotes the upper and lower limit
            of the RANGED-decoder
            n_variables: the number of variables the decoder will output
            coefficient: multiplier for the FRACTIONAL decoder

        # returns:
            x: decoded variable
    """
    operator = DecodingOperator()

    if scheme.lower() == 'fractional':
        x = operator.FractionalBinaryDecoding(chromosome, n_variables, coefficient)

    if scheme.lower() == 'ranged':
        x = operator.RangedBinaryDecoding(chromosome, n_variables, coefficient)

    return x

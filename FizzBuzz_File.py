import numpy as np

def FizzBuzz(start, finish):

    v = np.arange(start, finish + 1, dtype=object)

    fizz = (v % 3 == 0)
    buzz = (v % 5 == 0)

    v[fizz & ~buzz] = 'fizz'
    v[buzz & ~fizz] = 'buzz'
    v[fizz & buzz] = 'fizzbuzz'

    return list(v)

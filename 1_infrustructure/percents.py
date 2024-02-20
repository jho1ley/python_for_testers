__author__ = 'jholley'

def percents(x, y):
    """What percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    return result

def print_percents(x, y):
    """Print what percentage of x is y"""
    print(str(y) + ' is ' + str(int(percents(x, y))) + '% of ' + str(x))


x = 10
y = 1
print_percents(x,y)
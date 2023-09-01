# Cria uma calculadora de soma para interação ao usuario:
from sys import argv

class Sum:
    def __init__(self):
        pass

    def main():
        if argv[3] == 'sum':
            return print(float(argv[1]) + float(argv[2]))


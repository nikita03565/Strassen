import random
from datetime import datetime
random.seed(datetime.now())


def generate_and_save(n, name):
    matrix_a = create_random_matrix(n)
    save_matrix(matrix_a, name + "%i.in" % n, n)


def create_random_matrix(n):
    max_val = 1000
    matrix = []
    for i in range(n):
        matrix.append([random.randint(0, max_val) for _ in range(n)])
    return matrix


def save_matrix(matrix_a, filename, n):
    f = open(filename, 'w')
    f.write(str(n) + "\n")
    for i, matrix in enumerate([matrix_a]):
        if i != 0:
            f.write("\n")
        for line in matrix:
            f.write("\t".join(map(str, line)) + "\n")


for i in range(100, 4000, 100):
    print(i)
    generate_and_save(i, 'a')
    generate_and_save(i, 'b')

from fractions import Fraction

import random
import sys


def x(m: Fraction) -> Fraction:
    return (1 - m**2) / (m**2 + 1)


def y(m: Fraction, xn: Fraction) -> Fraction:
    return m * (xn + 1)


def main(triplet_quatity: int) -> set[tuple[Fraction, ...]]:
    triplets = set()

    while len(triplets) < triplet_quatity:
        m = Fraction(random.randint(1, triplet_quatity),
                     random.randint(1, triplet_quatity))
        xn = x(m)
        yn = y(m, xn)
        zn = xn**2 + yn**2
        if xn == 0 or yn == 0:
            continue
        triplets.add((xn, yn, zn))

    return triplets


if __name__ == '__main__':
    if len(sys.argv) < 2:
        user_input = input("Cuantas ternas pitagoricas deseas? ")
    else:
        user_input = sys.argv[1]
    triplets = main(int(user_input))
    for xn, yn, zn in triplets:
        print(f"{xn}, {yn}, {zn}")

from fractions import Fraction

import random
import sys


def x(m: Fraction) -> Fraction:
    return (1 - m**2) / (m**2 + 1)


def y(m: Fraction, xn: Fraction) -> Fraction:
    return m * (xn + 1)


def rational_to_int_triplet(a: Fraction, b: Fraction, c: Fraction) -> tuple[int]:  # noqa: E501
    """
    Converts a rational "pythagorean" triplet to a integer pythagorean triplet
    """
    return a * a.denominator, b * b.denominator, c * a.denominator


def find_tiplet(triplet_quatity: int) -> set[tuple[Fraction, ...]]:
    triplets = set()

    while len(triplets) < triplet_quatity:
        m = Fraction(random.randint(1, triplet_quatity),
                     random.randint(1, triplet_quatity))
        xn = x(m)
        yn = y(m, xn)
        zn = xn**2 + yn**2

        if xn <= 0 or yn <= 0:
            continue

        triplets.add(rational_to_int_triplet(xn, yn, zn))

    return triplets


if __name__ == '__main__':
    if len(sys.argv) < 2:
        user_input = input("Cuantas ternas pitagoricas deseas? ")
    else:
        user_input = sys.argv[1]
    triplets = find_tiplet(int(user_input))

    for a, b, c in triplets:
        print(f"{a}, {b}, {c}")

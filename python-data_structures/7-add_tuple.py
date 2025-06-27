#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Get first and second elements of tuple_a, or 0 if missing
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # Get first and second elements of tuple_b, or 0 if missing
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)

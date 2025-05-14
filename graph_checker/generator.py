# Tarasidou Anna
import random


def sequence_generator(order):
    num_list = [random.randint(1, order - 1) for _ in range(order)]
    total = sum(num_list)

    if total % 2 != 0:
        i = random.randint(0, order - 1)
        if num_list[i] < order - 1:
            num_list[i] += 1
        else:
            num_list[i] -= 1

    return num_list

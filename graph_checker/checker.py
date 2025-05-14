# Tarasidou Anna

def is_graphic(sequence):
    new_seq = sequence.copy()
    n = len(new_seq)

    if any(d > n - 1 for d in new_seq):
        return "NO"

    while True:
        new_seq.sort(reverse=True)
        print(new_seq)

        if all(d == 0 for d in new_seq):
            return "YES"
        if any(d < 0 for d in new_seq):
            return "NO"

        d1 = new_seq.pop(0)
        if d1 == 0:
            return "YES"

        for i in range(d1):
            if i >= len(new_seq):
                return "NO"
            new_seq[i] -= 1

        if len(new_seq) == 0:
            return "YES"

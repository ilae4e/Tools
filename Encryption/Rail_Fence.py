
__author__ = "georg" \
             "From: Stackoverflow.com" \
             "available at: http://stackoverflow.com/a/14520203"

def fence(string, num_rails):
    fence = [[None] * len(string) for n in range(num_rails)]
    rails = range(num_rails - 1) + range(num_rails - 1, 0, -1)
    for n, x in enumerate(string):
        fence[rails[n % len(rails)]][n] = x

    if 0:  # debug
        for rail in fence:
            print ''.join('.' if c is None else str(c) for c in rail)

    return [c for rail in fence for c in rail if c is not None]


def encrypt(string, num_rails):
    return ''.join(fence(string, num_rails))


def decrypt(string, num_rails):
    rng = range(len(string))
    pos = fence(rng, num_rails)
    return ''.join(string[pos.index(n)] for n in rng)

DIMS: int = 2
BITS_PER_DIM: int = 16
MAX: int = DIMS ** BITS_PER_DIM - 1


def hilbert(x: int, y: int) -> int:
    # assert 0 <= x <= MAX
    # assert 0 <= y <= MAX
    return _hilbert(x, y)


# Based on public domain code at https://github.com/rawrunprotected/hilbert_curves
cdef inline unsigned int _hilbert(unsigned int x, unsigned int y):
    cdef unsigned int a, b, c, d
    a = x ^ y
    b = 0xFFFF ^ a
    c = 0xFFFF ^ (x | y)
    d = x & (y ^ 0xFFFF)

    cdef unsigned int A, B, C, D
    A = a | (b >> 1)
    B = (a >> 1) ^ a
    C = ((c >> 1) ^ (b & (d >> 1))) ^ c
    D = ((a & (c >> 1)) ^ (d >> 1)) ^ d

    a = A
    b = B
    c = C
    d = D
    A = (a & (a >> 2)) ^ (b & (b >> 2))
    B = (a & (b >> 2)) ^ (b & ((a ^ b) >> 2))
    C ^= (a & (c >> 2)) ^ (b & (d >> 2))
    D ^= (b & (c >> 2)) ^ ((a ^ b) & (d >> 2))

    a = A
    b = B
    c = C
    d = D
    A = (a & (a >> 4)) ^ (b & (b >> 4))
    B = (a & (b >> 4)) ^ (b & ((a ^ b) >> 4))
    C ^= (a & (c >> 4)) ^ (b & (d >> 4))
    D ^= (b & (c >> 4)) ^ ((a ^ b) & (d >> 4))

    a = A
    b = B
    c = C
    d = D
    C ^= (a & (c >> 8)) ^ (b & (d >> 8))
    D ^= (b & (c >> 8)) ^ ((a ^ b) & (d >> 8))

    a = C ^ (C >> 1)
    b = D ^ (D >> 1)

    cdef unsigned int i0, i1
    i0 = x ^ y
    i1 = b | (0xFFFF ^ (i0 | a))

    return (interleave(i1) << 1) | interleave(i0)


cdef inline unsigned int interleave(unsigned int x):
    x = (x | (x << 8)) & 0x00FF00FF
    x = (x | (x << 4)) & 0x0F0F0F0F
    x = (x | (x << 2)) & 0x33333333
    x = (x | (x << 1)) & 0x55555555
    return x

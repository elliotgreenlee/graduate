# Solves the extended Euclidian algorithm as described on
# Wikipedia's Extended Euclidian algorithm page
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd_ab, x, y = extended_gcd(b % a, a)
        return gcd_ab, y - (b // a) * x, x


# Computes the inverse mod a number as described on Wikipedia's
# modular multiplicative inverse page. Returns none if numbers are not co-prime
def inverse_mod(num, mod):
    gcd_ab, x, _ = extended_gcd(num, mod)
    if gcd_ab == 1:
        return x % mod

print inverse_mod(7, 3120)
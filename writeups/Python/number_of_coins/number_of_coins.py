def number_of_coins(info):
    """
    Solves the system of modular congruences using the Chinese Remainder Theorem (CRT).

    Given multiple equations of the form:
        a ≡ ai (mod mi)
    This function finds the smallest positive integer 'a' that satisfies all the given constraints.

    Optimized approach:
    - Uses the Extended Euclidean Algorithm to find modular inverses instead of brute-force iteration.
    - Updates the modulus `m0` iteratively using LCM to ensure correctness.
    
    Parameters:
    -----------
    info : list of tuples (ai, mi)
        Each tuple represents a congruence of the form `a ≡ ai (mod mi)`.
    
    Returns:
    --------
    int or None:
        - Returns the smallest possible value of `a` satisfying all given congruences.
        - Returns `None` if no solution exists.
    """

    if len(info) == 1:
        return info[0][0]  # If only one congruence, return ai directly.

    a, m0 = info[0]  # Initial values

    for ai, mi in info[1:]:
        g = gcd(m0, mi)  # Compute GCD of moduli

        # If (ai - a) is not divisible by GCD, no solution exists
        if (ai - a) % g != 0:
            return None
        
        # Solve m0 * x ≡ (ai - a) (mod mi) using Extended Euclidean Algorithm
        _, x, _ = extended_gcd(m0, mi)

        # Scale x to adjust for (ai - a)
        x *= (ai - a) // g
        mi_g = mi // g  # Reduce modulus for next iteration

        # Update `a` to the correct solution for current congruence
        a += x * m0
        a %= mi_g * m0  # Keep `a` in the correct range (smallest solution)

        # Update `m0` to LCM for the next iteration
        m0 = lcm(m0, mi)

    return a


def gcd(a, b):
    """Computes the Greatest Common Divisor (GCD) using the Euclidean Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes the Least Common Multiple (LCM) using the relationship: LCM(a, b) = |a * b| / GCD(a, b)."""
    return abs(a * b) // gcd(a, b)


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm:
    Given integers `a` and `b`, finds `x` and `y` such that:
        a * x + b * y = gcd(a, b)

    Returns:
    --------
    (gcd, x, y) : tuple
        - gcd(a, b)
        - x and y such that a*x + b*y = gcd(a, b).
    """
    if b == 0:
        return (a, 1, 0)  # Base case: gcd(a, 0) = a

    g, x1, y1 = extended_gcd(b, a % b)  # Recursive step
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

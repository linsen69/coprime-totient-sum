#!/usr/bin/env python3
"""
verify.py
=========

Independent numerical checks for the note

    "Asymptotic Evaluation of a Coprime Two-Parameter Totient Sum"

The quantity is

    W(J) = sum_{1 <= u,a <= J, gcd(u,a)=1} 1 / phi(4*u*a)

and the proposed/proved asymptotic in PROOF.md is

    W(J) ~ (9 / (2*pi^2)) * (log J)^2.

What this script checks
-----------------------
1. A fast O(J log J) evaluation of W(J), based on Möbius inversion.
2. An independent brute-force exact Fraction check for a small J.
3. The Euler-product constant

       (3/8) * product_{p>2} (1 + 1/p^2)

   against 9/(2*pi^2).
4. The observed ratios W(J)/(log J)^2 for selected J.

This script is a FINITE NUMERICAL VERIFIER.  It is not a substitute for the
analytic proof in PROOF.md and it does not prove the Erdős-Straus conjecture.

Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction
from typing import Iterable, List


TARGET = 9.0 / (2.0 * math.pi * math.pi)


def phi_sieve(n: int) -> List[int]:
    """Euler phi for every 0 <= m <= n."""
    phi = list(range(n + 1))
    if n >= 1:
        phi[1] = 1
    for p in range(2, n + 1):
        if phi[p] == p:  # prime
            for k in range(p, n + 1, p):
                phi[k] -= phi[k] // p
    return phi


def mobius_sieve(n: int) -> List[int]:
    """Möbius mu(m) for every 0 <= m <= n."""
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    if n >= 0:
        mu[0] = 0
    if n >= 1:
        is_prime[0] = is_prime[1] = False

    # Multiply by -1 for every distinct prime divisor.
    for p in range(2, n + 1):
        if is_prime[p]:
            for k in range(p, n + 1, p):
                is_prime[k] = False if k != p else is_prime[k]
                mu[k] *= -1
            pp = p * p
            if pp <= n:
                for k in range(pp, n + 1, pp):
                    mu[k] = 0

    # The primality marking above is intentionally simple but correct:
    # composites are marked when their smallest prime is processed.
    return mu


def mobius_sieve_linear(n: int) -> List[int]:
    """Linear-time Möbius sieve; used by the main verifier."""
    mu = [0] * (n + 1)
    if n >= 1:
        mu[1] = 1

    primes: List[int] = []
    composite = [False] * (n + 1)

    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1

        for p in primes:
            v = i * p
            if v > n:
                break
            composite[v] = True

            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]

    return mu


def w_fast(J: int, phi: List[int] | None = None, mu: List[int] | None = None) -> float:
    """
    Compute W(J) in O(J log J) using Möbius inversion.

    Under gcd(u,a)=1, u and a cannot both be even.  Also:

      if u,a are odd:
          phi(4ua) = 2 phi(u) phi(a)

      if exactly one of u,a is even:
          phi(4ua) = 4 phi(u) phi(a).

    Therefore

      W = (1/2) S_oo + (1/2) S_eo,

    where
      S_oo = sum_{u,a odd, gcd=1} 1/(phi(u)phi(a)),
      S_eo = sum_{u even, a odd, gcd=1} 1/(phi(u)phi(a)).

    Möbius inversion,
      1_{gcd(u,a)=1} = sum_{d|u,d|a} mu(d),
    reduces both double sums to sums over odd d.
    """
    if J < 1:
        return 0.0

    if phi is None:
        phi = phi_sieve(J)
    if mu is None:
        mu = mobius_sieve_linear(J)

    soo = 0.0
    seo = 0.0

    for d in range(1, J + 1, 2):  # d must be odd
        md = mu[d]
        if md == 0:
            continue

        odd_sum = 0.0
        even_sum = 0.0

        for n in range(d, J + 1, d):
            term = 1.0 / phi[n]
            if n & 1:
                odd_sum += term
            else:
                even_sum += term

        soo += md * odd_sum * odd_sum
        seo += md * even_sum * odd_sum

    return 0.5 * (soo + seo)


def w_bruteforce_exact(J: int) -> Fraction:
    """
    Independent exact check using Fraction and direct gcd testing.

    This intentionally does NOT use Möbius inversion.
    Keep J small (roughly <= 40 is comfortable).
    """
    phi = phi_sieve(J)
    total = Fraction(0, 1)

    for u in range(1, J + 1):
        for a in range(1, J + 1):
            if math.gcd(u, a) != 1:
                continue

            # Since gcd(u,a)=1, both cannot be even.
            if (u & 1) and (a & 1):
                denominator = 2 * phi[u] * phi[a]
            else:
                denominator = 4 * phi[u] * phi[a]

            total += Fraction(1, denominator)

    return total


def primes_up_to(n: int) -> Iterable[int]:
    """Simple Eratosthenes sieve."""
    if n < 2:
        return []

    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"

    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)

    return (i for i in range(2, n + 1) if sieve[i])


def euler_constant_partial(prime_cutoff: int) -> float:
    """
    Partial Euler product

        H(0,0) = (3/8) prod_{p>2} (1 + 1/p^2).

    As prime_cutoff -> infinity this tends to 9/(2*pi^2).
    """
    value = 3.0 / 8.0
    for p in primes_up_to(prime_cutoff):
        if p > 2:
            value *= 1.0 + 1.0 / (p * p)
    return value


def parse_j_values(raw: str) -> List[int]:
    values: List[int] = []
    for piece in raw.split(","):
        piece = piece.strip()
        if not piece:
            continue
        j = int(piece)
        if j < 2:
            raise ValueError("Every J must be >= 2.")
        values.append(j)
    if not values:
        raise ValueError("At least one J value is required.")
    return sorted(set(values))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Numerically verify the totient-sum asymptotic in PROOF.md."
    )
    parser.add_argument(
        "--j-values",
        default="100,300,1000,3000",
        help="Comma-separated J values (default: 100,300,1000,3000).",
    )
    parser.add_argument(
        "--prime-cutoff",
        type=int,
        default=100000,
        help="Prime cutoff for the partial Euler product (default: 100000).",
    )
    parser.add_argument(
        "--exact-check",
        type=int,
        default=25,
        help="Run an independent exact brute-force check at this J; 0 disables it (default: 25).",
    )
    args = parser.parse_args()

    js = parse_j_values(args.j_values)
    max_j = max(js)

    print("=" * 76)
    print("Coprime two-parameter totient sum verifier")
    print("=" * 76)
    print()
    print("Target asymptotic constant:")
    print(f"  A = 9/(2*pi^2) = {TARGET:.15f}")
    print()

    # 1. Euler product check.
    partial = euler_constant_partial(args.prime_cutoff)
    print(f"Euler-product check through primes <= {args.prime_cutoff:,}:")
    print(f"  partial product = {partial:.15f}")
    print(f"  target          = {TARGET:.15f}")
    print(f"  difference      = {partial - TARGET:+.3e}")
    print()

    # 2. Build arithmetic tables once.
    phi = phi_sieve(max(max_j, args.exact_check))
    mu = mobius_sieve_linear(max_j)

    # 3. Independent small-J exact cross-check.
    if args.exact_check:
        j0 = args.exact_check
        exact = w_bruteforce_exact(j0)
        fast = w_fast(j0, phi=phi, mu=mobius_sieve_linear(j0))
        exact_float = float(exact)

        print(f"Independent exact cross-check at J={j0}:")
        print(f"  brute-force Fraction = {exact}")
        print(f"  brute-force decimal  = {exact_float:.15f}")
        print(f"  Möbius fast value    = {fast:.15f}")
        print(f"  absolute difference  = {abs(exact_float - fast):.3e}")

        tolerance = 5e-12 * max(1.0, abs(exact_float))
        if abs(exact_float - fast) > tolerance:
            raise SystemExit("ERROR: fast and brute-force computations disagree.")
        print("  status               = PASS")
        print()

    # 4. W(J) asymptotic table.
    print("Asymptotic check:")
    print(
        f"{'J':>10}  {'W(J)':>18}  {'W/log^2 J':>16}  "
        f"{'ratio - A':>14}  {'ratio/ A':>10}"
    )
    print("-" * 76)

    for J in js:
        w = w_fast(J, phi=phi, mu=mu)
        logj = math.log(J)
        ratio = w / (logj * logj)
        print(
            f"{J:10,d}  {w:18.12f}  {ratio:16.12f}  "
            f"{ratio - TARGET:+14.9f}  {ratio / TARGET:10.6f}"
        )

    print()
    print("Interpretation:")
    print("  The normalized ratio should approach 9/(2*pi^2) as J grows.")
    print("  Finite numerical agreement supports the calculation but is not a proof.")
    print("  The analytic argument is contained in PROOF.md.")


if __name__ == "__main__":
    main()

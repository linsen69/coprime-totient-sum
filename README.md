# A Coprime Two-Parameter Totient Sum

An exact leading constant for a totient sum arising in the study of the Erdős–Straus conjecture.

## Main result

For a positive integer $J$, define

```math
W(J)=\sum_{\substack{1\le u,a\le J\\ \gcd(u,a)=1}}
\frac{1}{\varphi(4ua)},
```

where $\varphi$ is Euler's totient function and $\log$ denotes the natural logarithm. Then

```math
\boxed{
W(J)=\left(\frac{9}{2\pi^2}+o(1)\right)(\log J)^2
}
\qquad (J\to\infty).
```

The leading constant is $9/(2\pi^2)=0.45594532639052\ldots$. In particular, **$W(J)\ge 0.45(\log J)^2$ for all sufficiently large $J$**.

[Read the complete proof →](PROOF.md)

## Why this sum matters

In [Benjamin Dahan's 2026 preprint](https://arxiv.org/abs/2608.24035), Lemma 4.22 gives

```math
W(J)\ge
\left(\frac{3}{2\pi^2}+o(1)\right)(\log J)^2.
```

Section 7 asks for a lower-bound coefficient of at least $0.45$. The result above supplies that bound and identifies the exact leading constant, which is three times the coefficient in Lemma 4.22.

This is a result about the arithmetic sum $W(J)$. It does not resolve the Erdős–Straus conjecture.

## How the proof works

The argument has three steps:

1. **Separate the prime contributions.** Coprimality allows a prime to divide either parameter, but not both. The prime $2$ is treated separately because the denominator contains the fixed factor $4$.
2. **Factor out the logarithmic growth.** Write the two-variable Dirichlet series as $F(s,t)=\zeta(1+s)\zeta(1+t)H(s,t)$ and prove that the coefficients of $H$ are absolutely summable.
3. **Recover the partial sums.** A convolution with two harmonic sums and dominated convergence identifies the leading constant as $H(0,0)$.

The constant simplifies to

```math
H(0,0)
=\frac38\prod_{p>2}\left(1+\frac1{p^2}\right)
=\frac38\cdot\frac{\zeta(2)/\zeta(4)}{1+2^{-2}}
=\frac9{2\pi^2}.
```

The proof includes the convergence argument needed to pass from the Euler product to the asymptotic formula.

## Numerical illustration

The following values were recomputed by summing over coprime pairs:

| $J$ | $W(J)$ | $W(J)/(\log J)^2$ |
| ---: | ---: | ---: |
| 100 | 13.317254584 | 0.627947497 |
| 300 | 19.358190414 | 0.595029981 |
| 1,000 | 27.253212761 | 0.571141634 |
| 3,000 | 35.614356280 | 0.555589526 |
| Limit as $J\to\infty$ | — | **0.455945326…** |

For a small exact check,

```math
W(25)=\frac{13932881}{1900800}
=7.330008943602693\ldots.
```

This value agrees in exact rational arithmetic between direct evaluation of $\varphi(4ua)$ and the coprime factorization formula given in the [proof's numerical note](PROOF.md#numerical-note).

The finite values illustrate the approach to the limit; the asymptotic statement is established by the proof.

## Files and background

- [README.md](README.md) — result, context, and numerical illustration.
- [PROOF.md](PROOF.md) — self-contained derivation and the $0.45$ corollary.

This note records a derivation developed with ChatGPT assistance on September 10, 2026. It makes no claim of literature priority.

**Reference:** Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, $n\equiv1\pmod{24}$*, arXiv:2608.24035 (2026). [Abstract](https://arxiv.org/abs/2608.24035) · [Full text](https://arxiv.org/html/2608.24035v1)

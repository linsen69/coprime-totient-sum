# A Coprime Two-Parameter Totient Sum

This repository records an independently checkable, AI-assisted derivation concerning the arithmetic sum

```math
W(J)
=
\sum_{\substack{1\le u,a\le J\\(u,a)=1}}
\frac{1}{\varphi(4ua)}.
```

The main claim proved in `PROOF.md` is

```math
\boxed{
W(J)
\sim
\frac{9}{2\pi^2}(\log J)^2
}
\qquad (J\to\infty).
```

Equivalently,

```math
\boxed{
\lim_{J\to\infty}
\frac{W(J)}{(\log J)^2}
=
\frac{9}{2\pi^2}
}
```

with

```math
\frac{9}{2\pi^2}
=
0.45594532639052\ldots
>
0.45.
```

Therefore the asymptotic implies

```math
W(J)
\ge
(0.45+o(1))(\log J)^2.
```

## Why this is of interest

Benjamin Dahan's 2026 preprint

> *Sieve dimension and search depth for the Erdős–Straus conjecture,  
> n ≡ 1 (mod 24)*  
> arXiv:2608.24035

studies this sum in connection with the Erdős–Straus conjecture.

The paper gives the lower bound

```math
W(J)
\ge
\left(
\frac{3}{2\pi^2}+o(1)
\right)(\log J)^2
```

and asks whether one can establish a coefficient of at least `0.45`.

The derivation in this repository gives the candidate exact leading constant

```math
\boxed{
\frac{9}{2\pi^2}
=
0.45594532639052\ldots
}.
```

This also explains why numerical experiments suggest a limiting coefficient close to `0.46`.

## Proof idea

The proof introduces the two-variable Dirichlet series

```math
F(s,t)
=
\sum_{\substack{u,a\ge1\\(u,a)=1}}
\frac{u^{-s}a^{-t}}{\varphi(4ua)}
```

and factors it as

```math
F(s,t)
=
\zeta(1+s)\zeta(1+t)H(s,t).
```

For every odd prime $p$, the regular Euler factor satisfies

```math
H_p(0,0)
=
1+\frac1{p^2},
```

while the special factor at $p=2$ is

```math
H_2(0,0)=\frac38.
```

Hence

```math
H(0,0)
=
\frac38
\prod_{p>2}
\left(1+\frac1{p^2}\right).
```

Using

```math
\prod_p
\left(1+\frac1{p^2}\right)
=
\frac{\zeta(2)}{\zeta(4)}
=
\frac{15}{\pi^2},
```

we obtain

```math
\prod_{p>2}
\left(1+\frac1{p^2}\right)
=
\frac{12}{\pi^2},
```

and therefore

```math
\boxed{
H(0,0)
=
\frac38\cdot\frac{12}{\pi^2}
=
\frac9{2\pi^2}.
}
```

The remaining part of the proof justifies passing from this regular Euler product to the partial-sum asymptotic using absolute convergence and dominated convergence.

See [`PROOF.md`](PROOF.md) for the complete derivation.

## Numerical verification

`verify.py` provides an independent finite numerical check.

It uses only the Python standard library and performs:

- a direct exact `Fraction` computation for a small value of $J$;
- an independent Möbius-inversion computation of $W(J)$;
- a partial Euler-product check of the constant;
- numerical evaluation of $W(J)/(\log J)^2$ for increasing $J$.

Run:

```bash
python verify.py
```

A typical exact cross-check is:

```text
Independent exact cross-check at J=25:
  brute-force decimal  = 7.330008943602693
  Möbius fast value    = 7.330008943602693
  absolute difference  = 0.000e+00
  status               = PASS
```

The default asymptotic check evaluates

```text
J = 100, 300, 1000, 3000
```

and compares the normalized values with

```text
9/(2*pi^2) = 0.455945326390520...
```

Finite numerical checks support the calculation, but they are **not** a substitute for the analytic proof.

## Repository contents

```text
.
├── README.md
├── PROOF.md
├── verify.py
└── PROVENANCE.md
```

`PROOF.md` contains the mathematical argument.

`verify.py` contains independent numerical checks.

`PROVENANCE.md` may be used to record the public provenance and timestamp trail of the derivation.

## Status and limitations

This repository does **not** claim to prove the Erdős–Straus conjecture.

The result here concerns one analytic arithmetic sum used inside a broader sieve approach.

In particular, this repository does not establish:

- the Erdős–Straus conjecture;
- a finite universal search depth;
- emptiness of the remaining exceptional set;
- termination of a Type I / Type II decomposition procedure;
- literature priority over unpublished or independently developed work.

The proof should be independently reviewed before being treated as an established mathematical result.

## Provenance

The derivation was produced during an AI-assisted mathematical investigation using ChatGPT on September 10, 2026.

The purpose of this repository is to make the derivation and numerical checks publicly inspectable and reproducible.

No personal identity is required for the mathematical content of the repository.

**No claim of literature priority is made until independent mathematical review and a broader prior-art search have been completed.**

If an error is found, it should be documented publicly and the repository corrected transparently.

## Reference

Benjamin Dahan,  
*Sieve dimension and search depth for the Erdős–Straus conjecture, n ≡ 1 (mod 24)*,  
arXiv:2608.24035, 2026.

---

### Core claim

```math
\boxed{
W(J)
\sim
\frac{9}{2\pi^2}(\log J)^2
}
```

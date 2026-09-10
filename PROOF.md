# Asymptotic Evaluation of a Coprime Two-Parameter Totient Sum

[← Overview](README.md)

## Abstract

We evaluate the leading term of the sum of $1/\varphi(4ua)$ over coprime positive integers $u,a\le J$. The result is

```math
W(J)\sim\frac9{2\pi^2}(\log J)^2.
```

The proof factors a two-variable Dirichlet series into two zeta factors and an Euler product with absolutely summable coefficients. A harmonic-sum convolution then gives the asymptotic formula by dominated convergence.

## 1. Theorem and notation

Throughout, $u,a,d,e,m,n$ are positive integers, $p$ denotes a prime, $\varphi$ is Euler's totient function, and $\log$ is the natural logarithm.

**Theorem.** For positive integers $J\to\infty$,

```math
W(J):=\sum_{\substack{1\le u,a\le J\\ \gcd(u,a)=1}}
\frac1{\varphi(4ua)}
=
\left(\frac9{2\pi^2}+o(1)\right)(\log J)^2.
```

The same statement holds for real $J\to\infty$, since the sum depends only on $\lfloor J\rfloor$.

## 2. The Dirichlet series and its Euler factors

For $\Re s>0$ and $\Re t>0$, define

```math
F(s,t)=
\sum_{\substack{u,a\ge1\\ \gcd(u,a)=1}}
\frac{u^{-s}a^{-t}}{\varphi(4ua)}.
```

Coprimality means that each prime divides at most one of $u$ and $a$. Multiplicativity of $\varphi$, with the fixed factor $4$ assigned to the prime $2$, gives

```math
F(s,t)=L_2(s,t)\prod_{p>2}L_p(s,t).
```

### Odd primes

For $p>2$, put $x=p^{-1-s}$ and $y=p^{-1-t}$. Since $\varphi(p^r)=p^{r-1}(p-1)$ for $r\ge1$,

```math
L_p(s,t)
=1+\sum_{r\ge1}\frac{p^{-rs}}{\varphi(p^r)}
  +\sum_{r\ge1}\frac{p^{-rt}}{\varphi(p^r)}
=1+\frac{p}{p-1}\left(\frac{x}{1-x}+\frac{y}{1-y}\right).
```

### The prime 2

If both parameters are odd, the $2$-part contributes $1/\varphi(4)=1/2$. If $2^r$ divides exactly one parameter, its contribution is $1/\varphi(2^{r+2})=2^{-r-1}$.

Thus, with $x=2^{-1-s}$ and $y=2^{-1-t}$,

```math
L_2(s,t)=\frac12\left(1+\frac{x}{1-x}+\frac{y}{1-y}\right).
```

For real $\sigma,\tau>0$, the odd-prime factors satisfy
$L_p(\sigma,\tau)-1=O(p^{-1-\sigma}+p^{-1-\tau})$.
Their product therefore converges. Expanding finite prime products and taking an increasing limit proves convergence of the positive coefficient sum. Taking $\sigma=\Re s$ and $\tau=\Re t$ also establishes absolute convergence of $F(s,t)$ and justifies its Euler product in the stated region.

## 3. Factoring out the two zeta functions

Define $H$ by

```math
F(s,t)=\zeta(1+s)\zeta(1+t)H(s,t).
```

Multiplying each local factor by $(1-p^{-1-s})(1-p^{-1-t})$ gives, for $p>2$,

```math
\begin{aligned}
H_p(s,t)
&=(1-x)(1-y)
  +\frac{p}{p-1}\bigl[x(1-y)+y(1-x)\bigr]\\
&=1+\frac{x+y}{p-1}-\frac{p+1}{p-1}xy\\
&=1+\frac{p^{-1-s}+p^{-1-t}}{p-1}
  -\frac{p+1}{p-1}p^{-2-s-t}.
\end{aligned}
```

At the prime $2$,

```math
H_2(s,t)
=\frac12\bigl[(1-x)(1-y)+x(1-y)+y(1-x)\bigr]
=\frac12(1-2^{-2-s-t}).
```

Consequently,

```math
H(s,t)=H_2(s,t)\prod_{p>2}H_p(s,t).
```

## 4. Absolute summability of the coefficients

We need absolute convergence of the coefficient series, not merely a value of the Euler product at the origin. This follows directly from the local polynomials.

Write

```math
H_p(s,t)
=1+\alpha_p p^{-s}+\alpha_p p^{-t}
  +\beta_p p^{-s-t}\qquad(p>2),
```

where

```math
\alpha_p=\frac1{p(p-1)},
\qquad
\beta_p=-\frac{p+1}{p^2(p-1)}.
```

Also, $H_2(s,t)=\frac12-\frac18\,2^{-s-t}$.

Expanding the local polynomials defines coefficients $h(d,e)$. Unique prime factorization makes each local choice unique for a fixed pair $(d,e)$. For any fixed $0<\eta<1/2$, the product of the weighted absolute coefficient sums is

```math
\left(\frac12+\frac{2^{2\eta}}8\right)
\prod_{p>2}
\left(
1+\frac{2p^\eta}{p(p-1)}
+\frac{(p+1)p^{2\eta}}{p^2(p-1)}
\right).
```

The nonconstant terms are $O(p^{-2+\eta}+p^{-2+2\eta})$, whose sum over primes converges. Expanding finite products with nonnegative coefficients and passing to the limit therefore gives

```math
\sum_{d,e\ge1}|h(d,e)|d^\eta e^\eta<\infty.
```

In particular,

```math
H(s,t)=\sum_{d,e\ge1}h(d,e)d^{-s}e^{-t},
\qquad
\sum_{d,e\ge1}|h(d,e)|<\infty.
```

The expansion converges absolutely for $\Re s,\Re t\ge-\eta$ and agrees with the Euler product wherever it was already defined. In particular,

```math
H(0,0)=\sum_{d,e\ge1}h(d,e).
```

## 5. Evaluation of the constant

For each odd prime,

```math
H_p(0,0)
=1+\frac2{p(p-1)}-\frac{p+1}{p^2(p-1)}
=1+\frac1{p^2},
```

while $H_2(0,0)=3/8$. Hence

```math
H(0,0)=\frac38\prod_{p>2}\left(1+\frac1{p^2}\right).
```

Using $1+p^{-2}=(1-p^{-4})/(1-p^{-2})$,

```math
\prod_p\left(1+\frac1{p^2}\right)
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2}.
```

Removing the factor $1+2^{-2}=5/4$ yields

```math
\boxed{
H(0,0)=\frac38\cdot\frac{15/\pi^2}{5/4}
=\frac9{2\pi^2}.
}
```

## 6. Recovering the partial sums

In the region of absolute convergence, the factorization
$F(s,t)=\zeta(1+s)\zeta(1+t)H(s,t)$ gives the coefficient identity

```math
\frac{\mathbf1_{\gcd(u,a)=1}}{\varphi(4ua)}
=\sum_{\substack{dm=u\\ en=a}}\frac{h(d,e)}{mn}.
```

Summing over $u,a\le J$ and defining

```math
\mathcal H(x)=\sum_{1\le n\le x}\frac1n
```

gives the exact identity

```math
W(J)=\sum_{d,e\le J}h(d,e)\mathcal H(J/d)\mathcal H(J/e).
```

For $J\ge3$, set

```math
A_J(d)=
\begin{cases}
\mathcal H(J/d)/\log J,&d\le J,\\
0,&d>J.
\end{cases}
```

For each fixed $d$, the estimate $\mathcal H(x)=\log x+O(1)$ as $x\to\infty$ implies $A_J(d)\to1$. Moreover,

```math
0\le A_J(d)\le\frac{1+\log J}{\log J}\le2
\qquad(J\ge3).
```

Therefore

```math
\frac{W(J)}{(\log J)^2}
=\sum_{d,e\ge1}h(d,e)A_J(d)A_J(e).
```

The summands are bounded in absolute value by $4|h(d,e)|$, a summable majorant by Section 4. Dominated convergence now gives

```math
\lim_{J\to\infty}\frac{W(J)}{(\log J)^2}
=\sum_{d,e\ge1}h(d,e)
=H(0,0)
=\frac9{2\pi^2}.
```

This proves the theorem. $\square$

## 7. The 0.45 lower bound

**Corollary.** There exists $J_0$ such that

```math
W(J)\ge0.45(\log J)^2
\qquad\text{for every }J\ge J_0.
```

Indeed, the normalized sum tends to $9/(2\pi^2)=0.45594532639052\ldots>0.45$. By the definition of a limit, it eventually exceeds $0.45$. $\square$

This implies the asymptotic lower bound
$W(J)\ge(0.45+o(1))(\log J)^2$.
The proof does not specify a numerical value of $J_0$.

## 8. Context and scope

[Dahan's preprint](https://arxiv.org/abs/2608.24035), Lemma 4.22, establishes

```math
W(J)\ge
\left(\frac3{2\pi^2}+o(1)\right)(\log J)^2.
```

Section 6, item (8), gives numerical evidence for a limiting coefficient near $0.46$, and Section 7 asks for a lower-bound coefficient of at least $0.45$. The theorem identifies the exact leading constant and supplies that lower bound.

The argument here concerns only $W(J)$; it does not establish the Erdős–Straus conjecture, an empty exceptional set, or a universal finite search depth. It uses no unproved number-theoretic hypothesis.

## Numerical note

For coprime positive integers $u,a$, multiplicativity gives

```math
\varphi(4ua)=
\begin{cases}
2\varphi(u)\varphi(a),&u,a\text{ both odd},\\
4\varphi(u)\varphi(a),&\text{exactly one of }u,a\text{ even}.
\end{cases}
```

These are the only possibilities under coprimality. This identity permits finite checks using totients only up to $J$.

At $J=25$, direct evaluation of $\varphi(4ua)$ and evaluation using this factorization agree in exact rational arithmetic:

```math
W(25)=\frac{13932881}{1900800}
=7.330008943602693\ldots.
```

Further finite values appear in the [overview](README.md#numerical-illustration). These checks illustrate the formula; the proof of its asymptotic behavior is in Sections 2–6.

## Background and reference

This note records a derivation developed with ChatGPT assistance on September 10, 2026. No claim of literature priority is made.

Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, $n\equiv1\pmod{24}$*, arXiv:2608.24035 (2026). [Abstract](https://arxiv.org/abs/2608.24035) · [Full text](https://arxiv.org/html/2608.24035v1)

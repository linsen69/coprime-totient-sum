# Asymptotic Evaluation of a Coprime Two-Parameter Totient Sum

## Abstract

Define

$$
W(J)
:=
\sum_{\substack{1\le u,a\le J\$u,a)=1}}
\frac{1}{\varphi(4ua)},
$$

where $\varphi$ denotes Euler's totient function.

We prove the asymptotic formula

$$
\boxed{
W(J)
\sim
\frac{9}{2\pi^2}(\log J)^2
}
\qquad (J\to\infty).
$$

In particular,

$$
\frac{9}{2\pi^2}
=
0.45594532639052\ldots>0.45,
$$

and hence

$$
W(J)
\ge
(0.45+o(1))(\log J)^2.
$$

If independently verified, this establishes the specific lower bound proposed as an open quantitative problem in Benjamin Dahan's 2026 preprint on sieve dimension and search depth for the Erdős–Straus conjecture.

This note does **not** prove the Erdős–Straus conjecture.

No claim of literature priority is made here. The argument should be independently checked before being treated as an established result.

---

## 1. Statement of the theorem

### Theorem

Let

$$
W(J)
=
\sum_{\substack{u,a\le J\$u,a)=1}}
\frac1{\varphi(4ua)}.
$$

Then

$$
\boxed{
\lim_{J\to\infty}
\frac{W(J)}{(\log J)^2}
=
\frac9{2\pi^2}.
}
$$

Equivalently,

$$
\boxed{
W(J)
=
\left(
\frac9{2\pi^2}+o(1)
\right)(\log J)^2.
}
$$

The proof proceeds by studying a two-variable Dirichlet series and extracting its two logarithmic poles.

---

# 2. The two-variable Dirichlet series

For complex $s,t$ with initially

$$
\Re s>0,\qquad \Re t>0,
$$

define

$$
F(s,t)
:=
\sum_{\substack{u,a\ge1\$u,a)=1}}
\frac{u^{-s}a^{-t}}{\varphi(4ua)}.
$$

Because of the coprimality condition

$$
(u,a)=1,
$$

a prime may divide $u$, or divide $a$, but cannot divide both.

This produces an Euler product

$$
F(s,t)
=
L_2(s,t)
\prod_{p>2}L_p(s,t),
$$

where the prime $2$ must be treated separately because of the fixed factor $4$ in $\varphi(4ua)$.

---

# 3. Euler factors at odd primes

Let $p>2$ be prime.

If $p^r\Vert u$, with $r\ge1$, then $p\nmid a$, and

$$
\frac1{\varphi(p^r)}
=
\frac1{p^{r-1}(p-1)}.
$$

Therefore

$$
\sum_{r\ge1}
\frac{p^{-rs}}{\varphi(p^r)}
=
\sum_{r\ge1}
\frac{p^{-rs}}{p^{r-1}(p-1)}.
$$

Since

$$
\frac1{p^{r-1}(p-1)}
=
\frac{p}{p-1}p^{-r},
$$

we obtain

$$
\sum_{r\ge1}
\frac{p^{-rs}}{\varphi(p^r)}
=
\frac{p}{p-1}
\sum_{r\ge1}p^{-r(1+s)}.
$$

Summing the geometric series gives

$$
\sum_{r\ge1}
\frac{p^{-rs}}{\varphi(p^r)}
=
\frac{p^{-s}}
{(p-1)(1-p^{-1-s})}.
$$

The corresponding contribution when powers of $p$ occur in $a$ is obtained by replacing $s$ with $t$.

Thus

$$
\boxed{
L_p(s,t)
=
1+
\frac{p^{-s}}
{(p-1)(1-p^{-1-s})}
+
\frac{p^{-t}}
{(p-1)(1-p^{-1-t})}.
}
$$

---

# 4. The Euler factor at $2$

Because

$$
(u,a)=1,
$$

at most one of $u,a$ can be even.

If neither is even, the $2$-part of the denominator is simply

$$
\varphi(4)=2,
$$

giving a contribution

$$
\frac12.
$$

If

$$
2^r\Vert u,\qquad r\ge1,
$$

then

$$
\varphi(4\cdot2^r)
=
\varphi(2^{r+2})
=
2^{r+1}.
$$

Hence the even-$u$ contribution is

$$
\sum_{r\ge1}
\frac{2^{-rs}}{2^{r+1}}
=
\frac12
\sum_{r\ge1}2^{-r(1+s)}.
$$

Therefore

$$
\sum_{r\ge1}
\frac{2^{-rs}}{2^{r+1}}
=
\frac12
\frac{2^{-1-s}}
{1-2^{-1-s}}.
$$

Similarly for $a$. Consequently

$$
\boxed{
L_2(s,t)
=
\frac12
+
\frac12
\frac{2^{-1-s}}{1-2^{-1-s}}
+
\frac12
\frac{2^{-1-t}}{1-2^{-1-t}}.
}
$$

---

# 5. Extracting the two zeta poles

The expected $(\log J)^2$ behavior corresponds to two copies of the pole of the Riemann zeta function at $1$.

Define

$$
H(s,t)
:=
\frac{F(s,t)}
{\zeta(1+s)\zeta(1+t)}.
$$

Thus

$$
\boxed{
F(s,t)
=
\zeta(1+s)\zeta(1+t)H(s,t).
}
$$

We now compute the Euler factors of $H$.

---

## 5.1 Odd-prime factors of $H$

Put

$$
A=p^{-1-s},
\qquad
B=p^{-1-t}.
$$

Then

$$
p^{-s}=pA,\qquad p^{-t}=pB.
$$

Hence

$$
L_p(s,t)
=
1+
\frac{pA}{(p-1)(1-A)}
+
\frac{pB}{(p-1)(1-B)}.
$$

The local Euler factor arising from the two zeta functions is

$$
(1-A)^{-1}(1-B)^{-1}.
$$

Therefore

$$
H_p(s,t)
=
(1-A)(1-B)L_p(s,t).
$$

Expanding gives

$$
H_p(s,t)
=
(1-A)(1-B)
+
\frac{p}{p-1}A(1-B)
+
\frac{p}{p-1}B(1-A).
$$

Collecting terms,

$$
H_p(s,t)
=
1
+
\frac{A+B}{p-1}
-
\frac{p+1}{p-1}AB.
$$

Thus

$$
\boxed{
H_p(s,t)
=
1
+
\frac{p^{-1-s}+p^{-1-t}}{p-1}
-
\frac{p+1}{p-1}p^{-2-s-t}.
}
$$

At

$$
s=t=0,
$$

we have

$$
H_p(0,0)
=
1+
\frac{2/p}{p-1}
-
\frac{p+1}{p-1}\frac1{p^2}.
$$

The nonconstant part is

$$
\frac{2p-(p+1)}
{p^2(p-1)}
=
\frac{p-1}{p^2(p-1)}
=
\frac1{p^2}.
$$

Hence, for every odd prime $p$,

$$
\boxed{
H_p(0,0)=1+\frac1{p^2}.
}
$$

This identity is the main source of the final constant.

---

## 5.2 The factor at $2$

Let

$$
A=2^{-1-s},
\qquad
B=2^{-1-t}.
$$

Then

$$
L_2(s,t)
=
\frac12
+
\frac{A}{2(1-A)}
+
\frac{B}{2(1-B)}.
$$

Thus

$$
H_2(s,t)
=
(1-A)(1-B)L_2(s,t).
$$

Multiplying out,

$$
H_2(s,t)
=
\frac12
\left[
(1-A)(1-B)
+
A(1-B)
+
B(1-A)
\right].
$$

Inside the brackets,

$$
(1-A)(1-B)+A(1-B)+B(1-A)
=
1-AB.
$$

Therefore

$$
\boxed{
H_2(s,t)
=
\frac{1-2^{-2-s-t}}{2}.
}
$$

At $s=t=0$,

$$
H_2(0,0)
=
\frac{1-\frac14}{2}
=
\boxed{\frac38}.
$$

---

# 6. Absolute convergence of the regular Euler product

We must justify that after removing the two zeta poles, $H(s,t)$ is regular around

$$
(s,t)=(0,0).
$$

Choose any fixed

$$
0<\delta<\frac12
$$

and suppose

$$
|\Re s|\le\delta,\qquad
|\Re t|\le\delta.
$$

For an odd prime $p$,

$$
p^{-1-s}
=
O(p^{-1+\delta}),
$$

and similarly

$$
p^{-1-t}
=
O(p^{-1+\delta}).
$$

From the exact formula

$$
H_p(s,t)
=
1
+
\frac{p^{-1-s}+p^{-1-t}}{p-1}
-
\frac{p+1}{p-1}p^{-2-s-t},
$$

we therefore obtain

$$
H_p(s,t)-1
=
O(p^{-2+\delta})
+
O(p^{-2+2\delta}).
$$

Since

$$
2-2\delta>1,
$$

the prime sum

$$
\sum_p
|H_p(s,t)-1|
$$

converges uniformly on a sufficiently small closed neighborhood of $(0,0)$.

Hence the Euler product

$$
H(s,t)
=
H_2(s,t)
\prod_{p>2}H_p(s,t)
$$

converges absolutely and locally uniformly there.

In particular,

$$
H(0,0)
$$

is finite and nonzero.

Moreover, $H$ has an absolutely convergent two-variable Dirichlet expansion in a neighborhood of the origin:

$$
\boxed{
H(s,t)
=
\sum_{d,e\ge1}
h(d,e)d^{-s}e^{-t},
}
$$

with, for some $\eta>0$,

$$
\sum_{d,e\ge1}
|h(d,e)|d^\eta e^\eta
<
\infty.
$$

In particular,

$$
\boxed{
\sum_{d,e\ge1}|h(d,e)|<\infty.
}
$$

This absolute summability will allow us to recover the partial sums without requiring a heavy Tauberian theorem.

---

# 7. Evaluation of $H(0,0)$

We have shown

$$
H(0,0)
=
\frac38
\prod_{p>2}
\left(1+\frac1{p^2}\right).
$$

Use the identity

$$
1+x
=
\frac{1-x^2}{1-x}
$$

with

$$
x=p^{-2}.
$$

Thus

$$
1+\frac1{p^2}
=
\frac{1-p^{-4}}{1-p^{-2}}.
$$

Taking the product over all primes,

$$
\prod_p
\left(1+\frac1{p^2}\right)
=
\frac{\prod_p(1-p^{-4})}
{\prod_p(1-p^{-2})}.
$$

By the Euler products for the zeta function,

$$
\prod_p(1-p^{-4})
=
\frac1{\zeta(4)},
$$

and

$$
\prod_p(1-p^{-2})
=
\frac1{\zeta(2)}.
$$

Therefore

$$
\prod_p
\left(1+\frac1{p^2}\right)
=
\frac{\zeta(2)}{\zeta(4)}.
$$

Using

$$
\zeta(2)=\frac{\pi^2}{6},
\qquad
\zeta(4)=\frac{\pi^4}{90},
$$

we get

$$
\frac{\zeta(2)}{\zeta(4)}
=
\frac{\pi^2/6}{\pi^4/90}
=
\frac{15}{\pi^2}.
$$

The $p=2$ factor of this product is

$$
1+\frac1{2^2}
=
\frac54.
$$

Consequently

$$
\prod_{p>2}
\left(1+\frac1{p^2}\right)
=
\frac{15/\pi^2}{5/4}
=
\frac{12}{\pi^2}.
$$

Hence

$$
H(0,0)
=
\frac38\cdot\frac{12}{\pi^2}.
$$

Therefore

$$
\boxed{
H(0,0)
=
\frac9{2\pi^2}.
}
$$

Numerically,

$$
\boxed{
H(0,0)
=
0.45594532639052\ldots
}
$$

---

# 8. Recovering the partial sums

It remains to show that the value $H(0,0)$ is indeed the leading constant in $W(J)$.

Because

$$
F(s,t)
=
\zeta(1+s)\zeta(1+t)H(s,t),
$$

and

$$
\zeta(1+s)
=
\sum_{m\ge1}\frac{m^{-s}}m,
$$

the coefficient identity associated with the product is

$$
\frac{\mathbf 1_{(u,a)=1}}{\varphi(4ua)}
=
\sum_{\substack{dm=u\\en=a}}
\frac{h(d,e)}{mn}.
$$

Summing over

$$
u,a\le J
$$

gives

$$
W(J)
=
\sum_{d,e\le J}
h(d,e)
\left(
\sum_{m\le J/d}\frac1m
\right)
\left(
\sum_{n\le J/e}\frac1n
\right).
$$

Define the harmonic sum

$$
\mathcal H(x)
:=
\sum_{1\le n\le x}\frac1n,
$$

where the upper bound means $n\le\lfloor x\rfloor$.

Then

$$
\boxed{
W(J)
=
\sum_{d,e\le J}
h(d,e)
\mathcal H(J/d)
\mathcal H(J/e).
}
$$

For every fixed positive integer $d$,

$$
\mathcal H(J/d)
=
\log(J/d)+\gamma+o(1),
$$

and therefore

$$
\frac{\mathcal H(J/d)}{\log J}
\longrightarrow1
$$

as $J\to\infty$.

The same holds for $e$.

Now define

$$
A_J(d)
=
\begin{cases}
\dfrac{\mathcal H(J/d)}{\log J},&d\le J,\$$1ex]
0,&d>J.
\end{cases}
$$

For every fixed $d$,

$$
A_J(d)\longrightarrow1.
$$

Furthermore, for $J\ge3$,

$$
0\le A_J(d)
\le
\frac{\mathcal H(J)}{\log J}.
$$

Since

$$
\mathcal H(J)\le1+\log J,
$$

we have a uniform bound such as

$$
|A_J(d)|\le2
$$

for all sufficiently large $J$.

Therefore

$$
\frac{W(J)}{(\log J)^2}
=
\sum_{d,e\ge1}
h(d,e)A_J(d)A_J(e).
$$

Because

$$
|A_J(d)A_J(e)|\le4
$$

and

$$
\sum_{d,e}|h(d,e)|<\infty,
$$

the dominated convergence theorem for absolutely convergent series applies.

Hence

$$
\lim_{J\to\infty}
\frac{W(J)}{(\log J)^2}
=
\sum_{d,e\ge1}h(d,e).
$$

But by absolute convergence,

$$
\sum_{d,e\ge1}h(d,e)
=
H(0,0).
$$

We already evaluated this quantity:

$$
H(0,0)
=
\frac9{2\pi^2}.
$$

Therefore

$$
\boxed{
\lim_{J\to\infty}
\frac{W(J)}{(\log J)^2}
=
\frac9{2\pi^2}.
}
$$

This proves the theorem.

$$
\boxed{\square}
$$

---

# 9. Immediate corollary

Since

$$
\frac9{2\pi^2}
=
0.45594532639052\ldots
>
0.45,
$$

the theorem immediately implies:

### Corollary

$$
\boxed{
W(J)
\ge
(0.45+o(1))(\log J)^2.
}
$$

Indeed, more strongly,

$$
\boxed{
W(J)
=
(0.45594532639052\ldots+o(1))
(\log J)^2.
}
$$

Thus any argument requiring only the lower bound with coefficient $0.45$ may use the strictly larger asymptotic coefficient

$$
\frac9{2\pi^2}.
$$

---

# 10. Relation to the Erdős–Straus literature

Benjamin Dahan's 2026 preprint

> *Sieve dimension and search depth for the Erdős–Straus conjecture,  
> $n\equiv1\pmod{24}$*,  
> arXiv:2608.24035

studies, among other things, the quantity

$$
W(J)
=
\sum_{\substack{u,a\le J\$u,a)=1}}
\frac1{\varphi(4ua)}.
$$

The paper obtains the lower bound

$$
W(J)
\ge
\left(
\frac{3}{2\pi^2}+o(1)
\right)
(\log J)^2
$$

by a simpler lower-estimate argument.

Its numerical experiments suggest that the actual limiting coefficient is close to $0.46$, and the paper asks whether one can establish at least

$$
W(J)
\ge
(0.45+o(1))(\log J)^2.
$$

The calculation above gives the candidate exact asymptotic coefficient

$$
\boxed{
\frac9{2\pi^2}
=
0.45594532639052\ldots,
}
$$

which explains the observed value near $0.46$.

The factor-of-three difference between

$$
\frac{3}{2\pi^2}
$$

and

$$
\frac9{2\pi^2}
$$

arises naturally once the complete Euler product, including the $2$-adic local factor and the full coprimality structure, is retained.

---

# 11. What this result does and does not establish

This note establishes, subject to independent verification of the argument,

$$
W(J)
\sim
\frac9{2\pi^2}(\log J)^2.
$$

It therefore establishes the requested $0.45$ lower bound if the proof is confirmed.

It does **not** establish:

- the Erdős–Straus conjecture;
- emptiness of the exceptional sets in Dahan's sieve argument;
- a finite universal search depth;
- a termination theorem for Type I or Type II decompositions;
- priority over any unpublished or independently developed proof.

The distinction is important.

This is a result about one analytic arithmetic sum occurring inside a broader approach to the Erdős–Straus conjecture.

---

# 12. Independent verification checklist

A reviewer wishing to check the proof can verify it in the following order.

1. Confirm the Euler factor for every odd prime:

$$
L_p(s,t)
=
1+
\frac{p^{-s}}
{(p-1)(1-p^{-1-s})}
+
\frac{p^{-t}}
{(p-1)(1-p^{-1-t})}.
$$

2. Confirm the special $2$-adic factor:

$$
L_2(s,t)
=
\frac12+
\frac12\frac{2^{-1-s}}{1-2^{-1-s}}
+
\frac12\frac{2^{-1-t}}{1-2^{-1-t}}.
$$

3. After factoring

$$
\zeta(1+s)\zeta(1+t),
$$

verify

$$
H_p(0,0)=1+\frac1{p^2}
\qquad(p>2)
$$

and

$$
H_2(0,0)=\frac38.
$$

4. Verify

$$
\prod_{p>2}
\left(1+\frac1{p^2}\right)
=
\frac{12}{\pi^2}.
$$

5. Therefore check

$$
H(0,0)
=
\frac38\frac{12}{\pi^2}
=
\frac9{2\pi^2}.
$$

6. Check the local convergence estimate

$$
H_p(s,t)-1
=
O(p^{-2+\delta})+
O(p^{-2+2\delta})
$$

for some

$$
0<\delta<\frac12.
$$

7. Use the resulting absolute convergence of the coefficient series of $H$ to justify dominated convergence in the partial-sum identity.

No unproved hypothesis such as the Riemann hypothesis is used.

---

# 13. Provenance and review status

This derivation was produced during an AI-assisted mathematical investigation using ChatGPT on September 10, 2026.

The investigation began from the open quantitative problem concerning

$$
W(J)
=
\sum_{\substack{u,a\le J\$u,a)=1}}
\frac1{\varphi(4ua)}
$$

appearing in recent work on the Erdős–Straus conjecture.

The argument was derived by forming the full two-variable Euler product, retaining the special $2$-adic factor, extracting the two zeta poles, and evaluating the remaining regular Euler product at the origin.

The resulting coefficient is

$$
\boxed{
\frac9{2\pi^2}.
}
$$

This repository is intended to make the derivation publicly inspectable and independently reproducible.

**No claim of literature priority is made until an independent mathematical review and a broader prior-art search have been completed.**

If an error is found, it should be reported publicly and this document should be corrected rather than silently replaced.

---

# Reference

Benjamin Dahan,  
*Sieve dimension and search depth for the Erdős–Straus conjecture, $n\equiv1\pmod{24}$*,  
arXiv:2608.24035, 2026.
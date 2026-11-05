# Hesitant fuzzy sets: formal definition and classroom example

## From single-valued membership to a set of grades

For an ordinary fuzzy set on a universe \(X\), the membership map is

$$\mu_A:X\longrightarrow[0,1].$$

For a hesitant fuzzy set (HFS) on \(X\), use the finite-valued map

$$h_H:X\longrightarrow \mathcal P_f([0,1])\setminus\{\varnothing\},$$

where \(\mathcal P_f\) denotes **finite** subsets. The notation in the scan is \(h:X\to P([0,1])\); the finiteness assumption is made explicit here for its listed classroom examples. The object is

$$H=\{\langle x,h_H(x)\rangle:x\in X\}. $$

Each set \(h_H(x)\) collects plausible grades; it is **not a probability distribution**, and no frequency or probability mass is implied. Duplicated degrees in a mathematical set are removed.

## Page-1 example

Let \(X=\{x_1,x_2,x_3\}\) and consider the grades read from the handwritten example:

$$\begin{aligned}
h_H(x_1)&=\{0.2,0.4,0.5\},\\
h_H(x_2)&=\{0.3,0.4\},\\
h_H(x_3)&=\{0.2,0.3,0.5,0.6\}.
\end{aligned}$$

Thus \(H\) consists of three ordered **element–set pairs**. The grades for \(x_3\) are presented in ascending order here for readability, not as a meaningful ranking of observers.

## Important distinctions

- Crisp: each \(x\) has grade exactly \(0\) or \(1\).
- Ordinary fuzzy: each \(x\) receives **one** grade in \([0,1]\).
- Hesitant fuzzy: each \(x\) receives a **nonempty set** of admissible grades.

A finite HFS becomes an ordinary fuzzy set if every \(h_H(x)\) is a singleton. Choosing one value per element is a **selection**, which needs justification and does not preserve the full uncertainty.

The handwritten scan does not supply a probability model, weights for experts or an aggregation operator. None is assumed here.

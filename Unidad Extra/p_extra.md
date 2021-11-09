# 1. 

- C categoría. 
- Funtores
    - F : CxC -> C 
    - G, G' : C -> C 

Defino
- $H\langle G, G'\rangle (A) = F(G(A), G'(A))$
- $H\langle G, G'\rangle (f) = F(G(f), G'(f))$

## a) Probar que H es un funtor

**Id**:
Sea $X \in ob(C), id_X$ la identidad de $X$
- $H\langle G, G'\rangle (id_X)$ 
- = def H
- $F(G(id_X), G'(id_X))$
- = G funtor
- $F(id_{G(X)}, id_{G'(X)})$
- = identidad en (G(X), G'(X)) (por definición de categoría producto)
- $F(id_{(G(X), G'(X))})$
- = F funtor
- $id_{F(G(X), G'(X))}$
- = def H
- $id_{H \langle G,G'\rangle(X)}$

**Composición**:
Sea $f, g \in mor(C)$ tal que se pueden componer de la manera $f \circ g$:

- $H\langle  G, G'\rangle (f \circ g)$ 
- = def H
- $F(G(f \circ g), G'(f \circ g))$
- = G funtor
- $F(G(f) \circ G(g), G'(f) \circ G'(g))$
- = composición de flechas en CxC
- $F((G(f), G'(f)) \circ (G(g) \circ G'(g)))$
- = F funtor
- $F(G(f), G'(f)) \circ F(G(g) \circ G'(g))$
- = def H
- $H \langle  G, G' \rangle (f) \circ H\langle  G, G'\rangle (g)$

## b) En qué condiciones es confiable o completo?

Recordemos las definiciones:
- Functor completo: sobreyectiva para flechas
- Functor confiable: inyectiva para flechas

Para que sea completo se tiene que cumplir: 
- $\forall y \in morC, \exist x \in morC :  H\langle G, G'\rangle (x) = y$

Es decir

- $\forall y \in morC, \exist x \in morC :  F(G(x), G'(x)) = y$

Necesitamos :
- F completo
    - $\forall y \in morC, \exist (z, z') \in morC \times C :  F(z, z') = y$
- Y que
    - $\exists x \in morC: G(x) = z \land G'(x) = z'$

Y nos queda H completo

---

Para que sea confiable se tiene que cumplir: 
- $H\langle G, G'\rangle (f) = H\langle G, G'\rangle (g) \implies f = g$

Si 
- F es confiable en la imágen de G y G'
- alguna G es confiable

Entonces H es confiable:
- $H\langle G, G'\rangle (f) = H\langle G, G'\rangle (g)$
- $\iff$
- $ F(G(f), G'(f)) = F(G(g), G'(g))$
- $\iff$ F confiable
- $ (G(f), G'(f)) = (G(g), G'(g))$
- $\iff$
- $ G(f) = G(g)$ y $G'(f) = G'(g)$
- $\iff$ G o G' confiable
- $f = g$


# 2. En el diagrama los cuatro trapecios conmutan
En fotos
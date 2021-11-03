# 1. 

- C categoría. 
- Funtores
    - F : CxC -> C 
    - G, G' : C -> C 

Defino
- $H\langle G, G'\rangle (A) = F(G(A), G'(A))$
- $H\langle G, G'\rangle (f) = F(G(f), G'(f))$

## a) Probar que H es un funtor

Id
- $H\langle G, G'\rangle (id_C)$ 
- = def H
- $F(G(id_C), G'(id_C))$
- = G funtor
- $F(id_{G(C)}, id_{G'(C)})$
- = F funtor
- $id_{F(G(C), G'(C))}$
- = def H
- $id_{H\langle  G,G'\rangle(C)}$

Composición:
- $H\langle  G, G'\rangle (f \circ g)$ 
- = def H
- $F(G(f \circ g), G'(f \circ g))$
- = G funtor
- $F(G(f) \circ G(g), G'(f) \circ G'(g))$
- = composición en CxC
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
- $\forall y \in C, \exist x \in C :  H\langle G, G'\rangle (x) = y$

Es decir

- $\forall y \in morC, \exist x \in morC :  F(G(x), G'(x)) = y$

Veamos que si F, G y G' son funtores completos, entonces H es completo:

- Como F es completo
    - $\forall y \in morC, \exist (z, z') \in morC \times C :  F(z, z') = y$
- Como G (análogo G') es completo
    - $\forall z \in morC, \exist x \in morC :  G(x) = z$

Y por lo tanto H es completo

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


También funciona si la categoría C tiene una única flecha, pero no es tan interesante ni general 

# 2. En el diagrama los cuatro trapecios conmutan
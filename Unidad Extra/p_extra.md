# 1. 

- C categoría. 
- Funtores
    - F : CxC -\rangle C 
    - G, G' : C -\rangle C 

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
- = 
- $F(G(f \circ g), G'(f \circ g))$
- = G funtor
- $F(G(f) \circ G(g), G'(f) \circ G'(g))$
- = composición en CxC
- $F((G(f), G'(f)) \circ (G(g) \circ G'(g)))$
- = F funtor
- $F(G(f), G'(f)) \circ F(G(g) \circ G'(g))$
- = def H
- $H \langle  G, G' \rangle (f) \circ H\langle  G, G'\rangle (g)$
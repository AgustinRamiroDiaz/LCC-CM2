Práctica 2, no se hacen: 2 c) y d), 7, del 9 al 17

preordenados:
- reflexivas
- transitivas

~ :
- reflexivas
- transitivas
- simetricas

parcialmente ordenados (Partially Ordered SET, POSET):
- reflexivas
- transitivas
- antisimétricas

retículo/lattice:
- Poset (L, <=)
- $\forall x, y \in L, \exists \sup \{x, y\}, \inf\{x, y\}$

# 2. Mostrar que los siguientes posets son ret ́ıculos:

## a) $(P(X),\subseteq)$.

Sean x, y ∈ P(X). Tenemos que ver que ヨ sup e inf de {x, y}
Proponemos sup = U e inf = ∩
Por definición la unión es cota superior. x ⊆ xUy e y ⊆ yUx
Supongamos que existe un s tal que
    x ⊆ s ⊂ xUy
    y ⊆ s ⊂ xUy

Es decir que existe un z \in xUy, y que z no está en s. Si z \in xUy es porque z está en x o en y. Y como s contiene a x y a y, entonces z \in s

El infimo es anal ogo

b) (Dn,|), donde Dn = {x ∈ N: x | n}.
x | n ⇔ x mod n = 0

sup{x, y} = mcd(x, y) = min({d : x | d, y | d}) por definición
inf = mcm

## c) $(L, \subseteq)$, donde L es el conjunto de subespacios vectoriales de Rn.

Intentemos demostrar con la definición alternativa de retículos

Proponemos:
- $\lor = + $
- $\land = \cap $

Asociatividad ∀x , y , z ∈L,
{
x ∨(y ∨z ) = (x ∨y ) ∨z
x ∧(y ∧z ) = (x ∧y ) ∧z
Conmutatividad ∀x , y ∈L,
{
x ∨y = y ∨x
x ∧y = y ∧x
Idempotencia ∀x ∈L,
{
x ∨x = x
x ∧x = x
Absorci ́on ∀x , y ∈L,
{
x ∨(x ∧y ) = x
x ∧(x ∨y ) = x
}

la suma de espacios vectoriales es asociativa y conmutativa por AL

- Conmutatividad: 
$U+V = \{u+v: u \in U, v \in V\} = \{v+u: u \in U, v \in V\} = V+U$

- Asociatividad:
$(U+V)+W = \{uv+w: uv \in U+V, w \in W\} = \{(u+v)+w: u \in U, v \in V, w \in W\} = \{u+(v+w): u \in U, v \in V, w \in W\} = \{u+vw: u \in U, vw \in V+W\} = U+(V+W)$

Idempotencia:
    U+U = {u+u’: u \in U, u’ in U} 
= (Clausura de la suma)
 {u’’: u \in U} = U

Absorción:
    U + (U \intersection V) = U
    U + (U \intersection V) = {u+uv: u \in U, uv \in U, uv \in V}
= (Clausura de la suma)
 {u’’: u \in U} = U

    U \interseccion (U + V)

    Como U \subset U+V, U \interseccion U+V = U


d) ́Algebra de Lindenbaum-Tarski.

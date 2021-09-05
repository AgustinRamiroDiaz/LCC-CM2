Práctica 2, no se hacen: 2 c) y d), 7, del 9 al 17

preordenados:
- reflexivas
- transitivas

~ :
- reflexivas
- transitivas
- simetricas

Conjuntos parcialmente ordenados (Partially Ordered SET, POSET):
- reflexivas
- transitivas
- antisimétricas

retículo/lattice:
- Poset $(L, \leq)$
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

Debemos probar:
- Asociatividad ∀x , y , z ∈L,
{
x ∨(y ∨z ) = (x ∨y ) ∨z
x ∧(y ∧z ) = (x ∧y ) ∧z
- Conmutatividad ∀x , y ∈L,
{
x ∨y = y ∨x
x ∧y = y ∧x
- Idempotencia ∀x ∈L,
{
x ∨x = x
x ∧x = x
- Absorción∀x , y ∈L,
{
x ∨(x ∧y ) = x
x ∧(x ∨y ) = x
}

Recordemos que la suma de espacios vectoriales es asociativa y conmutativa por AL

- Conmutatividad:
    
    - $U+V = \{u+v: u \in U, v \in V\} = \{v+u: u \in U, v \in V\} = V+U$
    
    - $U \cap V = V \cap U$

- Asociatividad:
    
    - $(U+V)+W = \{uv+w: uv \in U+V, w \in W\} \\= \{(u+v)+w: u \in U, v \in V, w \in W\} \\= \{u+(v+w): u \in U, v \in V, w \in W\} \\= \{u+vw: u \in U, vw \in V+W\} \\= U+(V+W)$
    
    - $(U \cap V) \cap W = U \cap (V \cap W)$

- Idempotencia:
    
    - $U+U = \{u+u’: u \in U, u’ \in U\}$ \
    =(Clausura de la suma)\
    $\{u’’: u \in U\} = U$

    - $U \cap U = U$

- Absorción:
    - $U + (U \cap V) = U$:\
    $U + (U \cap V) = \{u+uv: u \in U, uv \in U, u \in V\}$ \
    = (Clausura de la suma) \
    $\{u’’: u \in U\} = U$

    - $U \cap (U + V)$:\
    Como $U \subset U+V \implies U \cap U+V = U$


d) Álgebra de Lindenbaum-Tarski.



# Sea (L,≤) un retículo. Se definen las operaciones:
- x ∨ y = sup{x,y}
- x ∧ y = inf{x,y}

Probar que para todo x,y,z,w ∈L, ∨ y ∧ verifican las siguientes propiedades:

## a) x ≤ x ∨ y.

$x \lor y = \sup \{x, y\} = \min \{c: x \leq c, y \leq c\}$

$\therefore x \leq x \lor y$

## b) x ∧y ≤x.

$x \land y = \inf \{x, y\} = \max \{c: c \leq x, c \leq y\}$

$\therefore x \land y \leq x$

## c) x ≤y ⇔x ∨y = y ⇔x ∧y = x.

=>)

$x \lor y = \sup \{x, y\} = \min \{c: x \leq c, y \leq c\} = y$

$\iff$ (y es cota superior de x)

$x \leq y$

$\iff$ (x es cota inferior de y)

$\inf \{x, y\} = \max \{c: c \leq x, c \leq y\} = x$

## d) Asociatividad:

(x ∨y) ∨z = x ∨(y ∨z).

$(x \lor y) \lor z = \sup \{\sup \{x, y\}, z\}$

$= \min \{ c: \sup \{x, y\} \leq c, z \leq c \}$

$= \min \{ c: (\min \{k: x \leq k, y \leq k\}) \leq c, z \leq c \}$

$\iff$ (min de min)

$= \min \{ c: x \leq c, y \leq c, z \leq c \}$

(x ∧y) ∧z = x ∧(y ∧z).
Análogo

## e) Conmutatividad:

$x \lor y = \sup \{x, y\} = \sup \{y, x\} = y \lor x$


x ∧y = y ∧x. Analogo

## f) Idempotencia:

x ∨x = x = x ∧x.

$x \lor x = \sup \{x, x\} = x$


## g) Absorción:

x ∨(x ∧y) = x = x ∧(x ∨y).

$x \land y \leq x \implies x \lor (x \land y) = x$

$x \leq x \lor y \implies x = x \land (x \lor y)$

h) Compatibilidad:

x ≤z, y ≤w ⇒ x ∨y ≤z ∨w, x ∧y ≤z ∧w

$x \leq z \leq z \lor w$

$y \leq w \leq z \lor w$

Por lo tanto $z \lor w$ es cota superior de {x, y} y por ende $x \lor y \leq z \lor w$

# 4)

## a) Si L= (L,≤) es un ret ́ıculo, entonces las operaciones

- x ∨y = sup{x,y}

- x ∧y = inf{x,y}

definen un ret ́ıculo Lalg = (L,∨,∧).

Demostración:
Como vimos en el apartado anterior, estas definiciones cumplen con las 4 propiedades de la definición de retículos algebráicos (Asociatividad, conmutatividad, Idempotencia y Absorción) por lo cual Lalg es un retículo

## b) Si L= (L,∨,∧) es un ret ́ıculo, entonces la relaci ́on

x ≤y ⇔x ∨y = y

define un ret ́ıculo Lord = (L,≤).

Demostración:

Veamos que es poset:
- Reflexividad: Por idempotencia y la definición de la relación <= sabemos que\
$x \lor x = x \iff x \leq x$

- Transitividad: Sean $a, b, c \in L : a\leq b \leq c$ veamos que $a \leq c$:
    - $a \leq b \iff a \lor b = b$
    - $b \leq c \iff b \lor c = c$
    - $c = b \lor c = (a \lor b) \lor c = a \lor (b \lor c) = a \lor c$ por asociatividad
    - $\therefore a \leq c$ por def

- Antisimetría: Sean $a, b \in L : a\leq b, b \leq a$ veamos que $a = b$:
    - $a \leq b \iff a \lor b = b$
    - $b \leq a \iff b \lor a = a$
    - $a \lor b = b \lor a$ por asociatividad
    - $\therefore a = b$

Además queremos ver que para todo a, b en L existan supremo e infimo.

Definamos supremo como $\lor$ e infimo como $\land$ y veamos que efectivamente cumplen

Veamos que cumple ser cota superior

$a \leq a \lor b \iff a \lor (a \lor b) = a \lor b \iff (a \lor a) \lor b = a \lor b \iff a \lor b = a \lor b$



# %%
from graph import *
from poset import *

# %%
g = DefaultGraph(set(range(5)), {(0, 1), (0, 2), (1, 3), (1, 4)})
p = Poset(g)

#%%
assert (p.maximal_elements() == {2, 3, 4})
# %%
assert((p.has_bottom(), p.has_top()) == (True, False))
# %%

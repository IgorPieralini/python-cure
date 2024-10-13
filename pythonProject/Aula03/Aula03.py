# === OPERADORES LÓGICOS ===

# F - FALSE. T - TRUE

# +++++++ NÃO +++++++
# A (F, V)
# NÃO A(V, F)

a = True

print(not a)

#  +++++++ E +++++++
# (F, V) (F)
# (V, F) (F)
# (F, F) (F)
# (V, V) (V)

print((2 < 5) & (15/3 == 5))

# +++++++ OU +++++++

# (F, V) (F)
# (V, F) (V)
# (F, F) (V)
# (V, V) (V)

print((2 > 5) | (15/3 < 5))
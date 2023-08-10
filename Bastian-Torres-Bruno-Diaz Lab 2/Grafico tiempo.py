import matplotlib.pyplot as plt

Codigos = ["Codigo pandas", "Codigo normal"]
Valores = [350, 730]

# Colores para las barras (negro y amarillo)
colores = ['black', 'yellow']

fig, ax = plt.subplots()
bars = ax.bar(Codigos, Valores, color=colores)

ax.set_title('Comparacion de tiempos', loc="center")
ax.set_xlabel("Codigos")
ax.set_ylabel("Tiempos")

# Agregar valores dentro de las barras usando bar_label
ax.bar_label(bars)

# Agregar leyenda
ax.legend(bars, Valores, title="Valores")

plt.show()
class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop()


def deshacer_ultimo_cambio(ticket):
    historial_pila = ticket["historial"]
    estado_anterior = historial_pila.pop()
    
    if estado_anterior is not None:
        ticket["estado"] = estado_anterior
    else:
        print("No hay cambios que deshacer")

mi_ticket = {
    "id": "TCK-101",
    "estado": "Abierto",
    "historial": Pila()
}
print("Estado inicial:", mi_ticket["estado"])

mi_ticket["historial"].push(mi_ticket["estado"])
mi_ticket["estado"] = "En progreso"
print("Estado modificado:", mi_ticket["estado"])

print("Presionando deshacer...")
deshacer_ultimo_cambio(mi_ticket)
print("Estado final:", mi_ticket["estado"])



import re

#linea = "Jan 31 22:58:55 ubuntu.local ticky: INFO Created ticket [#2461] (jackowens)"
linea = "Jan 31 21:29:24 ubuntu.local ticky: ERROR The ticket was modified while updating (blossom)"

match = r"ticky: ([\w]+) ([\w\s].*)(?: (\[\#\d+\]))? \((\w+)\)$"
result = re.search(match, linea)

if result:
    tipo = result.group(1)
    mensaje = result.group(2)
    ticket = result.group(3)
    usuario = result.group(4)

    if ticket is None:
        ticket = ""  # Trata el caso en que "[#12345]" está ausente en INFO

    print(f"Tipo: {tipo}, Mensaje: {mensaje}, Ticket: {ticket}, Usuario: {usuario}")
else:
    print("No se encontró ninguna coincidencia.")
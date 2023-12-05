
#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess
import os

src = "/home/student/data/prod/"
dirs = next(os.walk(src))[1]

def change(dir_name):
    # Construir las rutas completas de origen y destino para el subdirectorio
    src_dir = os.path.join(src, dir_name)
    dest_dir = os.path.join("/home/student/data/prod_backup/", dir_name)

    # Usar rsync para copiar el contenido del subdirectorio
    subprocess.call(["rsync", "-arq", src_dir, dest_dir])

    # Imprimir un mensaje para mostrar cuál subdirectorio se está manejando
    print(f"Handling {dir_name}")

if __name__ == "__main":
    p = Pool(len(dirs))
    # Iniciar cada tarea dentro del grupo de procesos
    p.map(change, dirs)

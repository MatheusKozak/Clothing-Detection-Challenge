import os
import subprocess
import time
import shutil

def commit(origem , destino):
    # Configurações
    lote = 500                 # número de imagens por commit
    pausa = 1                  # segundos entre commits

    # Cria pasta destino se não existir
    os.makedirs(destino, exist_ok=True)

    # Pega todos os arquivos da origem (exceto o script e a pasta images)
    todos = [f for f in os.listdir(origem)]
    todos = [f for f in todos if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"))]
    todos.sort()

    print(f"Encontradas {len(todos)} imagens para processar.\n")

    commit_id = 1

    for i in range(0, len(todos), lote):
        grupo = todos[i:i + lote]

        # Move imagens para a pasta destino
        for img in grupo:
            src = os.path.join(origem, img)
            dst = os.path.join(destino, img)
            shutil.move(src, dst)

        # Faz git add/commit/push
        subprocess.run(["git", "add", destino], check=True)
        subprocess.run(["git", "commit", "-m", f"Commit {commit_id}: {len(grupo)} imagens"], check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"✔ Commit {commit_id} enviado com {len(grupo)} imagens.")
        commit_id += 1
        time.sleep(pausa)

    print("\n✅ Upload concluído!")


origem = ["C:\\Users\\mathe\\Downloads\\PAR2025\\PAR2025\\training_set\\training_set" , "C:\\Users\\mathe\\Downloads\\PAR2025\\PAR2025\\validation_set"]
destino = ["training_set" , "validation_set"]

for i in range(len(origem)):
    commit(origem[i], destino[i])

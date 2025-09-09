import os
import subprocess
import time
import shutil

def upload_images(source_dir, destination_dir):
    # Configurações
    batch_size = 500           # number of images per commit
    pause = 1                  # seconds between commits

    # Cria pasta destino se não existir
    os.makedirs(destination_dir, exist_ok=True)

    # Pega todos os arquivos da origem (exceto o script e a pasta images)
    all_files = [f for f in os.listdir(source_dir)]
    all_files = [f for f in all_files if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"))]
    all_files.sort()

    print(f"Found {len(all_files)} images to process.\n")

    commit_id = 1

    for i in range(0, len(all_files), batch_size):
        group = all_files[i:i + batch_size]

        # Move imagens para a pasta destino
        for img in group:
            src = os.path.join(source_dir, img)
            dst = os.path.join(destination_dir, img)
            shutil.move(src, dst)

        # Faz git add/commit/push
        subprocess.run(["git", "add", destination_dir], check=True)
        subprocess.run(["git", "commit", "-m", f"Commit {commit_id}: {len(group)} images"], check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"✔ Commit {commit_id} sent with {len(group)} images.")
        commit_id += 1
        time.sleep(pause)

    print("\n✅ Upload completed!")


sources = ["C:\\Users\\mathe\\Downloads\\PAR2025\\PAR2025\\training_set\\training_set" , "C:\\Users\\mathe\\Downloads\\PAR2025\\PAR2025\\validation_set"]
destinations = ["training_set" , "validation_set"]

for i in range(len(sources)):
    upload_images(sources[i], destinations[i])

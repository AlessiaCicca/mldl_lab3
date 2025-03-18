import os
import urllib.request
import zipfile

# URL del dataset
dataset_url = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"

# Percorsi di destinazione
dataset_folder = "tiny-imagenet"
zip_path = "tiny-imagenet-200.zip"

# Scaricare il dataset
if not os.path.exists(dataset_folder):  
    print("Downloading dataset...")
    urllib.request.urlretrieve(dataset_url, zip_path)
    print("Download complete!")

    # Estrarre il file ZIP
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dataset_folder)
    
    # Rimuovere il file ZIP dopo l'estrazione
    os.remove(zip_path)
    print("Dataset ready in", dataset_folder)
else:
    print("Dataset already downloaded.")

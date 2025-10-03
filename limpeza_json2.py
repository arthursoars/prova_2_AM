#Funcao para passar os Json para um csv longo unico
import os
import json
import pandas as pd

# pasta onde estão os arquivos JSON
pasta = "Sinais"

linhas = []

# percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".json"):
        caminho_json = os.path.join(pasta, arquivo)
        with open(caminho_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            for frame in data["frames"]:
                frame_id = frame["frame"]
                for kp in frame["keypoints"]:
                    linhas.append({
                        "file_name": arquivo,   # mantém o nome do arquivo json
                        "frame": frame_id,
                        "id": kp["id"],
                        "x": kp["x"],
                        "y": kp["y"],
                        "z": kp["z"],
                        "visibility": kp["visibility"]
                    })

# transforma tudo em um dataframe único
df_final = pd.DataFrame(linhas)

# salva em um único CSV
df_final.to_csv("sinais_long.csv", index=False)

print(f"CSV único criado com {len(df_final)} linhas.")

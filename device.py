import gdown
import json
import os
import torch


def download_models(models, models_path):
    current_path = os.getcwd()
    os.chdir(models_path)

    try:
        for model in models:
            filename, url = model
            file_path = os.path.join(models_path, filename)

            if not os.path.exists(file_path):
                print(f'Descargando {filename}...')
                gdown.download(url, file_path, quiet=False)
            else:
                print(f'{filename} ya existe.')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')

    os.chdir(current_path)


def get_device():
    device_name = torch.device('cpu')
    torch_dtype = torch.float32

    if torch.cuda.is_available():
        device_name = torch.device('cuda')
        torch_dtype = torch.float16

    return device_name, torch_dtype


def save_frame_info(json_obj, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=4)

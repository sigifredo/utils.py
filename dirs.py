import os


def delete_files_in_folder(folder_path):
    files_deleted = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                files_deleted += 1
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    print(f'✅ {files_deleted} archivos eliminados en "{folder_path}"')

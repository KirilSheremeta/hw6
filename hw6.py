import sys
from pathlib import Path
import os
import re
import shutil
import translate

path = r"C:\Users\migod\OneDrive\Робочий стіл\trash"


def create_directions(path):
    
    """
    This function creates directions
    """

    images_dir = os.path.join(path, "images")
    music_dir = os.path.join(path, "music")
    videos_dir = os.path.join(path, "videos")
    archives_dir = os.path.join(path, "archives")
    documents_dir = os.path.join(path, "documents")
    others_dir = os.path.join(path, "others")

    list_of_dirs = [images_dir, music_dir, videos_dir,
                    archives_dir, documents_dir, others_dir]
    names_of_dirs = ["images", "music", "videos",
                     "archives", "documents", "others"]
    for direction in list_of_dirs:
        try:
            os.mkdir(direction)
        except FileExistsError:
            print("File Exists Error!")
            pass


def remove_and_rename():
    
    """
    This function removes and renames files
    """

    images_list = ('JPEG', 'PNG', 'JPG', 'SVG', 'BMP')
    videos_list = ('AVI', 'MP4', 'MOV', 'MKV')
    documents_list = ('DOC', 'DOCX', 'TXT', 'PDF',
                      'XLSX', 'PPTX', 'RTF', 'XLS')
    music_list = ('MP3', 'OGG', 'WAV', 'AMR')
    archives_list = ('ZIP', 'GZ', 'TAR', 'RAR', '7Z')

    known_extensions = []
    unknown_extensions = []

    for roots, subFolders, files in os.walk(path):
        for file in files:
            try:
                txt_path = os.path.join(roots, file)
                files_list = file.rsplit(".")
                
                if files_list[-1].upper() in images_list:
                    new_name = os.path.join(
                        roots, translate.normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, create_directions.images_dir(path))
                    known_extensions.append(files_list[-1])
                    
                elif files_list[-1].upper() in videos_list:
                    new_name = os.path.join(
                        roots, translate.normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, create_directions.videos_dir(path))
                    known_extensions.append(files_list[-1])
                    
                elif files_list[-1].upper() in music_list:
                    new_name = os.path.join(
                        roots, translate.normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, create_directions.music_dir(path))
                    known_extensions.append(files_list[-1])
                    
                elif files_list[-1].upper() in documents_list:
                    new_name = os.path.join(
                        roots, translate.normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(
                        txt_path, create_directions.documents_dir(path))
                    known_extensions.append(files_list[-1])
                    
                elif files_list[-1].upper() in archives_list:
                    files_name = translate.normalize_names(file)
                    new_name = os.path.join(roots, files_name)
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    os.mkdir(os.path.join(create_directions.archives_dir(
                        path)), os.path.splitext(files_name[0]))
                    shutil.move(txt_path, os.path.join(create_directions.archives_dir(
                        path)), os.path.splitext(files_name[0]))
                    txt_path = os.path.join(
                        create_directions.archives_dir(path), os.path.splitext(files_name)[0], files_name)
                    try:
                        shutil.unpack_archive(txt_path, os.path.join(
                            create_directions.archives_dir(path), os.path.splitext(files_name)[0]))
                    except (ValueError, shutil.ReadError):
                        pass
                    known_extensions.append(files_list[-1])
                    
                else:
                    os.path.join(create_directions.others_dir(path), file)
                    new_name = os.path.join(
                        roots, translate.normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, create_directions.others_dir(path))
                    unknown_extensions.append(files_list[-1])
            finally:
                continue
    print("Known_extensions - ", known_extensions)
    print("Unknown_extensions - ", unknown_extensions)


def delete_dirs(path):
    """
    This function deletes folders after removing
    """

    for direct in Path(path).glob("*"):
        if direct.is_dir() and direct.name not in create_directions.names_of_dirs():
            try:
                shutil.rmtree(direct, ignore_errors=True)
            except PermissionError:
                print("Permission error for delete", direct)

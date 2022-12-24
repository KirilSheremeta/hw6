import sys
from pathlib import Path
import os
import re
import shutil
from translate import normalize_names

CATEGORIES = {
    "images": (".JPEG", ".PNG", ".JPG", ".SVG", ".BMP"),
    "music": (".MP3", ".OGG", ".WAV", ".AMR"),
    "videos": (".AVI", ".MP4", ".MOV", ".MKV"),
    "archives": (".ZIP", ".GZ", ".TAR", ".RAR", ".7Z"),
    "documents": (".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX", ".RTF", ".XLS"),
    "others": None,
}


def create_directions(path: Path):
    """
    This function creates directions
    """
    for direction in CATEGORIES:
        try:
            Path.mkdir(path.joinpath(direction))
        except FileExistsError:
            print("File Exists Error!")
            pass


def remove_and_rename(path: Path):
    """
    This function removes and renames files
    """
    known_extensions = []
    unknown_extensions = []

    for item in path.glob("**/*.*"):

        for cat, ext in CATEGORIES.items():

            if not ext:
                item.replace(
                    path.joinpath(
                        cat, f"{normalize_names(item.stem)}{item.suffix}")
                )
                unknown_extensions.append(item.suffix)
                break

            if item.suffix.upper() in ext:
                item.replace(
                    path.joinpath(
                        cat, f"{normalize_names(item.stem)}{item.suffix}")
                )
                known_extensions.append(item.suffix)
                break

    print("Known_extensions - ", known_extensions)
    print("Unknown_extensions - ", unknown_extensions)


def delete_dirs(path):
    """
    This function deletes folders after removing
    """

    for direct in Path(path).glob("*"):
        if direct.is_dir() and direct.name not in CATEGORIES:
            try:
                shutil.rmtree(direct, ignore_errors=True)
            except PermissionError:
                print("Permission error for delete", direct)


def unpack_archives(path: Path):
    arc: Path
    for arc in path.joinpath("archives").iterdir():
        shutil.unpack_archive(arc, path.joinpath("archives", arc.stem))


def get_path():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("Sorry, take the path to folder")
        return None
    if not path.exists():
        print("Sorry, the path not exist. Try another.")
        return None

    return path


if __name__ == "__main__":
    path = get_path()

    if path:
        create_directions(path)
        remove_and_rename(path)
        delete_dirs(path)
        unpack_archives(path)

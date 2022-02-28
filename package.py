from cyrtranslit import to_latin
import os
from pathlib import Path
import shutil
from util import get_loc_dir_path



VERSION = '2.3.0'
CYRILLIC_CODE = 'srp'
LATIN_CODE = 'srb'



def main():
    working_path = Path(__file__).resolve().parent

    localization_path = Path(get_loc_dir_path())
    cyrillic_path = localization_path / CYRILLIC_CODE
    latin_path = localization_path / LATIN_CODE

    shutil.rmtree(latin_path, ignore_errors=True)
    os.makedirs(latin_path)

    _, _, files = next(os.walk(cyrillic_path))
    for file in files:
        with open(cyrillic_path / file, 'r', encoding='utf-8') as cyrillic, open(latin_path / file, 'w', encoding='utf-8') as latin:
            text = cyrillic.read()
            latin.write(to_latin(text))

    cyrillic_zip_path = working_path / f'{CYRILLIC_CODE}-{VERSION}'
    os.chdir(cyrillic_path)
    shutil.make_archive(cyrillic_zip_path, 'zip', cyrillic_path)

    cyrillic_zip_path = working_path / f'{LATIN_CODE}-{VERSION}'
    os.chdir(latin_path)
    shutil.make_archive(cyrillic_zip_path, 'zip', latin_path)


if __name__ == '__main__':
    main()

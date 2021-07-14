# -*- coding: utf-8 -*-
import sys
import os
import shutil

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('[Error] usage: python *.py <file path>')
    else:
        filepath_list = map(str, sys.argv[1:])
        for filepath in filepath_list:
            # dir_path, filenameに分離
            dirpath = os.path.dirname(filepath)
            filename = os.path.basename(filepath)
            # oldディレクトリを作成し移動
            old_dirpath = os.path.join(dirpath, 'old')
            os.makedirs(old_dirpath, exist_ok=True)
            shutil.move(filepath, os.path.join(old_dirpath, filename))
            
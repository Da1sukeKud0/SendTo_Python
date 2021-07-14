# -*- coding: utf-8 -*-
import sys
import os
import pyperclip as pc

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('[Error] usage: python *.py <file path>')
    else:
        full_path = str(sys.argv[1])
        filename_list = []

        for p, ds, fs in os.walk(full_path):
            for f in fs:
                filename_list.append(f)

        # ファイル名毎に改行して取得
        pc.copy('\r\n'.join(filename_list))
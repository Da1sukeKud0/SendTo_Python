# -*- coding: utf-8 -*-
import sys
import os
import pyperclip as pc
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Error.')
    else:
        full_path = str(sys.argv[1])

        # dir_path, filenameに分離
        dir_path = os.path.dirname(full_path)
        filename = os.path.basename(full_path)

        # RocketChatでリンクを張るために``で囲う
        pc.copy('`' + dir_path + '`' + '\r\n' + filename)

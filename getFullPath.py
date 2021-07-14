# -*- coding: utf-8 -*-
import sys
import os
import pyperclip as pc
import json
import subprocess

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('[Error] usage: python *.py <file path>')
    else:
        full_path = str(sys.argv[1])

        # dir_path, filenameに分離
        dir_path = os.path.dirname(full_path)
        filename = os.path.basename(full_path)

        # configを読み込み、ディレクトリ部分を囲む文字を指定する
        codeblock_delimiter_start = '`'
        codeblock_delimiter_end = '`'
        appdata_path = subprocess.run("echo %APPDATA%", shell=True, encoding='utf-8', stdout=subprocess.PIPE).stdout.splitlines()[0]
        sendto_path = os.path.join(appdata_path + r'\Microsoft\Windows\SendTo')
        config_path = os.path.join(sendto_path, r"conf\config.json")
        if os.path.exists(config_path):
            config = json.load(open(config_path, encoding='utf-8'))
            if 'codeblock_delimiter_start' in config:
                codeblock_delimiter_start = config['codeblock_delimiter_start']
            if 'codeblock_delimiter_end' in config:
                codeblock_delimiter_end = config['codeblock_delimiter_end']
        
        # リンクをコピーし、ディレクトリ部分を指定された文字で囲う
        pc.copy(codeblock_delimiter_start + dir_path + codeblock_delimiter_end + '\r\n' + filename)

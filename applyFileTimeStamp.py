# -*- coding: utf-8 -*-
import sys
import os
import pyperclip as pc
import shutil
import datetime
import re

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('[Error] usage: python *.py <file path>')
    else:
        full_path = str(sys.argv[1])

        # dir_path, filenameに分離
        dir_path = os.path.dirname(full_path)
        filename = os.path.basename(full_path)

        # filenameから版部分(<DateFormat>-<Edition>)を抽出
        print(filename)
        pattern = r'_[0-9]{8}-[0-9]{1,}' #<DateFormat>-<Edition>:  yyyymmdd-e
        matchOB = re.search(pattern , filename)
        if not matchOB:
            pattern = r'_[0-9]{6}-[0-9]{1,}' #<DateFormat>-<Edition>:  yymmdd-e
            matchOB = re.search(pattern , filename)
        
        if matchOB:
            matchStr = matchOB.group() # マッチした文字列を返す

            # 版更新処理
            date, edition = matchStr.replace('_','').split('-')
            # patternを確認しdatetime形式にパース
            if len(date) == 8:
                update_date = datetime.datetime.strptime(date, '%Y%m%d') #<DateFormat>: yyyymmdd-e
            else:
                update_date = datetime.datetime.strptime(date, '%y%m%d') #<DateFormat>: yymmdd-e

            #更新日時/アクセス日時変更
            #hourは10で固定
            mtime = datetime.datetime(update_date.year, update_date.month, update_date.day, 10).timestamp()
            atime = datetime.datetime(update_date.year, update_date.month, update_date.day, 10).timestamp()
            os.utime(full_path, (atime, mtime))

            # RocketChatでリンクを張るために``で囲う
            # pc.copy('`' + dir_path + '`' + '\r\n' + update_filename)

            print('Done.')
        else:
            print('[Error] undefined pattern')
            print('defined pattern: *<yyyymmdd-e>*, *<yymmdd-e>*')
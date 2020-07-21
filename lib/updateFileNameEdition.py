# -*- coding: utf-8 -*-
import sys
import os
import pyperclip as pc
import shutil
import datetime
import re
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Error.')
    else:
        full_path = str(sys.argv[1])

        # dir_path, filenameに分離
        dir_path = os.path.dirname(full_path)
        filename = os.path.basename(full_path)

        # filenameから版部分(<DateFormat>-<Edition>)を抽出
        print(filename)
        #pattern = r'_[0-9]{8}-[0-9]{1,}' #<DateFormat>-<Edition>:  yyyymmdd-e
        pattern = r'_[0-9]{6}-[0-9]{1,}' #<DateFormat>-<Edition>:  yymmdd-e
        matchOB = re.search(pattern , filename)
        if matchOB:
            matchStr = matchOB.group() # マッチした文字列を返す

            # 版更新処理
            date, edition = matchStr.replace('_','').split('-')
            #update_date = datetime.date.today().strftime('%Y%m%d') #<DateFormat>: yyyymmdd-e
            update_date = datetime.date.today().strftime('%Y%m%d')[2:] #<DateFormat>: yymmdd-e
            # 日付が同じ場合は版+1、異なる場合は0
            if date == update_date:
                update_edition = str(int(edition) + 1)
            else:
                update_edition = '0'

            # 更新後のファイル名決定
            update_filename = filename.replace(matchStr, '_' + update_date + '-' + update_edition)
            print(update_filename)

            # 版更新してファイルコピー
            update_full_path = os.path.join(dir_path, update_filename)
            shutil.copy2(full_path, update_full_path)

            # RocketChatでリンクを張るために``で囲う。
            pc.copy('`' + dir_path + '`' + '\r\n' + update_filename)

            print('Done.')
        else:
            print('Error.')
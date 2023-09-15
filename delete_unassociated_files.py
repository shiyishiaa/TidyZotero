from __future__ import print_function

import datetime
import os
import re
import shutil
import sqlite3
import tkinter as tk
from os import walk

import pandas as pd

import util

root = tk.Tk()
root.withdraw()

# 选择PDF备份的目录
back_dir = "./Backups/" + str(datetime.datetime.now()).replace(":", "-")

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


def run():
    # 得到zotero数据目录和文件目录
    data_dir = util.get_zotero_data_dirs()
    dest_dir = util.get_zotfile_dest_dir()

    list_of_files = []  # 文件包含目录
    files = []  # 仅文件名
    for (dir_path, dir_names, filenames) in walk(dest_dir):
        for file in filenames:
            if file.endswith('.pdf'):
                list_of_files.append(os.path.join(dir_path, file))
                files.append(file)

    # 连接数据库
    zot_sqlite = os.path.join(data_dir, 'zotero.sqlite')
    with sqlite3.connect(zot_sqlite) as con:
        item_att = pd.read_sql_query("SELECT * FROM itemAttachments", con=con)
        item_path = item_att['path']

    # 生成备份文件目录
    # 当文件不存在时，才创建该文件夹。
    if not os.path.exists(back_dir):
        os.mkdir(back_dir)

    for i in range(len(files)):
        # 如zotero.sqlite的path中不包括文件
        if not (item_path.str.contains(re.escape(files[i])).any()):
            # os.remove(list_of_files[i]) #也可以删除文件
            shutil.move(list_of_files[i], os.path.join(back_dir, files[i]))  # 移动文件到备份目录
            print('已备份', files[i], '到', back_dir)


if __name__ == '__main__':
    run()

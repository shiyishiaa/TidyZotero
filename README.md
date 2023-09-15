# 来源声明

源代码参考自[[zotero/python]库中参考文献条目删除后，清除残留PDF的脚本](https://zhuanlan.zhihu.com/p/121770068)
和[为 Zotero 删除 storage 中的“空”文件夹](https://zhuanlan.zhihu.com/p/41168160)两篇文章，自己做了些微调和优化，感谢大佬们的贡献！

# 免责声明

使用前请确认自己是否了解本项目作用。

# 使用方法

- 删除残留的PDF文件

```bash
python delete_unassociated_files.py
```

被移除的文件将会备份在`Backups\{datetime}`文件夹下。

- 删除Zotero文件仓库下空文件夹

```bash
python delete_empty_folders_in_zotero_storage_dir
```

<b>被删除的文件夹无法恢复！</b>

- 删除ZotFile指定目录下空文件夹

```bash
python delete_empty_folders_in_zotfile_dest_dir
```

<b>被删除的文件夹无法恢复！</b>

- 一键清理

```bash
python all_in_one.py
```
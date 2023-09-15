from __future__ import print_function

import shutil

import click

import util

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


def get_empty_folders(storage_dir):
    """
    Get a list of empty dir in string type.
    """
    return [
        p.as_posix() for p in storage_dir.iterdir()
        if (not p.is_file()) and (not len([f for f in list(p.iterdir()) if f.name[0] != '.']))
    ]


def run():
    zotero_storage_dir = util.get_zotero_storage_dir()
    dirs_to_remove = get_empty_folders(zotero_storage_dir)

    print('The following folders contain no attachments:')
    print('\n  '.join([''] + dirs_to_remove))
    if click.confirm('Do you want remove them?', default=True):
        [shutil.rmtree(p, ignore_errors=True) for p in dirs_to_remove]


if __name__ == '__main__':
    run()

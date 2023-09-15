from __future__ import print_function

import configparser
import re
import sys
from pathlib import Path


def get_zotero_data_dirs():
    """
    Get the Zotero data dir and the Zotfile destination dir in PosixPath type
    """
    configs = get_zotero_configs()

    zotero_data_pat = re.compile(r'user_pref\("extensions.zotero.dataDir", "(?P<zotero_data>.+)"\);')
    zotero_data_dir = Path(zotero_data_pat.search(configs).group('zotero_data'))

    return zotero_data_dir


def get_zotero_storage_dir():
    """
    Get the Zotero storage dir and in PosixPath type
    """
    return get_zotero_data_dirs() / 'storage'


def get_zotfile_dest_dir():
    """
    Get the Zotfile destination dir in PosixPath type
    """
    configs = get_zotero_configs()

    zotfile_dest_pat = re.compile(r'user_pref\("extensions.zotfile.dest_dir", "(?P<zotfile_dest>.+)"\);')
    zotfile_dest_dir = Path(zotfile_dest_pat.search(configs).group('zotfile_dest'))

    return zotfile_dest_dir


def get_zotero_configs():
    profile_dirs = {
        'darwin': Path.home() / 'Library/Application Support/Zotero',
        'linux': Path.home() / '.zotero/zotero',
        'linux2': Path.home() / '.zotero/zotero',
        'win32': Path.home() / 'AppData/Roaming/Zotero/Zotero'
    }
    profile_dir = profile_dirs[sys.platform]
    config = configparser.ConfigParser()
    config.read('{}'.format(profile_dir / 'profiles.ini'))
    configs_loc = profile_dir / config['Profile0']['Path'] / 'prefs.js'
    configs = configs_loc.read_text()
    return configs

import delete_empty_folders_in_zotero_storage_dir
import delete_empty_folders_in_zotfile_dest_dir
import delete_unassociated_files

if __name__ == '__main__':
    delete_unassociated_files.run()
    delete_empty_folders_in_zotfile_dest_dir.run()
    delete_empty_folders_in_zotero_storage_dir.run()

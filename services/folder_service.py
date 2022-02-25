from utilities.folder_utility import FolderUtility
from services.file_service import FileService
from utilities.logger_utility import LogUtility


class FolderService:
    @staticmethod
    def get_file_names_and_its_word_counts_of_folder(folder_path):
        try:
            folder_content_lst = FolderUtility.get_folder_content_list(folder_path)
            dict = {}
            for file in folder_content_lst:
                dict[file] = FileService.count_each_word(file)
            return dict
        except Exception as ex:
            LogUtility.write_error('folder-service.log',
                                   "Folder '{}' processing for getting word count. (->on FolderService=>get_file_names_and_its_word_counts_of_folder()<-) : {}".format(
                                       folder_path, str(ex)))
            raise Exception('could not able to get folder contents with count')

    @staticmethod
    def get_file_names_and_its_word_first_alpahbate_count_of_folder(folder_path):
        try:
            folder_content_lst = FolderUtility.get_folder_content_list(folder_path)
            dict = {}
            for file in folder_content_lst:
                dict[file] = FileService.count_each_first_alphabet(file)
            return dict
        except Exception as ex:
            LogUtility.write_error('folder-service.log',
                                   "Folder '{}' processing for getting first alphabete  count. (->on FolderService=>get_file_names_and_its_word_first_alpahbate_count_of_folder()<-) : {}".format(
                                       folder_path, str(ex)))
            raise Exception('could not able to get folder contents with alphabet count')

    @staticmethod
    def get_file_names_and_its_pure_words(folder_path):
        try:
            folder_content_lst = FolderUtility.get_folder_content_list(folder_path)
            dict = {}
            for file in folder_content_lst:
                dict[file] = FileService.get_cleared_up_alphabet(file)
            return dict
        except Exception as ex:
            LogUtility.write_error('folder-service.log',
                                   "Folder '{}' processing for getting pure words. (->on FolderService=>get_file_names_and_its_pure_words()<-) : {}".format(
                                       folder_path, str(ex)))
            raise Exception('could not able to get folder contents with pure alphabet')

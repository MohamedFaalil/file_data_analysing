from utilities.file_utility import FileUtility
from utilities.logger_utility import LogUtility
import re


class FileService:
    __file_directory = "./storage/data_sets"

    @classmethod
    def get_cleared_up_alphabet(cls, file_name):
        try:
            file_path = "{file_dir}/{file_name}".format(file_dir=cls.__file_directory, file_name=file_name)
            file_content_list = FileUtility.get_file_content_as_list(file_path)
            deletable_indices = []
            for index in range(len(file_content_list)):
                word = file_content_list[index]
                purified_word = FileService.__remove_non_alpahbates_of_the_word(word)
                if len(purified_word) < 1:
                    deletable_indices.append(index)
                    continue
                file_content_list[index] = FileService.__remove_non_alpahbates_of_the_word(word)
            return FileService.__delete_contents_of_list_by_index(file_content_list, deletable_indices)
        except Exception as ex:
            LogUtility.write_error('file-service.log',
                                   "Exception occurred, while getting cleared up  file `{}` (->on FileService=>get_cleared_up_alphabet()<-) : {}".format(
                                       file_name, str(ex)))
            raise Exception("could not able to cleared up the  file `{}`".format(file_name))

    @classmethod
    def count_each_first_alphabet(cls, file_name):
        try:
            file_path = "{file_dir}/{file_name}".format(file_dir=cls.__file_directory, file_name=file_name)
            file_content_list = FileUtility.get_file_content_as_list(file_path)
            counted_words_dict = FileService.__count_words_first_alphabates(file_content_list)
            return FileService.__convert_dict_key_value_into_tuple_list(counted_words_dict)
        except Exception as ex:
            LogUtility.write_error('file-service.log',
                                   "Exception occurred, while counting first alphabete on the file `{}` (->on FileService=>get_cleared_up_alphabet()<-) : {}".format(
                                       file_name, str(ex)))
            raise Exception("could not able to count alphabets on the  file `{}`".format(file_name))

    @classmethod
    def count_each_word(cls, file_name):
        try:
            file_path = "{file_dir}/{file_name}".format(file_dir=cls.__file_directory, file_name=file_name)
            file_content_list = FileUtility.get_file_content_as_list(file_path)
            counted_words_dict = FileService.__count_words(file_content_list)
            return FileService.__convert_dict_key_value_into_tuple_list(counted_words_dict)
        except Exception as ex:
            LogUtility.write_error('file-service.log',
                                   "Exception occurred, while counting words on  file `{}` (->on FileService=>get_cleared_up_alphabet()<-) : {}".format(
                                       file_name, str(ex)))
            raise Exception("could not able to counting words on the  file `{}`".format(file_name))

    @staticmethod
    def __delete_contents_of_list_by_index(lst, del_indices):
        result = []
        for lst_index in range(len(lst)):
            if lst_index not in del_indices:
                result.append(lst[lst_index])
        return result

    @staticmethod
    def __convert_dict_key_value_into_tuple_list(counted_words_dict):
        lst = []
        for key in counted_words_dict:
            lst.append((key, counted_words_dict[key]))
        return lst

    @staticmethod
    def __count_words(file_content_list):
        dict = {}
        for word in file_content_list:
            keys = dict.keys()
            if word in keys:
                dict[word] += 1
            else:
                dict[word] = 1
        return dict

    @staticmethod
    def __count_words_first_alphabates(file_content_list):
        dict = {}
        for word in file_content_list:
            pure_alpahbate_word = FileService.__remove_non_alpahbates_of_the_word(word)
            if len(pure_alpahbate_word) < 1:
                continue

            first_char = pure_alpahbate_word[0]
            keys = dict.keys()
            if first_char in keys:
                dict[first_char] += 1
            else:
                dict[first_char] = 1
        return dict

    @staticmethod
    def __remove_non_alpahbates_of_the_word(word):
        regex = r"[a-zA-Z]*"
        matches = re.finditer(regex, word, re.MULTILINE)
        str = ''
        for matchNum, match in enumerate(matches, start=1):
            # getting long pure alphabet
            if len(match.group()) > len(str):
                str = match.group()
        return str

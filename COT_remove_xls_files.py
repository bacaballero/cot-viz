import os


def remove_xls_files():
    dir_name = os.path.dirname(__file__)
    folder_name = os.path.join(dir_name, 'COT Reports')
    file_list = os.listdir(folder_name)

    for item in file_list:
        if item.endswith(".xls"):
            print(f"removing {item}")
            os.remove(os.path.join(folder_name, item))


remove_xls_files()

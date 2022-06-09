import os
import shutil
import re
import zipfile

if __name__ == '__main__':
    os.getcwd()
    path = 'C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\extracted_content.zip'
    path1 = 'C:\\Users\\jbwow\\PycharmProjects\\pythonProject'
    unzipped_file = zipfile.ZipFile(path, 'r')
    unzipped_file.extractall(path1)
    walk_flag = True
    for files in os.walk('C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Five'):
        #   list of strings of the name of each text file at files[2]
        if walk_flag == True:
            for text in files[2]:
                #   now open up the text files
                final_path = f'C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Five\\{text}'
                f = open(final_path, 'r')
                phone = re.search('\d\d\d-\d\d\d-\d\d\d\d', f.read())
                if phone != None:
                    print(phone.group())
                    walk_flag = False
                    break
                #   print(f'{f.read()} \n')
                #   sets the pointer to the beginning after reading a file
                f.seek(0)
    for files in os.walk('C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Four'):
        #   list of strings of the name of each text file at files[2]
        if walk_flag == True:
            for text in files[2]:
                #   now open up the text files
                final_path = f'C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Four\\{text}'
                f = open(final_path, 'r')
                phone = re.search('\d\d\d-\d\d\d-\d\d\d\d', f.read())
                if phone != None:
                    print(phone.group())
                    walk_flag = False
                    break
                #   sets the pointer to the beginning after reading a file
                f.seek(0)
    for files in os.walk('C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Three'):
        #   list of strings of the name of each text file at files[2]
        if walk_flag == True:
            for text in files[2]:
                #   now open up the text files
                final_path = f'C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Three\\{text}'
                f = open(final_path, 'r')
                phone = re.search('\d\d\d-\d\d\d-\d\d\d\d', f.read())
                if phone != None:
                    print(phone.group())
                    walk_flag = False
                    break
                #   sets the pointer to the beginning after reading a file
                f.seek(0)
    for files in os.walk('C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Two'):
        #   list of strings of the name of each text file at files[2]
        if walk_flag == True:
            for text in files[2]:
                #   now open up the text files
                final_path = f'C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\Two\\{text}'
                f = open(final_path, 'r')
                phone = re.search('\d\d\d-\d\d\d-\d\d\d\d', f.read())
                if phone != None:
                    print(phone.group())
                    walk_flag = False
                    break
                #   sets the pointer to the beginning after reading a file
                f.seek(0)
    for files in os.walk('C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\One'):
        #   list of strings of the name of each text file at files[2]
        if walk_flag == True:
            for text in files[2]:
                #   now open up the text files
                final_path = f'C:\\Users\\jbwow\\PycharmProjects\\pythonProject\\One\\{text}'
                f = open(final_path, 'r')
                phone = re.search('\d\d\d-\d\d\d-\d\d\d\d', f.read())
                if phone != None:
                    print(phone.group())
                    walk_flag = False
                    break
                #   sets the pointer to the beginning after reading a file
                f.seek(0)

import csv
import os

dirname='C:/Users/HKH/Downloads/chrome download/crawlmaster/driver/txtfile'
filenames = os.listdir(dirname)
txt_file = 'title_list.txt'
for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    with open(txt_file, "a+", encoding='UTF8') as my_output_file:
        my_output_file.write(filename[:-4])
        my_output_file.write('\n')
my_output_file.close()

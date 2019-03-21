import csv
import os

dirname='C:/Users/HKH/Downloads/chrome download/crawlmaster/driver/txtfile'
filenames = os.listdir(dirname)
for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    with open('one_text.txt', "a+", encoding='UTF8') as my_output_file:
        with open(full_filename, "r", encoding='UTF8') as my_input_file:
            atext = my_input_file.read().replace('\n', ' ')
            my_output_file.write(atext)
            my_output_file.write('\n')
            my_output_file.write('\n')
            my_output_file.write('BREAKS HERE')
            my_output_file.write('\n')
            my_output_file.write('\n')
my_output_file.close()
my_input_file.close()
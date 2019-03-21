import glob
import os
save_path = 'C:/Users/HKH/Documents/카카오톡 받은 파일/cine21최종 (2)'
os.chdir('C:/Users/HKH/Downloads/chrome download/crawlmaster/driver/daum_review/edit') #txt 있는 경로
for file in glob.glob("*.txt"): #'*'은 모든 값을 의미
    name_of_file = file
    completeName = os.path.join(save_path, name_of_file)
    file1 = open(completeName, 'a+', encoding="utf8")
    f = open(file, 'r', encoding="utf8")
    lines = f.readlines()
    for line in lines:
        file1.write(line)
    file1.close()
    f.close()

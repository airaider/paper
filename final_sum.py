import glob
import os
save_path = 'C:/Users/HKH/Downloads/chrome download/crawlmaster/driver/review'
os.chdir('C:/Users/HKH/Downloads/chrome download/crawlmaster/driver/daum_review/edit') #txt 있는 경로
for file in glob.glob("*.txt"): #'*'은 모든 값을 의미
    os.chdir('C:/Users/HKH/Documents/카카오톡 받은 파일/cine21최종 (2)')
    for files in glob.glob('*.txt'):
        if file.split('(')[0].replace(" ", '') == files.split('(')[0].replace(" ", ''):
            completeName = os.path.join(save_path, files)
            file1 = open(completeName, 'w', encoding="utf8")
            os.chdir('C:/Users/HKH/Downloads/chrome download/crawlmaster/driver/daum_review/edit')
            f = open(file, 'r', encoding="utf8")
            lines = f.readlines()
            os.chdir('C:/Users/HKH/Documents/카카오톡 받은 파일/cine21최종 (2)')
            f2 = open(files, 'r', encoding="utf8")
            lines2 = f2.readlines()
            for line in lines:
                file1.write(line)
            for line in lines2:
                file1.write(line)



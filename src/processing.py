file=open('C:\\Users\\ATIF ADIB\\Desktop\\reviews.txt','r')
file1=open('C:\\Users\\ATIF ADIB\\Desktop\\reviews_processed_electronics.txt','a')
s=file.readline()
while(s!=''):
    file1.write(s+',')
    s=file.readline()
file.close()
file1.close()
    
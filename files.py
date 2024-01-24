# opens file if it exits in the directory
alexia=open('spiral_line.py','r')
# alexia.write(alexia)
# it  will generate an error if the file does not exit.
sales_file=open('sales.txt','w')
sales_file.write('hello ,im alex practising to \n write in new file')
sales_file.write('\n i am getting use to it ')
sales_file.close()

# the above creates a file in the same directory as the project
# when giving a different path  ,prefix the string with 'r'
# example
fille=open(r'C:\Users\njugu\OneDrive\Documents\Cirriculum vitae.docx','r')

# .write method adds the contents to the file and accepts string

lisst=['jdjdhd',83838,'hjhdhjuis']

# that is a  list
print(lisst)

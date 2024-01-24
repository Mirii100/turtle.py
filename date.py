import  calendar
print(calendar.calendar(2024))
def main():
    print('enter the names of three friends  ')
    name1=input('enter the first name  ')
    name2=input('enter the second name')
    name3=input('enter the third name  ')
    myfile=open('friends.txt','w')
    myfile.write(name1 + '\n')
    myfile.write(name2 +'\n')
    myfile.write(name3 +'\n')
    myfile.close()
    print('the names have been written to friends.txt ')
    # call the main function
main()
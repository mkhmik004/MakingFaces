#MKHABELE MMM
#28/06/2023
def convert(s):
    s=s.split()#create list of string
    print(s)
    for i in range(len(s)): #searches and goes through each string and examine selection string
        if s[i]== ":)":
            print("🙂",sep=' ',end=' ')
        elif s[i]==":(":
            print("🙁")
        else:
            print(s[i],sep=' ',end=' ')
def main():
    string=input("input string: ")  
    convert(string)
main()
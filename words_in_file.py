
def word_count(fname,search):
    with open(fname) as file:
        texts= file.read()
        words= texts.split()
    
    if(len(words)==0):
        print("Empty file")
    else :
    	dict={}
        for word in words:
            if word in dict:
    	        dict[word]+=1
            else:
                dict[word]=1
        if search in dict:
            print(search," occurs ",dict[search]," times...")
        else:
            print("not such word found...")



fname=input("Enter filename with extension in current directory: ")
search= input("Enter word to search: ")

word_count(fname,search)
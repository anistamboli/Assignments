unit=["","eka ", "dva ", "tri ", "catur ","panca ", "sat ", "sapta ","asta ", "nava ", "dasa "]
tens=["","dasha","vishanti","trishant","caturishant","pancashant ", "shathi ", "saptati ","ashiti ", "navati "]
hundreds=["shatam","hazar","dashahazar","laksh","dashlaksh","koti","dashkoti","arab","dasharab","kharab","dashkharab","neel","dashneel","padma","dashpadma","shankh","dashshankh","mahashankh"]


def num_to_word(num):
    l=len(str(num))
    div=10**(l-1)
    res=""
    while(num//10>=10):
        pre=num//div
        num=num%div
        div=div//10
        res+= (unit[pre]+hundreds[l-3]+" ")
        l-=1
        if(num<100):
            res+=(" "+unit[num%10]+tens[num//10])
    return res
        
num= input("Enter a number: ")

if(len(num)<=20):
    num=int(num)
    if num==0:
        res =("Shunya")

    elif (num>0):
        res = num_to_word(num)

    else :
        num=(-num)
        res =("Minus " + num_to_word(num))
else:
    res="Invalid Input"
    
print(res)

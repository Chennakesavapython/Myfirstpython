data_1 = "hello"
data_2 = 'hello'
data_3 = '''hello'''
data_4  = """hello"""
print(data_4)


#if we working with multi lines use """ must


#descrip = "heloonjnjj nd 
# kvfkgmgmklbmglkbbf lmblk"

descip = """the vfrnaskdm  vpefvwefvfd vm vk kkb
mbgbkhbhmblgmlbmlgkmblgmblmllbmmbkmbml"""

#using a single quote inside single quoote is not valid
#answer = 'i'm fine'

#use double quotes

answer = "i'm fine"
print(answer)


#answer = "im "good""
answer = 'im"good"'
print(answer)

#if you need both usse ''' or """

answer = """i'm fine and "good" """
print(answer)



#accessing 


text ="python"


#python goes indexing for accessing individual characters.

print(text[0])
print(text[2])

print(text[-2])



#invalid range

#print(text[10]) #IndexError: string index out of range


text ="python"
#using for loop to access each character
for i in text:
    print(i)


    print(text[1])
    print(text[2])
    print(text[3])


text = "python is very easy to learn "

#slicing

text = "python"
print(text[0:3]) #last is excluded  ->pyt
print(text[1:4]) #last is excluded  ->yth

print(text[1:])  #last is excluded  ->ython
print(text[:4])   #last is excluded ->pyth


print(text[1:4:1]) #last is excluded ->yth
print(text[0:4:2])#last is excluded ->pt



#for negative indexing default step is 1

text = "python"
print(text[-4:-1])  #tho
print(text[-4:-1:1])#tho
print(text[-4:-1:-1])#noth 
text = 'python'
print(text[1:4:-1])


#where we use -1 in step in slicing it cannot perform the reesult.

#typical use case of backward step

text ="python"
print(text[::-1])



#there is only ways to print
print(text[-2]+text[-3]+text[-4])

print(text[0:4:-1])



#string immutability


# = "python"
#TypeError: 'str' object does not support item assignment
#text[0]="p"
#print(text)




#reassigning  is okay
text = "python"

text = "Python" #new
print(text)


new_text = "j"+text[1:]
print(new_text)

#concat and repeat
#repeat * repated string
#concat ->join multiplr strings


str = "hello"
print(str*5)

#string Methods



print(dir(str))


mobile_number = input("enter mobile number")
valid_numbe = mobile_number.isdigit()
print(valid_numbe)


pan_num = input("enter the pan number")

valid_pan = pan_num.isalnum()
formatvalid_pan =pan_num.upper()

print(formatvalid_pan)
print(valid_numbe)



#every method functionality

print(help(str.isupper))
#Dictionaries

emp_dic = {}
print(type(emp_dic))
print(emp_dic)


#list = [1,2,3]
#tuples = (1,2,3,4)
#dictionaries = {key:value}

#numbers dict

dic_num = {1:100,2:200,3:300}
print(dic_num)
#print(dic_num[0])  #key Error

print(dic_num[3])  #300


#text dic

dic_tex = {"course1":"python","course2":"java","course3":"html"}
print(dic_tex)
print(dic_tex["course1"])


#mixed dic

dic_mix = {1:100,"coursse1":"python"}
print(dic_mix)
print(dic_mix[1])

#dict inside dict

students = {101:{"name":"ravi","age":30},
            102:{"name":"chenna","age":21}}

print(students)


#incorrect

#nums = {[1,2,3,4]:"python"} #TypeError: unhashable type: 'list'
nums = {(10,20,3,4):"python"}
print(nums)



#this is possible

dic_sub_dict = {101:["ravi","python","9am"],102:["chenna","python","9:30 am"]}
print(dic_sub_dict)



#update data ---> methods

fruits  = { "a":"apple","b":"banana"}
print(fruits)
fruits["c"] = "cherry"
print(fruits)

fruits["a"] = "apricot"


#numbers dict
print(fruits)




#class dict same as lists and tuples

emp_dic = dict()
print(type(emp_dic))
print(emp_dic)


#list = [1,2,3]
#tuples = (1,2,3,4)
#dictionaries = {key:value}

#numbers dict

dic_num = dict({1:100,2:200,3:300})
print(dic_num)
#print(dic_num[0])  #key Error

print(dic_num[3])  #300


#dictionary operator

print(dir(dic_num))


#update ---> add/update dict items

fruits  = { "a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)




#pop() - remmovve items with speciefied keys 

fruits = {"a":"apple","b":"banana"}
print(fruits)
#fruits.pop("c") #KeyError: 'c'
print(fruits)


#pop item() - remove the last inserted item
fruits  = { "a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)
#fruits.popitem("b") #TypeError: dict.popitem() takes no arguments (1 given)

#clear() - remove all items

fruits  = { "a":"apple","b":"banana"}
print(fruits)
fruits.clear()
print(fruits)



#access related methods

#get() - get the value for key
dic_num = {1:100,2:200,3:300}
print(dic_num)
#print(dic_num[0])  #key Error

print(dic_num[3])  #300

print(dic_num.get(0))  #if key is not present NO ERROR


#keys () -< returns all the keys only

dic_num = {1:100,2:200,3:300}
print(dic_num.keys())






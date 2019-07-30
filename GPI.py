from bs4 import BeautifulSoup
import requests

usr_name=input('Enter the user name : ')
url='https://www.github.com/'+usr_name
req=requests.get(url)
soup=BeautifulSoup(req.content,'html.parser')
#print(req.text)


#For profile Basic details section


main_tag=soup.find(class_='float-left col-9 col-md-12 pl-2 pl-md-0')#All the essential details are in this tag
details=[]

try:
 temp_tag=main_tag.find(itemprop="name")#actual name containging tag's attr
 print(f'Full Name : {temp_tag.text}','red')#Some colors are being added in this line and More colors are to be added in some other output lines syntax is print(colored('text','colorname'
 details.append(temp_tag.text)
except:
 pass
try:
 temp_tag=main_tag.find(itemprop="additionalName")#username containing tag's attr
 print(f'Username : {temp_tag.text}')
 details.append(temp_tag.text)
except:
 pass

try:
 temp_tag=main_tag.find(class_="p-note user-profile-bio js-user-profile-bio")# Bio containing tag's attr
 print(f'Bio : {temp_tag.text.strip()}')#using strip function to remove the whitespace from beginning of the bio
 details.append(temp_tag.text)
except:
 pass

try:
 temp_tag = main_tag.find(itemprop="worksFor")#work for containing tag attr
 print(f'Works For : {temp_tag.text.strip()}')
 details.append(temp_tag.text)
except:
 pass

try:
 temp_tag = main_tag.find(itemprop="homeLocation") # location tag attr
 print(f'Location : {temp_tag.text.strip()}')
 details.append(temp_tag.text)
except:
 pass

try:
 temp_tag = main_tag.find(itemprop="url") # user web address containg tag attr
 print(f'Web address : {temp_tag.text.strip()}')
 details.append(temp_tag.text)

except:
    pass #it will ignore any error occured so the remaining code from the try block can be executed






#For project and work details section


main_tag=soup.find(class_='col-lg-9 col-md-8 col-12 float-md-left pl-md-2')#This tag contains details about the project and work section

temp_tag = main_tag.find(href='/'+usr_name+'?tab=repositories') #total repos tag
temp_tag=temp_tag.find('span')
print(f'Repositories : {temp_tag.text.strip()}')

temp_tag = main_tag.find(href='/'+usr_name+'?tab=projects') #total projects tag
temp_tag=temp_tag.find('span')
print(f'Projects : {temp_tag.text.strip()}')

temp_tag = main_tag.find(href='/'+usr_name+'?tab=stars') #total stars tag
temp_tag=temp_tag.find('span')
print(f'Stars : {temp_tag.text.strip()}')

temp_tag = main_tag.find(href='/'+usr_name+'?tab=followers') #followers tag
temp_tag=temp_tag.find('span')
print(f'Followers : {temp_tag.text.strip()}')

temp_tag = main_tag.find(href='/'+usr_name+'?tab=following') #following tag
temp_tag=temp_tag.find('span')
print(f'Following : {temp_tag.text.strip()}')
print('\n')




#Detailed Section about all the deep details of the repositories


url='https://github.com/'+usr_name+'?tab=repositories'
req=requests.get(url)
soup=BeautifulSoup(req.content,'html.parser')
main_tag=soup.find_all(itemtype="http://schema.org/Code")
#print(main_tag)
ctr=0

for i in main_tag:#this will run for each repository

 print(f'*************** Repository #{ctr+1} **********************')
 try:
  temp=i.find(itemprop="name codeRepository")
  print(f'Name Of Repository : {temp.text.strip()}')
 except:
  pass

 try:
  temp=i.find(itemprop="description")
  print(f'Description : {temp.text.strip()}')
 except:
  pass

 try:
  temp = i.find(itemprop="programmingLanguage")
  print(f'Programming Language : {temp.text.strip()}')
 except:
  pass

 try:
  temp=i.find_all(class_="topic-tag topic-tag-link f6 my-1")#all the tags containig "tags" of project
  print('Tags : ',end='')
  for j in temp:#loop in case the tags are more than one
   print(f'{j.text.strip()}',end=', ')
  print('')
 except:
  pass

 try:
  temp=i.find_all(class_="muted-link mr-3")[0]#star tag attr
  print(f'Stars : {temp.text.strip()}')
 except:
  pass

 try:
  temp = i.find_all(class_="muted-link mr-3")[1]#fork tag attr
  print(f'Forks : {temp.text.strip()}')
 except:
  pass

 try:
  temp = i.find_all(class_="mr-3")[3]#this tag is not working properly so i.e. class_=mr-3 is giving same output as for Programming language
  print(f'License : {temp.text.strip()}')
 except:
  pass

 try:
  temp=i.find('relative-time')
  print(f'Last Update : {temp.text.strip()}')

 except:
     pass
 ctr+=1
 print('\n')


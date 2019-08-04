##################Github Profile Report Generator#############################
'''
This program inspects given GitHub Profile by provided username and generate report for that profile.
'''



from bs4 import BeautifulSoup
import requests
def entry(u_names): #driver function i.e. entry point
  for n in u_names:

    usr_name=str(n)
    url='https://www.github.com/'+usr_name
    req=requests.get(url)
    if req.text=="Not Found":
        print(f'User Does Not Exist : {usr_name}')
        continue
    soup=BeautifulSoup(req.content,'html.parser')
    final_details=basic_details(soup,usr_name)+repo_details(usr_name)
    records(usr_name,final_details)
    print(f'Report Generated for profile : {usr_name}')



def records(uname,details): #function to save records
    #fname=uname+'txt'
    f=open(uname+'.txt','w')
    for i in details:
        f.write(i)
        f.write('\n')




def basic_details(soup,usr_name):
    main_tag=soup.find(class_='float-left col-9 col-md-12 pl-2 pl-md-0')#All the essential details are in this tag
    details=[]
    try:
        temp_tag=main_tag.find(itemprop="name")#actual name containging tag's attr
        #print(f'Full Name : {temp_tag.text.strip()}','red')#Some colors are being added in this line and More colors are to be added in some other output lines syntax is print(colored('text','colorname'
        temp='Full Name : '+temp_tag.text.strip()
        details.append(temp)
    except:
        pass
    try:
        temp_tag=main_tag.find(itemprop="additionalName")#username containing tag's attr
        #print(f'Username : {temp_tag.text.strip()}')
        temp = 'Username : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass

    try:
        temp_tag=main_tag.find(class_="p-note user-profile-bio js-user-profile-bio")# Bio containing tag's attr
        #print(f'Bio : {temp_tag.text.strip()}')#using strip function to remove the whitespace from beginning of the bio
        temp = 'Bio : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass

    try:
        temp_tag = main_tag.find(itemprop="worksFor")#work for containing tag attr
        temp = 'Works For : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass

    try:
        temp_tag = main_tag.find(itemprop="homeLocation") # location tag attr
        temp = 'Location : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass

    try:
        temp_tag = main_tag.find(itemprop="url") # user web address containg tag attr
        #print(f'Web address : {temp_tag.text.strip()}')
        temp = 'Web Address : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass #it will ignore any error occured so the remaining code from the try block can be executed



    main_tag=soup.find(class_='col-lg-9 col-md-8 col-12 float-md-left pl-md-2')#This tag contains details about the project and work section

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=repositories') #total repos tag
    temp_tag=temp_tag.find('span')
    #print(f'Repositories : {temp_tag.text.strip()}')
    temp='Repositories : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=projects') #total projects tag
    temp_tag=temp_tag.find('span')
    #print(f'Projects : {temp_tag.text.strip()}')
    temp='Projects : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=stars') #total stars tag
    temp_tag=temp_tag.find('span')
    #print(f'Stars : {temp_tag.text.strip()}')
    temp='Stars : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=followers') #followers tag
    temp_tag=temp_tag.find('span')
    #print(f'Followers : {temp_tag.text.strip()}')
    temp='Followers : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=following') #following tag
    temp_tag=temp_tag.find('span')
    #print(f'Following : {temp_tag.text.strip()}')
    #print('\n')
    temp='Following : '+temp_tag.text.strip()
    details.append(temp)

    #for _ in details:
     #   print(_)
    return details


def repo_details(usr_name):
  url='https://github.com/'+usr_name+'?tab=repositories'
  req=requests.get(url)
  soup=BeautifulSoup(req.content,'html.parser')
  main_tag=soup.find_all(itemtype="http://schema.org/Code")
  ctr=0
  test=[]
  t=''
  for i in main_tag: #this will run for each repository

    #print(f'*************** Repository #{ctr+1} **********************')
    t = '\n*************** Repository #'+str((ctr+1))+'**********************'
    test.append(t)
    try:
        temp=i.find(itemprop="name codeRepository")
        #print(f'Name Of Repository : {temp.text.strip()}')
        t='Name Of Repository :'+temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp=i.find(itemprop="description")
        #print(f'Description : {temp.text.strip()}')
        t = 'Name Of Description :' + temp.text.strip()
        test.append(t)

    except:
        pass

    try:
        temp = i.find(itemprop="programmingLanguage")
        #print(f'Programming Language : {temp.text.strip()}')
        t = 'Programming Language :' + temp.text.strip()
        test.append(t)
    except:
        pass
    #tags aren't required to put inside the file thats why commenting this section
    '''try: #
        temp=i.find_all(class_="topic-tag topic-tag-link f6 my-1")#all the tags containig "tags" of project
        #print('Tags : ',end='')
        t=''
        for j in temp:#loop in case the tags are more than one
            #print(f'{j.text.strip()}',end=', ')
         t+= temp.text.strip()+' '
        test.append(t)
        #print('')
    except:
        pass
     '''
    try:
        temp=i.find_all(class_="muted-link mr-3")[0]#star tag attr
        #print(f'Stars : {temp.text.strip()}')
        t = 'Stars :' + temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp = i.find_all(class_="muted-link mr-3")[1]#fork tag attr
        #print(f'Forks : {temp.text.strip()}')
        t = 'Forks : '+temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp = i.find_all(class_="mr-3")[3]#this tag is not working properly so i.e. class_=mr-3 is giving same output as for Programming language
        #print(f'License : {temp.text.strip()}')
        t = 'License : ' + temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp=i.find('relative-time')
        #print(f'Last Update : {temp.text.strip()}')
        t = 'Last Update : '+temp.text.strip()
        test.append(t)
    except:
        pass
    ctr+=1
  return test




#################### Execution starts from here to i.e. calling entry function by passing the list of the name in that function
users=['blueoblin06','s0md3v','fabpot','taylorotwell']#sample list
print('welcome to the program!!!!')
entry(users)
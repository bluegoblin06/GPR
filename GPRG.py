
from bs4 import BeautifulSoup
import requests
from termcolor import colored
def entry(u_names): 
  for n in u_names:

    usr_name=str(n)
    url='https://www.github.com/'+usr_name
    req=requests.get(url)
    if req.text=="Not Found":
        print(f'User Does Not Exist : {usr_name}','red',attrs=['bold'])
        continue
    soup=BeautifulSoup(req.content,'html.parser')
    final_details=basic_details(soup,usr_name)+repo_details(usr_name)

    full_name=str(final_details[0])
    full_name=full_name.replace('Full Name : ','').replace(' ','_')

    records(full_name, final_details)
    print('Report Generated for profile : ',end='')
    print(colored(f'{full_name}','magenta',attrs=['bold']),end='')
    print(colored(f'({usr_name})', 'cyan', attrs=['bold']))


def records(uname,details): #function to save records
    #fname=uname+'txt'
    f=open(uname+'.txt','w',encoding='utf-8')
    for i in details:
        f.write(i)
        f.write('\n')




def basic_details(soup,usr_name):
    main_tag=soup.find(class_='float-left col-9 col-md-12 pl-2 pl-md-0')#All the essential details are in this tag
    details=[]
    try:
        temp_tag=main_tag.find(itemprop="name")#actual name containging tag's attr
        temp='Full Name : '+temp_tag.text.strip()
        details.append(temp)
    except:
        pass
    try:
        temp_tag=main_tag.find(itemprop="additionalName")#username containing tag's attr
        temp = 'Username : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass

    try:
        temp_tag=main_tag.find(class_="p-note user-profile-bio js-user-profile-bio")# Bio containing tag's attr
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
        temp = 'Web Address : ' + temp_tag.text.strip()
        details.append(temp)
    except:
        pass #it will ignore any error occured so the remaining code from the try block can be executed



    main_tag=soup.find(class_='col-lg-9 col-md-8 col-12 float-md-left pl-md-2')#This tag contains details about the project and work section

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=repositories') #total repos tag
    temp_tag=temp_tag.find('span')
    temp='Repositories : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=projects') #total projects tag
    temp_tag=temp_tag.find('span')
    temp='Projects : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=stars') #total stars tag
    temp_tag=temp_tag.find('span')
    temp='Stars : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=followers') #followers tag
    temp_tag=temp_tag.find('span')
    temp='Followers : '+temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=following') #following tag
    temp_tag=temp_tag.find('span')
    temp='Following : '+temp_tag.text.strip()
    details.append(temp)
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

    t = '\n*************** Repository #'+str((ctr+1))+'**********************'
    test.append(t)
    try:
        temp=i.find(itemprop="name codeRepository")
        t='Name Of Repository :'+temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp=i.find(itemprop="description")
        t = 'Description Of Repository : ' + temp.text.strip()
        test.append(t)

    except:
        pass

    try:
        temp = i.find(itemprop="programmingLanguage")
        t = 'Programming Language :' + temp.text.strip()
        test.append(t)
    except:
        pass
    try:
        temp=i.find_all(class_="muted-link mr-3")[0]#star tag attr
        t = 'Stars :' + temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp = i.find_all(class_="muted-link mr-3")[1]#fork tag attr
        t = 'Forks : '+temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp = i.find_all(class_="mr-3")[3]#this tag is not working properly so i.e. class_=mr-3 is giving same output as for Programming language
        t = 'License : ' + temp.text.strip()
        test.append(t)
    except:
        pass

    try:
        temp=i.find('relative-time')
        t = 'Last Update : '+temp.text.strip()
        test.append(t)
    except:
        pass
    ctr+=1
  return test



if __name__ == '__main__':

    #################### Execution starts from here to i.e. calling entry function by passing the list of the name in that function
    users=['fabpot','andrew','bluegoblin06']
    print(colored('Profile Report Generation Started!!!!','blue'))
    entry(users)
    print(colored('Thank You For Using This Tool!!! Have A Nice Day!!!!','yellow',attrs=['bold']))

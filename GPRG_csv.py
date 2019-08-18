
from bs4 import BeautifulSoup
import requests
from termcolor import colored
import csv

def entry(u_names):
  csv_file()
  for n in u_names:

    usr_name=str(n)
    url='https://www.github.com/'+usr_name
    req=requests.get(url)
    if req.text=="Not Found":
        print(f'User Does Not Exist : {usr_name}','red',attrs=['bold'])
        continue
    soup=BeautifulSoup(req.content,'html.parser')
    profile_details=basic_details(soup,usr_name)

    full_name=str(profile_details[0])
    full_name=full_name.replace('Full Name : ','').replace(' ','_')
    file_name=full_name+'('+usr_name+')'
    repositories=repo_details(usr_name)

   # records(file_name, final_details)

    records(file_name,profile_details,repositories)
    print('Report Generated for profile : ',end='')
    print(colored(f'{full_name}','red',attrs=['bold']),end='')
    print(colored(f'({usr_name})', 'cyan', attrs=['bold']))


def csv_file():
 row = ['Full Name', 'User Name', 'Bio', 'Works For', 'Location', 'Web Address', 'Repositories', 'Projects', 'Starts',
        'Followers', 'Following']
 with open('Records.csv','w') as file:
  writer=csv.writer(file)
  writer.writerow(row)
 file.close()

def records(file_Name,record_row,repos):
 columns = ['Sr. No.', 'Name Of Repo', 'Description', 'Programming Language', 'Stars', 'Forks', 'License',
            'Last Update', 'Watch', 'Issues', 'Projects', 'Pull Requests', 'Commits', 'Branches', 'Releases']
 with open('Records.csv','a') as file:
  writer=csv.writer(file)
  writer.writerow(record_row)
 file.close()
 rows=[]
 with open(file_Name + '.csv', 'w') as file:
     writer = csv.writer(file)
     writer.writerow(columns)
 file.close()
 with open(file_Name+'.csv','a') as file:
     writer=csv.writer(file)
     for i in repos:
              writer.writerow(i)
 file.close()



def basic_details(soup,usr_name):
    main_tag=soup.find(class_='float-left col-9 col-md-12 pl-2 pl-md-0')#All the essential details are in this tag
    details=[]
    try:
        temp_tag=main_tag.find(itemprop="name")#actual name containging tag's attr
        temp=temp_tag.text.strip()
        details.append(temp)
    except:
     details.append('')
     pass


    try:
        temp_tag=main_tag.find(itemprop="additionalName")#username containing tag's attr
        temp = temp_tag.text.strip()
        details.append(temp)
    except:
        details.append('')
        pass

    try:
        temp_tag=main_tag.find(class_="p-note user-profile-bio js-user-profile-bio")# Bio containing tag's attr
        temp = temp_tag.text.strip()
        details.append(temp)
    except:
        details.append('')
        pass

    try:
        temp_tag = main_tag.find(itemprop="worksFor")#work for containing tag attr
        temp = temp_tag.text.strip()
        details.append(temp)
    except:
        details.append('')
        pass

    try:
        temp_tag = main_tag.find(itemprop="homeLocation") # location tag attr
        temp = temp_tag.text.strip()
        details.append(temp)
    except:
     details.append('')
     pass

    try:
        temp_tag = main_tag.find(itemprop="url") # user web address containg tag attr
        temp = temp_tag.text.strip()
        details.append(temp)
    except:
     details.append('')
     pass

    main_tag=soup.find(class_='col-lg-9 col-md-8 col-12 float-md-left pl-md-2')#This tag contains details about the project and work section

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=repositories') #total repos tag
    temp_tag=temp_tag.find('span')
    temp = temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=projects') #total projects tag
    temp_tag=temp_tag.find('span')
    temp = temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=stars') #total stars tag
    temp_tag=temp_tag.find('span')
    temp = temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=followers') #followers tag
    temp_tag=temp_tag.find('span')
    temp = temp_tag.text.strip()
    details.append(temp)

    temp_tag = main_tag.find(href='/'+usr_name+'?tab=following') #following tag
    temp_tag = temp_tag.find('span')
    temp = temp_tag.text.strip()
    details.append(temp)

    return details


def repo_details(usr_name):
  url='https://github.com/'+usr_name+'?tab=repositories'
  req=requests.get(url)
  soup=BeautifulSoup(req.content,'html.parser')
  main_tag=soup.find_all(itemtype="http://schema.org/Code")
  ctr=0
  final_lis=[]
  t=''
  repo_name = ''
  for i in main_tag: #this will run for each repository
    test=[]
    t = str((ctr+1))
    test.append(t)
    try:
        temp=i.find(itemprop="name codeRepository")
        t=temp.text.strip()
        repo_name=temp.text.strip()
        test.append(t)
    except:
        test.append('')
        pass

    try:
        temp=i.find(itemprop="description")
        t =  temp.text.strip()
        test.append(t)

    except:
        test.append('')
        pass
    try:
        temp = i.find(itemprop="programmingLanguage")
        t = temp.text.strip()
        test.append(t)
    except:
        test.append('')
        pass
    try:
        temp=i.find_all(class_="muted-link mr-3")[0]#star tag attr
        t = temp.text.strip()
        test.append(t)
    except:
        test.append('')
        pass

    try:
        temp = i.find_all(class_="muted-link mr-3")[1]#fork tag attr
        t = temp.text.strip()
        test.append(t)
    except:
        test.append('')
        pass

    try:
        temp = i.find_all(class_="mr-3")[3]#this tag is not working properly so i.e. class_=mr-3 is giving same output as for Programming language
        t = temp.text.strip()
        test.append(t)
    except:
        test.append('')
        pass

    try:
        temp=i.find('relative-time')
        t = temp.text.strip()
        test.append(t)
    except:
        test.append('')
        pass
    try:
            #print(f'############### {repo_name} ####################')
            r1=requests.get('https://www.github.com/'+usr_name+'/'+repo_name)
            soup1 = BeautifulSoup(r1.content, 'html.parser')
            temp = soup1.find_all(class_="social-count")
            try:
                t=temp[0].text.strip()
                test.append(t)
                '''t = 'Star : ' + temp[1].text.strip()
                test.append(t)
                t = 'Fork : ' + temp[2].text.strip()
                test.append(t)'''
            except:
                test.append('')
                pass
            temp = soup1.find_all(class_="Counter")
            try:
               t =   temp[0].text.strip()
               test.append(t)
               t =  temp[1].text.strip()
               test.append(t)
               t =  temp[2].text.strip()
               test.append(t)
            except:
                test.append('')
                pass
            temp = soup1.find_all(class_="num text-emphasized")
            try:
               t = temp[0].text.strip()
               test.append(t)
               t = temp[1].text.strip()
               test.append(t)
               t = temp[2].text.strip()
               test.append(t)
               #This doesnt work fine
               '''t = 'Contributors : ' + temp[3].text.strip()
               test.append(t)'''
            except:
                test.append('')
                pass
        #Lets forget this for a while
            '''
            temp = soup1.find_all(class_='lang')
            temp1 = soup1.find_all(class_='percent')
            try:
               test.append('     File Type Ratio     ')
               for i in range(len(temp)):
                t=temp[i].text + ' : ' + temp1[i].text
                test.append(t)
            except:
                test.apend('')
                pass
                '''
    except:
        pass
    ctr+=1
    final_lis.append(test)
  return final_lis



if __name__ == '__main__':

    #################### Execution starts from here to i.e. calling entry function by passing the list of the name in that function
    users=['s0md3v','fabpot','andrew']#More profile names can be added in this list of usrnames
    print(colored('Profile Report Generation Started!!!!','blue',attrs=['reverse']))
    entry(users)
    print(colored('Thank You For Using This Tool!!! Have A Nice Day!!!!','yellow',attrs=['bold']))

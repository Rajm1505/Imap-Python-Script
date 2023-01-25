import easyimap as ei
from decouple import config

server = ei.connect("imap.gmail.com", config("IMAP_USER"),  config("IMAP_PASSWORD"))

all_mailids = server.listids(500) #Gets id of all the avaliable emails
"""
all_mailids = server.unseen(500) 
.unseen The method to retrieve mailobjects of all the unseen mail
Body of mail objects can be retrieved all_mailids by used .body directly to the var
eg; allmailids[0].body
"""
print("Mailids: ",all_mailids)

mail_titles = {}
filtered_mailids = {}

for i in range(0,len(all_mailids)):
    email = server.mail(all_mailids[i],include_raw=True)
    if 'Re:' == email.title[0:3]: #Filtering the Replied mails 
        mail_titles[i+1] = email.title 
        filtered_mailids[i+1] = all_mailids[i]

# print(mail_titles)
# print(filtered_mailids)
for key,value in mail_titles.items():
    print(key," : ",value)

if filtered_mailids:
    mail_choice = int(input("Which mail you want to retrieve: "))
    email = server.mail(filtered_mailids[mail_choice])
    print(email.body)
else:
    print("No Replied mails Found")

import easyimap as ei
from decouple import config

server = ei.connect("imap.gmail.com", config("IMAP_USER"),  config("IMAP_PASSWORD"))

unseen_mails = server.unseen(20)
"""
unseen_mails = server.unseen(500) 
.unseen The method to retrieve mailobjects of all the unseen mail
Body of mail objects can be retrieved all_mailids by using .body directly to the variable
eg: allmailids[0].body
"""
print("Unseen Mails: ",unseen_mails)

mail_titles = {}
filtered_mailids = {}

for i in range(0,len(unseen_mails)):
    mail_titles[i+1] = unseen_mails[i].title 
    filtered_mailids[i+1] = (str(unseen_mails[i].uid)).encode()

print(mail_titles)
print(filtered_mailids)
for key,value in mail_titles.items():
    print(key," : ",value)

if unseen_mails:
    mail_choice = int(input("Which mail you want to retrieve: "))
    email = server.mail(filtered_mailids[mail_choice],include_raw=True)
    print(email.body)
else:
    print("No Unseen mails Found")

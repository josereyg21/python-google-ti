# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
#  Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    emails = []
    for domain, users in domains.items():
          for user in users:
              emails.append(user+'@'+domain)
    return (emails)



print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def email_list(domains):
    emails = []
    for y in domains:
        for i in range(len(domains[y])):
            emails.append(domains[y][i]+ "@" + y)

    return emails


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
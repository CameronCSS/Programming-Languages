email = 'stephen.marquard@uct.ac.za Sat Jan 5 2008'

findat = email.find('@')

findspace = email.find(' ',findat)

emailhost = email[findat + 1: findspace]

print(emailhost)
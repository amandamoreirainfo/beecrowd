senhaUser1 = "123456"
senhaUser2 = "Abcde12"
senhaUser3 = "progrAmador92"
senhaUser4 = "iasd ufa 13j daf"
senhaUser5 = "201830928143A"
senhaUser6 = "g@mer_21"

#123456 - False ok
#Abcde12 - True ok
#progrAmador92 - True ok
#iasd ufa 13j daf - False
#201830928143A - True ok
#g@mer_21 - False

print(senhaUser1.isalpha())
print(senhaUser2.isalnum())
print(senhaUser3.isalnum())
print(senhaUser4.isalpha())
print(senhaUser5.isalnum())
print(senhaUser6.isalpha())
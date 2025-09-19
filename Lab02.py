#Samples
'''
#Task 1
with open('sample.txt', 'r') as f:
    for line in f:
        print(line)                 #prints txt file

#Task 2
with open('sample.txt', 'r') as f:  #with open is a function that reads in files
    for line in f:
            print(line.strip())     #the .strip function removes the line bespace between words

#Task 3
with open('output.txt', 'w') as f:
    f.write("This is a new file.\n")
    f.write("It has two lines.\n")

#Task 4
import re

pattern = r"at"                    #prints the word cat if it matches
text = "The cat sat on the mat."

matches = re.findall(pattern, text)
print(matches)

#Task 5
import re 
pattern = r"[A-Za-z]+"
text = "Order 123 was placed on 2023-05-01."
print(re.findall(pattern, text))


#Task 6
import re 
pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1  and 10.0.0.5 at 10:30"
print(re.findall(pattern, text,))
'''



#Lab excersises
#Step1 - read in the auth file, print out only the ip addresses 

import re 
IpFound=[] 
ips = []                                                #makes an empty list for the found ip addresses 
with open('auth.log', 'r') as f:                        #opens the file auth.log
    for line in f:                                      #for loop reads file 
        IpChecker = (line.strip())                      #ipchecker variable strips the empty lines between
        pattern = r"\d+\.\d+\.\d+\.\d+"                 #pattern is given a parameter for what to search 
        x=re.findall(pattern, IpChecker)                #ip addresses get added to the empty list
        for ip in x:                                    #ip is a variable name used in the list
            ips.append(ip)

#Step 2 - print all the Ip's as a list

#print(ips)
uniqueIps = set(ips)
print("Unique IPs:")

for ip in (uniqueIps):
    print(uniqueIps)  










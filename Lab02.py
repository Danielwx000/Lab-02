#Name:      Daniel Vintila
#Date:      19/9/25
#ID:        C00307041
#Lab:       02
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
uniqueIps = set(ips)                                    #setting the ips as a set 
print("Unique IPs:")                                    #printing a line 

for ip in (uniqueIps):                                  #for loop to traverse the set
    FinalIp = (ip)                                      #assigning a variable to the set 
    print(FinalIp)                

with open('Unique_Ip.txt', 'w') as f:                   #creating a file called unique_ip and givign write permissions
    for ip in uniqueIps:                                #traversing through list 
        f.write(ip + '\n')                              #prints the list on a new line each time







cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
from collections import defaultdict
import collections

# def subdomainVisit(cpdomains):
#     cp = collections.defaultdict()

#     for cpdomain in cpdomains: 
#         current = cpdomain.split(' ')
#         count = int(current[0]) 
#         domain = current[1]

#         currentDomain = ""
#         for sub in domain.split('.')[::-1]:
#             if currentDomain == "":
#                 currentDomain = sub
#             else : 
#                 currentDomain = sub+ "."+currentDomain
#                 cp[currentDomain]+= count
    
#     result = []
#     for key in cp.keys():
#         result.append(str(cp[key])+ " "+key)
    
#     return result

# result = subdomainVisit(cpdomains)
# print(result)

n = 121
ns = str(n)
for i in ns: 
    print(ns[i])
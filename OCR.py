

def help(S):
    S = list(S)

    count = 1
    for i in range(0, len(S)):
        if isinstance(S[i], int):
            count = int(S[i]) - 1
        count += 1

    return count


def solution(S, T):
    if help(S) == help(T):
        solDict1 = set(S)
        solDict2 = set(T)
        commonElement = (solDict1 & solDict2)

        if len(commonElement) == 0:
            return True
        elif len(commonElement) > 0:
            commonElement = list(commonElement)
            for i in range(0, len(commonElement)):
                if S.index(commonElement[i]) == T.index(commonElement[i]):
                    return True
                elif solDict1==solDict2:
                    return True 
        else:
            return False
    return False  


print(final("ba1", "1Ad"))


h = ['0','1','2','3','4','5','6','7','8','9']
  def check(s):
    count = 0
    for i in range(0,len(s)): 
      c = S[i]
      if c in h:
        c= int(c)
        count+=c
      else:
        count+=1
    return count
  
  if check(S) == check(T):
      for i in range (0,len(S)):
          for j in range(0,len(T)): 
            if(S[i] and T[j] not in h) and (S[i]!=T[j]):
                return False 
  elif (check(S) ==check(T)): 
    return True




def ans(s):
#     t = []
#     i = 0
#     n = len(s)
#     count = 0
#     while (i<n):
#         c = s[i]
#         if c.isdigit():
#             t.append(c)
#         elif i<n-1 and c ==s[i+1]:
#             count+=1
#             i+=1
#             t.append(str(count))
#         else: 
#             t.append(c)
#         i+=1
#         print (t)
#     return ''.join(t)





def solution(A):
    # write your code in Python 3.6
    var = len(A)*2

    for i in range(1,7):
        count = 0
        for x in A: 
            if x ==i:
                count+=0
            elif x+i ==7:
                count +=2
            else:
                count+=1
        if count<var:
            var = count
    return var
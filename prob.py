# I/P : score = [700,500,650] O/P: 

#ranges = ["Poor":"400-499", "Fair":"500-599", "Good":"600-699", "Excellent":"700-799", "Elite":"800-850"]

#output in the format - [Fair: 33%, Good: 33%, Good: 33%]  

#1. Read from the I/P array and categirze
#2. Print the count 
#3. Prin the percentage 
#4. Output as asked

score = [501,625,789,821,456]



def Result(score):
    count = 0
    ans = {"Poor":0,"Fair":0,"Good":0,"Excellent":0,"Elite":0}
    for i in range(len(score)-1): 

    
        if (score[i]>= 400 and score[i]<500) :
            count+=1
            ans["Poor"] = count

        elif (score[i]>=500 and score[i]<600):
            count+=1
            ans["Fair"] = count
        
        elif (score[i]>=600 and score[i]<700):
            count+=1
            ans["Good"] = count
        
        elif (score[i]>=700 and score[i]<800):
            count+=1
            ans["Excellent"] = count
        
        elif (score[i]>=800 and score[i]<=850):
            count+=1
            ans["Elite"] = count
        else: 
            print("Out of range")

    return ans 

finalsore = Result(score)
print(finalsore)
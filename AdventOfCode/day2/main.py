file = open("input.txt","r")
ligne = file.readlines()
pts = 0
for car in ligne :  
    if car[0] == "A":
        if car[2] == "Y":
          pts += 1+3
        
        elif car[2] == "Z":
            pts += 2+6
        
        elif car[2] == "X":
            pts += 3+0
            
    elif car[0]== "B":
        
        if car[2]=="X":
            pts += 1+0
    
        elif car[2] == "Y":
            pts += 2+3
        
        elif car[2] == "Z":
            pts += 3+6 
   
    elif car[0] == "C":
        
        if car[2]=="X" :
            pts += 2+0
        
        elif car[2]=="Y" :
            pts+=3+3
        
        elif car[2]=="Z" :
            pts+= 1+6
file.close()
print(pts)
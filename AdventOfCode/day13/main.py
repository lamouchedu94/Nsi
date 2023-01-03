with open("input.txt", "r") as f :
    data = f.readlines()
    f.close()

def run(data) :
    for i in range(0,len(data),2):
        compare(data[i], data[i+1])
        
def compare(tab1, tab2) :
    curs = 0
    while len(tab1)<= curs and len(tab2) <= curs :
        if tab1[curs] < tab2[curs]:
            pass
run(data)


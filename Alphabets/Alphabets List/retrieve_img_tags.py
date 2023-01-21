import re
 
with open("img.html", mode="r") as f:
    lines = f.readlines()

img_href = []

cntr = 0
for i, v in enumerate(lines):
    x = re.search(r"\"https:.+?\"", v)    
    try:
        
        if(i % 2 == 0):
            print("img8: " + x.group() + ",")
            print(chr(cntr + 65))
            cntr += 1
            print()
    except:
        #print("Exception: " + i)
        pass 
    
    


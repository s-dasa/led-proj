color = input('This program returns the RGB value of your ROYGBIV color.')
#print(color)
arr = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
Dict = {"red":[255, 0, 0],"orange":[255, 127, 0], "yellow":[255, 255, 0],"green":[0, 255, 0],"blue":[0, 0, 255],"indigo":[39, 0, 5],"violet":[139, 0, 255]}

index = len(Dict) -1
while (index!=-1):
    #print(index)
    #print(arr[index])
    if (Dict[color.lower()]!=None):
        print("Your color is encoded with", Dict[color.lower()])
        break
    else:
        index = index-1



    

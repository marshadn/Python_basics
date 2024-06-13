with open("twinkle.txt","r") as f:
    if('twinkle' in f.read()):
        print("twinkle is present in the poem")
        
    else:
         print("twinkle is not present in the poem")
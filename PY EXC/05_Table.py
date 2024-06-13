for i in range(2,21):
    table=''
    for j in range(1,11):
       table+= f"Table {i} X {j}={i * j}\n"
        
with open("table.txt","w") as f:
    f.write(table)

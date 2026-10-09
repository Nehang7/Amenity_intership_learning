import csv
data =[
    ["Name","Age"],
    ["Nehang",22],
    ["Harsh",21],
    
]

with open('example.csv','w',newline='')as f:
    writer=csv.writer(f)
    writer.writerows(data)
    print("writing done")

with open('example.csv','r')as r:
    reader=csv.reader(r)
    for row in reader:
        print("reading from file "row)

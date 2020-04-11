import csv
def create_csv():
    path = "mnist_dataset/aa.csv"
    with open(path,'w') as f:
        csv_write = csv.writer(f)
        csv_head = ['good','bad']
        #csv_head = csv_head.encode()
        csv_write.writerow(csv_head)


create_csv()
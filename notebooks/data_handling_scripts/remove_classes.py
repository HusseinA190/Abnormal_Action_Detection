import os

label_org = r'F:\Model\data\fire&smoke\main3\train\labels'


label_dst = r'F:\Model\data\fire&smoke\main3\base_0\train_0\labels'



for label in os.listdir(label_org):

    with open(os.path.join(label_org,label)) as file:

        lines = file.readlines()
    

    new_lines = [line for line in lines if line.split()[0]!='1']

    print(new_lines)

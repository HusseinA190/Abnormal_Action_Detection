import os
import shutil
import random


src = r"F:\Model\data\Fire_Smoke\smoke_ones\labels_renamed"

dst = r"F:\Model\data\Fire_Smoke\smoke_ones\images_renamed"

move_lab = r"F:\Model\data\Fire_Smoke\smoke_ones\moved_img"
move_img = r"F:\Model\data\Fire_Smoke\smoke_ones\moved_lab"


rand_select = random.sample(os.listdir(dst) , 4000)


print(rand_select)


for i in rand_select:
    shutil.move(os.path.join(dst,i) , move_img)   
    shutil.move(os.path.join(src,os.path.splitext(i)[0]+".txt") , move_lab)   


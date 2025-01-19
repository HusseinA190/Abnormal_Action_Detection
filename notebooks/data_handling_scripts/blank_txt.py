import os


src_path = r"F:\Model\data\fire&smoke\bg_640x640"

dst_path = r"F:\Model\data\fire&smoke\labels_640x640"


for img in os.listdir(src_path):
    
    open(os.path.join(dst_path,os.path.splitext(img)[0]+'.txt'),'x')
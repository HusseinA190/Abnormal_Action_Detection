import os 
import uuid



src_files = r"F:\Model\projects_violence\bg_data\bg_640x640"
lab_files = r"F:\Model\projects_violence\bg_data\bg_labels_640x640"

go = r"F:\Model\projects_violence\bg_data\vio_bg\renamed"
lab_go = r"F:\Model\projects_violence\bg_data\vio_bg\labels"

# pth = r"F:\Model\data\BG_Train - Copy"

num = 0 
for img in os.listdir(src_files):

    ext = img.split('.')[-1]
    
    ind = len(ext)*-1
    ind -=1

    # os.rename(os.path.join(pth,img) , os.path.join(go,f"FGB{str(uuid.uuid4())}.jpg") )
    # os.rename(src -> old_file_full_path , dst -> new_file_full_path_with_ext)
    os.rename(os.path.join(src_files,img),os.path.join(go,"VIOLENCEE_BG"+str(num)+".jpg"))

    os.rename(os.path.join(lab_files,os.path.splitext(img)[0]+".txt"),os.path.join(lab_go,"VIOLENCEE_BG"+str(num)+".txt"))


    num+=1

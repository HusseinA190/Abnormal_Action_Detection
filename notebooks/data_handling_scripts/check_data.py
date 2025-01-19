import os 
import shutil

src_path = r"F:\Model\data\fire&smoke\Fire&SmokeData\train\labels"

img_path = r"F:\Model\data\fire&smoke\Fire&SmokeData\train\images"

move = r"F:\Model\projects_violence\model_test\frames\labels"

class_dict = {"Violence" : 0 , "Weapon" : 0 , "Fire" : 0 , "Smoke" : 0}

label_names = set()
img_list = set()
imgs_ext = dict()



value = 1
c=1

# for img in os.listdir(img_path):

#     imgs_ext[os.path.splitext(img)[1]] = imgs_ext.get(os.path.splitext(img)[1] , 0) + 1


# print(imgs_ext)

for file in os.listdir(move):
    
    try:
        content = open(os.path.join(move,file))
        
        content_list = content.readlines()
            
        for i , item in enumerate(content_list):
            
            # if item.split()[0] == '3':
            #     class_dict['Smoke'] = class_dict.get('Smoke' ,  0 ) +1
            #     img_list.add(file)
            #     break

            # if item.split()[0] == '0':
            #     class_dict['Violence'] = class_dict.get('Violence' ,  0 ) + 1
            #     img_list.add(file)
            #     break

            # if item.split()[0] == '1':
            #     class_dict['Weapon'] = class_dict.get('Weapon' ,  0 ) + 1
            #     img_list.add(file)
            #     break

            if item.split()[0] == '2':
                class_dict['Fire'] = class_dict.get('Fire' ,  0 ) + 1
                img_list.add(file)
                break
            # pass


        # value +=1
            
            # if item.split()[0]=='2':
            #     label_names.add(file)
    except:
        print(c)
        c+=1


# print(label_names)

print(class_dict)
# print(len(img_list))
# print(img_list)




# moving labels that contains either smoke or fire 
# for lab in img_list:

#     shutil.move(os.path.join(src_path,lab) , move)
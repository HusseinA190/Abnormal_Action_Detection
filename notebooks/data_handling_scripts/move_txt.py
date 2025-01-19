import shutil
import os 


dst = r"F:\Model\projects_violence\model_test\frames\imgs"
src_path = os.listdir(dst)

# print(len(src_path))
src = r"F:\Model\projects_violence\model_test\frames\labels"
labels_path = os.listdir(src)


match = r"F:\Model\data\fire&smoke\Fire&SmokeData\train\labels"


# s = set()

found_lab = set()
not_found_lab = set()
not_found_img = set()
found_img = set()
moving_labels = set()
moving_imgs = set()

c=0

# for img in src_path:
    
#     # s.add(img.split('.')[-1])
    
#     ext = img.split('.')[-1]
    
#     ind = len(ext)*-1
#     ind -=1
    

#     # with open(os.path.join(src,img[:ind]+".txt")) as file:
#     #         if len(file.read()) ==0:
#     #             os.remove(os.path.join(dst,img))  
              
# # # #     if img[:ind]+'.txt' not in labels_path:
# # # #         # os.remove(os.path.join(src,img[:ind]+'.txt'))
# # # #         print('nn')

# # # #     moving_labels.add(os.path.splitext(img)[0]+'.txt')
    
        
#     if os.path.splitext(img)[0]+'.txt' not in labels_path:
#         os.remove(os.path.join(dst , img))
# # # #         # print(img)
        # found_lab.add(os.path.splitext(img)[0]+'.txt')
#         not_found_img.add(os.path.splitext(img)[0]+os.path.splitext(img)[1])
#             # ext_dict[ext] = ext_dict.get(ext,0)+1  
#             # c+=1


# print(found_lab)


# for label in labels_path:

#     with open(os.path.join(src,label)) as file:
    
#         if len(file.read()) ==0 :
#             # os.remove(os.path.join(dst,os.path.splitext(label)[0]+'.jpg'))
#             c+=1


# print(c)

# print(f" The number of samples that not contains objects {c}")



# for img in src_path:
    
# #     l = os.path.splitext(img)
# #     moving_labels.add(l[0]+".txt")
#     if img not in found_img:
#         not_found_img.add(img)



# for l in labels_path:

#     if l not in found_lab:
#         os.remove(os.path.join(src,l))

# gg=0

# for label in labels_path:

#     if label not in moving_labels:
#         os.remove(os.path.join(src,label))

# print(f" not found labels are : {gg}")

for label in labels_path:
    
    with open(os.path.join(src,label)) as file:
    
        if file.read() == '':
            c+=1
    #         moving_imgs.add(os.path.splitext(label)[0]+'.jpg')

# # # #         # os.system(os.path.join(src,label))
            # file.close()    
            # os.remove(os.path.join(src,label))

    # if label not in found_lab:
    #     not_found_lab.add(label)


print(c)


# print(f" Found : {len(not_found_lab)}")
# # # print(f" Not - Found : {len(not_found_img)}")
# # # print(f" Moving labels {len(moving_labels)}")


# for i in not_found_lab:
#     os.remove(os.path.join(src,i))


# for i in not_found_img:
#     os.remove(os.path.join(dst,i))

# for i in moving_labels:
#     shutil.move(os.path.join(src,i) , r"F:\Model\data\fire&smoke\main\high_quality_train\labels" )


# for i in moving_imgs:
#     shutil.move(os.path.join(dst,i) , r"F:\Model\data\Violence_Data\Violence\resized_data\VIO_2\bg" )





















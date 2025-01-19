if item.split()[0] == '0':
                class_dict['Violence'] = class_dict.get('Violence' ,  0 ) + 1
                img_list.add(file)
                break
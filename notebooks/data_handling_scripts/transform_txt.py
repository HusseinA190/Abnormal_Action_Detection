import os 

label_org = r'F:\Model\data\Weapons\Weapons_Data\valid\labels'

label_src = r'F:\Model\data\Weapons\w_1base\valid\labels'




for label in os.listdir(label_org):
    
    with open(os.path.join(label_org,label)) as file:

        lines = file.readlines()
    

    # new_lines = [line for line in lines if line.split()[0]!='1']

    for i , item in enumerate(lines):
        
        content = lines[i]
        
        content = content.split()
            
        content = ['1' if i == '0' else i for i in content]
        # content = ['3' if i == '1' else i for i in content]
        # content = ['1' if i == '7' else i for i in content]
        # content = ['0' if i == '3' else i for i in content]
        # content = ['0' if i == '4' else i for i in content]
        # content = ['0' if i == '5' else i for i in content]
        
        
        
        content = ' '.join(content)
        
        
        lines[i] = content 
        
        lines[i]+='\n'
    
    new_file = open(os.path.join(label_src,label),'w')
    
    new_file.writelines(lines)
    new_file.close()
    
    
        
        
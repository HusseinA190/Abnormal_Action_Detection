import cv2 as cv
import uuid
import os

# define the number of frames to be choosen
SEQUENCE_LENGTH = 20
src = r"F:\Model\projects_violence\model_test\model_present.mp4"
# others = os.listdir(src)

loc_videos = r'F:\Model\projects_violence\model_test\model_present_frames'

# # com_pth = 


# print(others)



# for folder in os.listdir(src):

cap = cv.VideoCapture(src)

video_frames_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

#         # Calculate the the interval after which frames will be added to the list.
skip_frames_window = max(int(video_frames_count/SEQUENCE_LENGTH), 1)

print(video_frames_count,skip_frames_window)


vid_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)



    # skip_frame = max(int(vid_frames/seq_len),1)



    # print(skip_frame)


# while cap.isOpened():
for f in range(SEQUENCE_LENGTH):
    
    # cap.set(cv.CAP_PROP_FRAME_COUNT,i*skip_frames_window)
    cap.set(cv.CAP_PROP_POS_FRAMES, f * skip_frames_window)
    
    ret , frame = cap.read()

    try:
        frame = cv.resize(frame,(640,640))
        
        if not ret:
            break
        
        cv.imwrite(os.path.join(loc_videos,"detection"+str(uuid.uuid1())+'.jpg'),frame)
    except:
        print("empty")
    

cap.release()
# cv.destroyAllWindows()














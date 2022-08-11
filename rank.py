import os
import cv2
import pandas as pd

# short script for easy methodical shots rating 
# when launched script will show the videos from configuration folder
# pressing q,e,r ranks the video accordingly as P, U, X
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

path = os.getcwd()
# configuration
new_path = os.path.join(path, "shots")
vid_q = []
os.chdir(new_path)
df = pd.DataFrame(columns=["File:","Tag:"])
for file in os.listdir():
    if file.endswith(".mp4"):
        vid_q.append(file)
window_name = "window"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
i = 0
tablica = []
for video in vid_q:
    print(i,"/500")
    new_path_v = os.path.join(new_path, video)
    if os.path.getsize(new_path_v) > 100 * 1024:
        cap = cv2.VideoCapture(new_path_v)
        make_720p()
        while(cap.isOpened()):
            ret, frame = cap.read()
            try:
                cv2.imshow(window_name,frame)
                key = cv2.waitKey(50) 
                if key == 113: #q
                    df.loc[i] = [str(video)] + ['P']
                    break
                if key == 101: #e
                    df.loc[i] = [str(video)] + ['U']
                    break
                if key == 114: #r
                    df.loc[i] = [str(video)] + ['X']
                    break
            except: 
                df.loc[i] = [str(video)] + ['X']
                break
        i = i + 1
        cap.release()
        cv2.destroyAllWindows()
os.chdir(path)
df.to_csv("csv/grading.csv", index=False)
print("tablica z bledami:", tablica)

# this part joins mitsu gradings with user input, dirs need to be configured
df1 = pd.read_csv("csv/grading.csv")
df2 = pd.read_csv("csv/all_res.csv")
df_final = pd.merge(df2, df1, on = 'File:')
df_final.to_csv("csv/merged.csv" ,index=False)
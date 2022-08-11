import utils_2
import os
import sys
import cv2
import moviepy.editor

# script for cutting videos into shots

def _seconds(value, framerate):
     if isinstance(value, str):
        _zip_ft = zip((3600, 60, 1, 1/framerate), value.split(':'))
        return sum(f * float(t) for f,t in _zip_ft)

    
utils_2.make_dir("shots")
path = os.getcwd()

# configuration
new_path = os.path.join(path, "video_files")
vid_q = []
os.chdir(new_path)

for file in os.listdir():
    if file.endswith(".mp4"):
        vid_q.append(file)


# Create output dir
for video in vid_q:
    video_path = os.path.join(new_path, video)    
    video = cv2.VideoCapture(video_path)
    fps_from_vid = video.get(cv2.CAP_PROP_FPS)
    file_name = os.path.basename(os.path.normpath(video_path))
    file_name = file_name.replace(".mp4","")
    clip = moviepy.editor.VideoFileClip(video_path)
    # Gets a list of shots
    scene_list_out = utils_2.find_scenes(video_path)
    cut = 0
    # save shots
    for i in scene_list_out:
        out_clip = clip.subclip(_seconds(str(i[0]),fps_from_vid),_seconds(str(i[1]),fps_from_vid))
        new_v_path = os.path.join(path, "shots", file_name+"_"+str(cut)+".mp4")
        out_clip.write_videofile(new_v_path, fps=fps_from_vid,threads=8, codec="libx264")
        cut = cut + 1 
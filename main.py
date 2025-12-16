import os
import subprocess
import glob

frames_folder = "renders"
output_video = "output.mp4"
frame_rate = 24

png_files = sorted(glob.glob(os.path.join(frames_folder, "*.png")))

if not png_files:
    print("No PNG files found in the specified folder.")
    exit(1)

with open("file_list.txt", "w", encoding="utf-8") as f:
    for path in png_files:
        abs_path = os.path.abspath(path).replace("\\", "/")
        f.write(f"file '{abs_path}'\n")

cmd = [
    r"C:\ffmpeg\bin\ffmpeg.exe",
    "-y",
    "-r", str(frame_rate),
    "-f", "concat",
    "-safe", "0",
    "-i", "file_list.txt",
    "-vf", "fps=30,format=yuv420p",
    output_video
]

subprocess.run(cmd)
print(f" Video saved as {output_video} ")

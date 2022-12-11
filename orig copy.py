from moviepy.editor import *
outsrc = 'm3.mp4'


video1 = VideoFileClip('video8.mp4')
if video1.fps >22:
    video1.fps = 22
if video1.duration > 30:
    video1 = video1.subclip(0, 30)
width1 = video1.w
height1 = video1.h
if height1 == width1:
    height1 = width1
    clipresized = video1.resize(height=400, width=400)
elif height1 > width1:
    clipresized = video1.crop(
        y1=((video1.h-video1.w)/2), height=width1)
    print(clipresized.size)
    clipresized = clipresized.resize(width=400)
else:
    clipresized = video1.crop(
        x1=((video1.w-video1.h)/2), width=height1)
    clipresized = clipresized.resize(height=400)
    print('h < w')
final = CompositeVideoClip([clipresized])
watermark = (ImageClip('logo4.PNG').set_duration(final.duration).resize(height=400, width=final.w).set_position(('center', 'center')))

final = CompositeVideoClip([final, watermark])
final.write_videofile(outsrc,)

    

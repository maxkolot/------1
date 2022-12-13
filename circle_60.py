from moviepy.editor import *


def circle_60(src, outsrc, src1, sectext):

    video1 = VideoFileClip(src)
    if video1.fps > 60:
        video1.fps = 60
    if video1.duration > 60:
        video1 = video1.subclip(0, 60)
    width1 = video1.w
    height1 = video1.h
    if height1 == width1:
        height1 = width1
        clipresized = video1.resize(height=500, width=500)
    elif height1 > width1:
        clipresized = video1.crop(
            y1=((video1.h-video1.w)/2), height=width1)
        print(clipresized.size)
        clipresized = clipresized.resize(width=500)
    else:
        clipresized = video1.crop(
            x1=((video1.w-video1.h)/2), width=height1)
        clipresized = clipresized.resize(height=500)
        print('h < w')
    final = CompositeVideoClip([clipresized])
    watermark = (ImageClip('logo4.PNG').set_duration(final.duration).resize(height=500, width=final.w).set_position(('center', 'center')))
    audioclip = AudioFileClip(src1).subclip(
        sectext, (sectext + final.duration))
    final = final.set_audio(audioclip)
    final = CompositeVideoClip([final])
    final.write_videofile(outsrc)

    return final

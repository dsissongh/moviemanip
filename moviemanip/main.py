from moviepy.editor import *

def writeclip(filein, start, end, fileout):
	'''start and end are in seconds'''
	clip = VideoFileClip(file).subclip(start, end)
	clip.write_videofile(fileout)

#file = 'M20170105_201403.mp4'
file = 'M20170106_154802.mp4'
startseconds = 30
endseconds = 40
clip = 'test.mp4'

#writeclip(file, startseconds, endseconds, clip)


#write snip from a video file
clip = (VideoFileClip(file))
       #.subclip((1,22.65),(1,23.2))
        #
clip.write_gif("testclip.gif")
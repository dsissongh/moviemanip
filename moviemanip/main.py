from moviepy.editor import *

def writeclip(filein, start, end, fileout):
	'''start and end are in seconds'''
	clip = VideoFileClip(file).subclip(start, end)
	clip.write_videofile(fileout)

file = 'M20170105_201403.mp4'
start = 180+46
end = 240+37
clip = 'test.mp4'

writeclip(file, startseconds, endseconds, clip)
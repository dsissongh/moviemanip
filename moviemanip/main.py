from moviepy.editor import *
import subprocess


def writeclip(filein, start, end, fileout):
	'''start and end are in seconds'''
	clip = VideoFileClip(file).subclip(start, end)
	clip.write_videofile(fileout)


def sec2frames():
	file = 'M20170106_154802.mp4'
	ffexe = 'ffmpeg.exe'
	everyx = '3'
	args = (ffexe, "-i", file, "-vf", "fps="+everyx, "nail\\%03d.png")
	cmd = ffexe + " -i " + file + " -vf fps=1/" + everyx + " nail\\%03d.png"
	print(cmd)
	# extract a frame every x seconds - ffmpeg native instead
	subprocess.call(cmd, shell=True)



sec2frames()

exit()
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
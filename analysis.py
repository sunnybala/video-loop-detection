import pylab
import imageio
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time 
import pdb

def show_frame(frame):
	image = vid.get_data(frame)
	fig = pylab.figure()
	fig.suptitle('frame #{}'.format(frame), fontsize=20)
	pylab.imshow(image)
	pylab.show()

def compare_frames(frame1, frame2):
	fig = plt.figure()
	a=fig.add_subplot(1,2,1)
	img = vid.get_data(frame1)
	imgplot = plt.imshow(img)
	a.set_title('Frame #%s' % frame1)
	a=fig.add_subplot(1,2,2)
	img = vid.get_data(frame2)
	imgplot = plt.imshow(img)
	a.set_title('Frame #%s' % frame2)
	plt.show()

def diff_frames(frame1, frame2):
	f1 = vid.get_data(frame1)
	f2 = vid.get_data(frame2)
	return f1 - f2

def main(frames):
	filename = 'video.mp4'
	vid = imageio.get_reader(filename,  'ffmpeg')
	
	all_frames = vid.get_length()

	start = time.time()
	values = {}
	hash_counts = {}

	for x in range(frames):
		frame = vid.get_data(x)
		if x % 1000 == 0:
			print("frame count: ",x,"\t",round(x*1.0/all_frames,3)*100,'%')
		hashed = hash(frame.tostring())
		if values.get( hashed, None):
			compare_frames(hash_counts[hashed][0],x)
			hash_counts[hashed].append(x)
		else:
			values[hashed] = x
			hash_counts[hashed] = [x]

	print("Elapsed: ", time.time() - start,"seconds")
	return [hash_counts[x] for x in hash_counts if len(hash_counts[x]) > 1]
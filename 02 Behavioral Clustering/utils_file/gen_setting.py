
# all_video_names = [\
# 				   '1411_black_two','1929_black_two','0808_black_two','1410_black_two',\
# 				   '1115_black_two','1425_black_two','0856_black_two','1258_black_two',\
# 				   '1431_black_two','0923_black_two','1312_black_two','1929_black_two',\
# 				   '0941_black_two','1323_black_two','1959_black_two','0953_black_two',\
# 				   '1335_black_two','2009_black_two']


# print('imgdir:')
# for i in range(len(all_video_names)):
# 	v_name = all_video_names[i]
# 	print('\'/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0603/%s/pose_track_vis/\', # %d'%(v_name,i))

# print('tracked_json:')
# for i in range(len(all_video_names)):
# 	v_name = all_video_names[i]
# 	print('\'/disk4/zexin/ruihan/mice/datasets/20190603/%s/alphapose-results-forvis-tracked.json\', # %d'%(v_name,i))

# print('contdir:')
# for i in range(len(all_video_names)):
# 	v_name = all_video_names[i]
# 	print('\'/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0603/%s/contour/\', # %d'%(v_name,i))

# print('videodir:')
# for i in range(len(all_video_names)):
# 	v_name = all_video_names[i]
# 	print('\'/disk4/zexin/ruihan/mice/datasets/20190603/%s.mov\', # %d'%(v_name,i))


# all_video_names = [\
# 				   # '0902_black_two','0854_black_two','0910_black_two',
# 				   # '0913_black_two',\
# 				   # '1028_black_two',\
# 				   '2019-10-25_15-29-43_femalespost3hourisolation',
# 				   # '1138_black_two',
# 				   # '1030_black_two'
# 				   ]
# all_video_names = [\
# 					"2019-11-07_femaleandmalepost6hrisolation",\
# 					"2019-11-07_malemaleinteraction6hrpostisolation", \
# 					"2019-10-25_15-29-43_femalespost3hourisolation", \
# 					"2019-11-04_females4hrpostisolation",
# 				   ]
all_video_names = [\
					# '2019-10-25_15-29-43_femalespost3hourisolation',\
					# '2019-11-07_femaleandmalepost6hrisolation',\
					# '2019-11-04_females4hrpostisolation',\
					# '2019-11-07_malemaleinteraction6hrpostisolation',\
					'2019-11-19_2femalespost8hrisolation',\
				   ]

# video_clips_willUse = [
# 	[[0,300],[,] ]
# ]


print('        self.imgdir = [')
for i in range(len(all_video_names)):
	v_name = all_video_names[i]
	# print('            \'/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0605/%s/pose_track_vis/\', # %d'%(v_name,i))
	print('            \'/disk2/zexin/project/mice/clustering_sequencial/forZexin/cluster_results/%s/pose_track_vis/\', # %d'%(v_name,i))

print('            ]')

print('        self.tracked_json = [')
for i in range(len(all_video_names)):
	v_name = all_video_names[i]
	# print('            \'/disk1/zexin/project/mice/clustering_sequencial/track_result_folder/%s/alphapose-results-forvis-tracked.json\', # %d'%(v_name,i))
	# print('            \'/disk1/zexin/project/mice/clustering_sequencial/track_result_folder/withLimbs_interaction/%s/alphapose-results-forvis-tracked.json\', # %d'%(v_name,i))
	print('            \'/disk2/zexin/project/mice/track_result/insteraction/%s/alphapose-results-forvis-tracked.json\', # %d'%(v_name,i))
print('            ]')

print('        self.contdir = [')
for i in range(len(all_video_names)):
	v_name = all_video_names[i]
	# print('            \'/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0605/%s/contour/\', # %d'%(v_name,i))
	print('            \'/disk2/zexin/project/mice/clustering_sequencial/forZexin/cluster_results/%s/contour/\', # %d'%(v_name,i))
print('            ]')

print('        self.videodir = [')
for i in range(len(all_video_names)):
	v_name = all_video_names[i]
	# print('            \'/disk4/zexin/ruihan/mice/datasets/0605/%s.mov\', # %d'%(v_name,i))
	# print('            \'/disk4/zexin/project/mice/datasets/06_040506_twoMice/%s.mov\', # %d'%(v_name,i))
	# print('            \'/disk4/zexin/ruihan/mice/datasets/20191030_social/%s.mov\', # %d'%(v_name,i))
	# print('            \'/disk4/zexin/project/mice/datasets/interaction/%s.mp4\', # %d'%(v_name,i))
	print('            \'/disk2/zexin/data/mice/demo_videos/%s.mp4\', # %d'%(v_name,i))


print('            ]')
print('        self.intervals = [')
for i in range(len(all_video_names)):
	print('            [], # %d'%(i))
print('            ]')











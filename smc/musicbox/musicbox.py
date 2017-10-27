

class Musicbox:

	# track = {
	# 	'id': qwer,
	# 	'source': asdfasdf,
	# 	'start': asdfasdf,
	# 	'end': asdfasdf,
	# 	'numloops': asdfasdf,
	# 	'volume': asdfas,
	# 	'effects': [fadein,fadeout]
	# }
	
	def __init__(self):
		print('Im a musicbox')
		
	def __len__(self):
		pass # return whole duration

	def __str__(self):
		# 
		pass

	def addTrack(self, audio, numLoops, soundlevel, startoffset, fade):
		"""
		Returns
		track number, duration, starttime, endtime
		"""


	def getMusic(self, range):
		"""
		Returns
		one audio object of all tracks combined
		"""
		pass


	def getTrack(self, trackid):
		"""
		Returns
		audio object for given track
		or track object
		"""
		pass

	
	def shift(self, trackids, timeunit, amount):
		"""
		Shift tracks within the timeline

		trackids: a list of track ids to be modified
		timeunit: 4:4 time, seconds, loop, ...
		amount: the amount to be shifted, as per the timeunit. positive / negative to determine direction
		
		shift([1,2], musicbox.loop, 4)
		would shift tracks 1 and 2 by their respective loop length * 4

		Returns
		None		
		"""
		pass

	
	def removeTracks(self, trackids):
		pass


	def align(track1, track2, alignPoint):
		"""
		aligns track1's start/end to track2's start/end
		align(3, 2, musicbox.start) or 'start'?

		alignPoint: start or end of track2		

		Returns
		None
		"""
		pass

	# ideas:
	# musicbox[id] gives track object
	# musicbox[trackid].volume(50%)
	# musixbox[trackid].trim(front=1loop, back=2sec)
	# musicbox.trim
	# musicbox.volume


from copy import deepcopy

PYTHAGOREAN = {"m2":256/243, "M2":9/8, "m3":32/27, "M3": 81/64, "P4": 4/3, "+4": 729/512, "*5": 1024/729, "P5": 3/2, "m6": 128/81, "M6": 27/16, "m7": 16/9, "M7": 243/128, "P8": 2}

def get_interval(w, interval):
	ret = deepcopy(w)
	ret.freq *= interval
	return ret

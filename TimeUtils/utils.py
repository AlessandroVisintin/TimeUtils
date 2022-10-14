import datetime
from numbers import Number


def now_iso8601(utc:bool=True, micro:bool=False) -> str:
	"""
	
	Print current UTC time in ISO-8601 standard.
	
	Args :
		utc : whether to use UTC time or local time. Defaults to True.
		micro : wheter to print with microsecond precision.
			Defaults to False.
	
	Returns :
		formatted string.

	"""
	
	now = None
	if utc:
		now = datetime.datetime.utcnow()
	else:
		now = datetime.datetime.now()
	
	if micro:
		return now.isoformat()
	return now.replace(microsecond=0).isoformat()


def stamp2str(stamp:Number, form:str='%Y-%m-%d %H:%M:%S') -> str:
	"""
	
	Convert timestamp to formatted UTC string.
	
	Args : 
		stamp : timestamp to convert.
		form : formatting string.
	
	Returns : 
		formatted string.
	
	"""
	
	return datetime.datetime.utcfromtimestamp(stamp).strftime(form)


def str2stamp(string, form='%Y-%m-%d %H:%M:%S') -> Number:
	"""
	
	Convert time string to UTC timestamp.
	
	Args : 
		string : string to convert.
		form : formatting string.

	
	"""
	
	utc = datetime.timezone.utc
	return datetime.datetime.strptime(string, form).replace(tzinfo=utc).timestamp()
	
# 	no_aware = datetime.datetime.strptime(string, form)
# 	return pytz.utc.localize(no_aware).timestamp()
from TimeUtils.utils import now_iso8601
from TimeUtils.utils import str2stamp
from TimeUtils.utils import stamp2str


# print current UTC time.
print('Current UTC: ', now_iso8601())

# convert time string
DATE = '2022-10-14 08:00:00'
converted = str2stamp(DATE)
print('Time string to timestamp: ', DATE, ' -> ', converted)

# converting back
print('Converting back: ', stamp2str(converted))

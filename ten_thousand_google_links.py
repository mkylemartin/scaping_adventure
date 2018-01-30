import requests as r
import re
import time
import random

year_range = range(2014, 2017)
month_range = range(1, 13)
weeks = [(1, 7), (8, 14), (15, 21), (22, 28)]

# for week in weeks:
#     print('week ' + str(week) + ' start: ' + str(week[0]) + ' end: ' + str(week[1]))

def get_links(month_range, weeks):
    """
    pass in month and day to write a query that will
    go get all the links on that google search page.
    """

    links = []
    for year in year_range:
        for month in month_range:
            for week in weeks:
                # append to a search_str list
                link_a = 'https://www.google.com/search?q=de&num=100&lr=lang_fr&tbs=cdr:1,cd_min:'
                link_b = str(month) + '/' + str(week[0]) + '/' + str(year) + ',cd_max:' + str(month) + '/' + str(week[1])
                link_c = '/' + str(year) + ',sbd:1&tbm=nws&cr=countryFR'
                link = link_a + link_b + link_c
                links += [link, ]
                print(len(links))
    return links

query_list = get_links(month_range, weeks)


# finder_re = r'<a class="l _PMs" href="(.*?)"'

index = 1
for url in query_list[:3]:
	response = r.get(url)
	with open('search_no_' + str(index) + '.txt', 'w+') as f:
			f.write(response.text)
			print('wrote file no. ' + str(index))
			time.sleep(5)
	index += 1
print('done!')

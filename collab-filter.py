import csv
import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff
    if (math.sqrt(xdiff2 * ydiff2)) == 0:
    	return 0
    return diffprod / math.sqrt(xdiff2 * ydiff2)

rating_list_of_lists = list(csv.reader(open('movie-ratings.csv', 'r')))

person = input('Please enter your name: ')
rate_list = list(csv.reader(open('user_preference.csv', 'r')))

names = [];
for x in rating_list_of_lists[1:]:
	names += [x[0]];
dist = [];
for x in rating_list_of_lists[1:]:
	d = 0;
	i = 0;
	me = []
	celebrity = []
	for y in x[1:]:
		if (float(y) != -1 and float(rate_list[1][i]) != -1):
			me.append(float(y))
			celebrity.append(float(rate_list[1][i]))
		i+=1;
	d = pearson_def(me, celebrity)
	dist += [d];
zipped = list(zip(names,dist));
zipped.sort(key = lambda l: l[1]);
print(zipped);
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

rate_list = list(csv.reader(open('user_preference.csv', 'r')))

names = [];
for x in rating_list_of_lists[1:]:
	names += [x[0]];
dist = [];
dtot = [None]*len(rate_list[0]);
for x in range(0,len(rate_list[0])):
    dtot[x] = 0;
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
    d = pearson_def(me, celebrity)/2+0.5;
    k = 0;
    dist += [d];
# print(dist);
for i in dist:
    i = float(i);
for i in rate_list[1]:
    i = float(i);
# print(dist);
zipped = list(zip(names,dist));
j=0;
ratings=[None]*len(rate_list[0]);
for x in range(0,len(rate_list[0])):
    ratings[x] = 0;

# print(ratings[2]);
for x in rating_list_of_lists[1:]:
    k = 1;
    rat = 0;
    for y in x[1:]:
        y = float(y) ;
        # print (y);
        if(y != -1):
            y = y * dist[j];
            x[k] = y;
            ratings[k-1] += y;
            dtot[k-1] += dist[j];
            # print(x);
        k+=1; 
            
    #print(x);
    rating_list_of_lists[j+1] = x;
    # print(j);
    j+=1;
# print(rate_list[1]);

for x in range(0,len(rate_list[0])):
    ratings[x] /= dtot[x];
# print(ratings);
j=0;
z = list(zip(ratings,rate_list[0]));
z.sort(key = lambda l: l[0]);

no = 0;
l = len(z);
m = 0;
while m < l and no <3:
    current = z[l-m-1][1];
    n = 0;
    while rate_list[0][n] != current :
        n+=1;
    if(rate_list[1][n] == '-1'):
        print(current);
        no += 1;
    m += 1;
    
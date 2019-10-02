>>> import pandas as pd
>>> df = pd.read_csv("data/Salaries.csv")
>>> df.head()
   rank discipline  phd  service   sex  salary
0  Prof          B   56       49  Male  186960
1  Prof          A   12        6  Male   93000
2  Prof          A   23       20  Male  110515
3  Prof          A   40       31  Male  131205
4  Prof          B   20       18  Male  104800
>>> df.head(10)
        rank discipline  phd  service   sex  salary
0       Prof          B   56       49  Male  186960
1       Prof          A   12        6  Male   93000
2       Prof          A   23       20  Male  110515
3       Prof          A   40       31  Male  131205
4       Prof          B   20       18  Male  104800
5       Prof          A   20       20  Male  122400
6  AssocProf          A   20       17  Male   81285
7       Prof          A   18       18  Male  126300
8       Prof          A   29       19  Male   94350
9       Prof          A   51       51  Male   57800
>>> df.head(20)
         rank discipline  phd  service   sex  salary
0        Prof          B   56       49  Male  186960
1        Prof          A   12        6  Male   93000
2        Prof          A   23       20  Male  110515
3        Prof          A   40       31  Male  131205
4        Prof          B   20       18  Male  104800
5        Prof          A   20       20  Male  122400
6   AssocProf          A   20       17  Male   81285
7        Prof          A   18       18  Male  126300
8        Prof          A   29       19  Male   94350
9        Prof          A   51       51  Male   57800
10       Prof          B   39       33  Male  128250
11       Prof          B   23       23  Male  134778
12   AsstProf          B    1        0  Male   88000
13       Prof          B   35       33  Male  162200
14       Prof          B   25       19  Male  153750
15       Prof          B   17        3  Male  150480
16   AsstProf          B    8        3  Male   75044
17   AsstProf          B    4        0  Male   92000
18       Prof          A   19        7  Male  107300
19       Prof          A   29       27  Male  150500
>>> df.head(50)
         rank discipline  phd  service     sex  salary
0        Prof          B   56       49    Male  186960
1        Prof          A   12        6    Male   93000
2        Prof          A   23       20    Male  110515
3        Prof          A   40       31    Male  131205
4        Prof          B   20       18    Male  104800
5        Prof          A   20       20    Male  122400
6   AssocProf          A   20       17    Male   81285
7        Prof          A   18       18    Male  126300
8        Prof          A   29       19    Male   94350
9        Prof          A   51       51    Male   57800
10       Prof          B   39       33    Male  128250
11       Prof          B   23       23    Male  134778
12   AsstProf          B    1        0    Male   88000
13       Prof          B   35       33    Male  162200
14       Prof          B   25       19    Male  153750
15       Prof          B   17        3    Male  150480
16   AsstProf          B    8        3    Male   75044
17   AsstProf          B    4        0    Male   92000
18       Prof          A   19        7    Male  107300
19       Prof          A   29       27    Male  150500
20   AsstProf          B    4        4    Male   92000
21       Prof          A   33       30    Male  103106
22   AsstProf          A    4        2    Male   73000
23   AsstProf          A    2        0    Male   85000
24       Prof          A   30       23    Male   91100
25       Prof          B   35       31    Male   99418
26       Prof          A   38       19    Male  148750
27       Prof          A   45       43    Male  155865
28   AsstProf          B    7        2    Male   91300
29       Prof          B   21       20    Male  123683
30  AssocProf          B    9        7    Male  107008
31       Prof          B   22       21    Male  155750
32       Prof          A   27       19    Male  103275
33       Prof          B   18       18    Male  120000
34  AssocProf          B   12        8    Male  119800
35       Prof          B   28       23    Male  126933
36       Prof          B   45       45    Male  146856
37       Prof          A   20        8    Male  102000
38   AsstProf          B    4        3    Male   91000
39       Prof          B   18       18  Female  129000
40       Prof          A   39       36  Female  137000
41  AssocProf          A   13        8  Female   74830
42   AsstProf          B    4        2  Female   80225
43   AsstProf          B    5        0  Female   77000
44       Prof          B   23       19  Female  151768
45       Prof          B   25       25  Female  140096
46   AsstProf          B   11        3  Female   74692
47  AssocProf          B   11       11  Female  103613
48       Prof          B   17       17  Female  111512
49       Prof          B   17       18  Female  122960
>>> df.tail()
         rank discipline  phd  service     sex  salary
73       Prof          B   18       10  Female  105450
74  AssocProf          B   19        6  Female  104542
75       Prof          B   17       17  Female  124312
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646

>>> df['salary'].dtype
dtype('int64')
>>> df.dtypes
rank          object
discipline    object
phd            int64
service        int64
sex           object
salary         int64
dtype: object
>>> df.ndim()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> df.ndim
2
>>> df.size
468
>>> df.axes
[RangeIndex(start=0, stop=78, step=1), Index(['rank', 'discipline', 'phd', 'service', 'sex', 'salary'], dtype='object')]

>>> df.describe()
             phd    service         salary
count  78.000000  78.000000      78.000000
mean   19.705128  15.051282  108023.782051
std    12.498425  12.139768   28293.661022
min     1.000000   0.000000   57800.000000
25%    10.250000   5.250000   88612.500000
50%    18.500000  14.500000  104671.000000
75%    27.750000  20.750000  126774.750000
max    56.000000  51.000000  186960.000000
>>> df.std()
phd           12.498425
service       12.139768
salary     28293.661022
dtype: float64
>>> a = df.head(50)
>>> a.mean()
phd            21.52
service        17.60
salary     113789.14
dtype: float64


>>> df['sex']
0       Male
1       Male
2       Male
3       Male
4       Male
       ...
73    Female
74    Female
75    Female
76    Female
77    Female
Name: sex, Length: 78, dtype: object
>>> df.sex
0       Male
1       Male
2       Male
3       Male
4       Male
       ...
73    Female
74    Female
75    Female
76    Female
77    Female
Name: sex, Length: 78, dtype: object


>>> df.salary.describe()
count        78.000000
mean     108023.782051
std       28293.661022
min       57800.000000
25%       88612.500000
50%      104671.000000
75%      126774.750000
max      186960.000000
Name: salary, dtype: float64
>>> df.salary.count()
78
>>> df.salary.mean()
108023.78205128205


>>> df_rank = df.groupby(['rank'])
>>> df_rank.mean()
                 phd    service         salary
rank
AssocProf  15.076923  11.307692   91786.230769
AsstProf    5.052632   2.210526   81362.789474
Prof       27.065217  21.413043  123624.804348

>>> df.groupby('rank')[['salary']].mean()
                  salary
rank
AssocProf   91786.230769
AsstProf    81362.789474
Prof       123624.804348

>>> df.groupby(['rank'], sort = False)[['salary']].mean()
                  salary
rank
Prof       123624.804348
AssocProf   91786.230769
AsstProf    81362.789474


>>> df_sub = df[df['salary'] > 120000]
>>> df_sub
    rank discipline  phd  service     sex  salary
0   Prof          B   56       49    Male  186960
3   Prof          A   40       31    Male  131205
5   Prof          A   20       20    Male  122400
7   Prof          A   18       18    Male  126300
10  Prof          B   39       33    Male  128250
11  Prof          B   23       23    Male  134778
13  Prof          B   35       33    Male  162200
14  Prof          B   25       19    Male  153750
15  Prof          B   17        3    Male  150480
19  Prof          A   29       27    Male  150500
26  Prof          A   38       19    Male  148750
27  Prof          A   45       43    Male  155865
29  Prof          B   21       20    Male  123683
31  Prof          B   22       21    Male  155750
35  Prof          B   28       23    Male  126933
36  Prof          B   45       45    Male  146856
39  Prof          B   18       18  Female  129000
40  Prof          A   39       36  Female  137000
44  Prof          B   23       19  Female  151768
45  Prof          B   25       25  Female  140096
49  Prof          B   17       18  Female  122960
51  Prof          B   20       14  Female  127512
58  Prof          B   36       26  Female  144651
72  Prof          B   24       15  Female  161101
75  Prof          B   17       17  Female  124312



>>> df_f = df[df['sex'] == 'Female']
>>> df_f
         rank discipline  phd  service     sex  salary
39       Prof          B   18       18  Female  129000
40       Prof          A   39       36  Female  137000
41  AssocProf          A   13        8  Female   74830
42   AsstProf          B    4        2  Female   80225
43   AsstProf          B    5        0  Female   77000
44       Prof          B   23       19  Female  151768
45       Prof          B   25       25  Female  140096
46   AsstProf          B   11        3  Female   74692
47  AssocProf          B   11       11  Female  103613
48       Prof          B   17       17  Female  111512
49       Prof          B   17       18  Female  122960
50   AsstProf          B   10        5  Female   97032
51       Prof          B   20       14  Female  127512
52       Prof          A   12        0  Female  105000
53   AsstProf          A    5        3  Female   73500
54  AssocProf          A   25       22  Female   62884
55   AsstProf          A    2        0  Female   72500
56  AssocProf          A   10        8  Female   77500
57   AsstProf          A    3        1  Female   72500
58       Prof          B   36       26  Female  144651
59  AssocProf          B   12       10  Female  103994
60   AsstProf          B    3        3  Female   92000
61  AssocProf          B   13       10  Female  103750
62  AssocProf          B   14        7  Female  109650
63       Prof          A   29       27  Female   91000
64  AssocProf          A   26       24  Female   73300
65       Prof          A   36       19  Female  117555
66   AsstProf          A    7        6  Female   63100
67       Prof          A   17       11  Female   90450
68   AsstProf          A    4        2  Female   77500
69       Prof          A   28        7  Female  116450
70   AsstProf          A    8        3  Female   78500
71  AssocProf          B   12        9  Female   71065
72       Prof          B   24       15  Female  161101
73       Prof          B   18       10  Female  105450
74  AssocProf          B   19        6  Female  104542
75       Prof          B   17       17  Female  124312
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646


>>> df["salary"]
0     186960
1      93000
2     110515
3     131205
4     104800
       ...
73    105450
74    104542
75    124312
76    109954
77    109646
Name: salary, Length: 78, dtype: int64
>>> df[["rank", "salary"]]
         rank  salary
0        Prof  186960
1        Prof   93000
2        Prof  110515
3        Prof  131205
4        Prof  104800
..        ...     ...
73       Prof  105450
74  AssocProf  104542
75       Prof  124312
76       Prof  109954
77       Prof  109646


>>> df_sub.loc[10:20, ['rank', 'sex', 'salary']]
    rank   sex  salary
10  Prof  Male  128250
11  Prof  Male  134778
13  Prof  Male  162200
14  Prof  Male  153750
15  Prof  Male  150480
19  Prof  Male  150500


>>> df_sorted = df.sort_values(by = "service")
>>> df_sorted.head()
        rank discipline  phd  service     sex  salary
55  AsstProf          A    2        0  Female   72500
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
>>> df_sorted
        rank discipline  phd  service     sex  salary
55  AsstProf          A    2        0  Female   72500
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
..       ...        ...  ...      ...     ...     ...
40      Prof          A   39       36  Female  137000
27      Prof          A   45       43    Male  155865
36      Prof          B   45       45    Male  146856
0       Prof          B   56       49    Male  186960
9       Prof          A   51       51    Male   57800


>>> df_sorted = df.sort_values(by = ['service', 'salary'], ascending = [True, False])
>>> df_sorted
        rank discipline  phd  service     sex  salary
52      Prof          A   12        0  Female  105000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
..       ...        ...  ...      ...     ...     ...
40      Prof          A   39       36  Female  137000
27      Prof          A   45       43    Male  155865
36      Prof          B   45       45    Male  146856
0       Prof          B   56       49    Male  186960
9       Prof          A   51       51    Male   57800

[78 rows x 6 columns]
>>> df_sorted.head(10)
        rank discipline  phd  service     sex  salary
52      Prof          A   12        0  Female  105000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
55  AsstProf          A    2        0  Female   72500
57  AsstProf          A    3        1  Female   72500
28  AsstProf          B    7        2    Male   91300
42  AsstProf          B    4        2  Female   80225
68  AsstProf          A    4        2  Female   77500




>>> df_mean = df[df['discipline'] == "A"]
>>> df_mean
         rank discipline  phd  service     sex  salary
1        Prof          A   12        6    Male   93000
2        Prof          A   23       20    Male  110515
3        Prof          A   40       31    Male  131205
5        Prof          A   20       20    Male  122400
6   AssocProf          A   20       17    Male   81285
7        Prof          A   18       18    Male  126300
8        Prof          A   29       19    Male   94350
9        Prof          A   51       51    Male   57800
18       Prof          A   19        7    Male  107300
19       Prof          A   29       27    Male  150500
21       Prof          A   33       30    Male  103106
22   AsstProf          A    4        2    Male   73000
23   AsstProf          A    2        0    Male   85000
24       Prof          A   30       23    Male   91100
26       Prof          A   38       19    Male  148750
27       Prof          A   45       43    Male  155865
32       Prof          A   27       19    Male  103275
37       Prof          A   20        8    Male  102000
40       Prof          A   39       36  Female  137000
41  AssocProf          A   13        8  Female   74830
52       Prof          A   12        0  Female  105000
53   AsstProf          A    5        3  Female   73500
54  AssocProf          A   25       22  Female   62884
55   AsstProf          A    2        0  Female   72500
56  AssocProf          A   10        8  Female   77500
57   AsstProf          A    3        1  Female   72500
63       Prof          A   29       27  Female   91000
64  AssocProf          A   26       24  Female   73300
65       Prof          A   36       19  Female  117555
66   AsstProf          A    7        6  Female   63100
67       Prof          A   17       11  Female   90450
68   AsstProf          A    4        2  Female   77500
69       Prof          A   28        7  Female  116450
70   AsstProf          A    8        3  Female   78500
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646
>>> df_mean.mean()
phd           21.527778
service       15.722222
salary     98331.111111


>>> df_sal = df[df["salary"] > 100000]
>>> df_sal
         rank discipline  phd  service     sex  salary
0        Prof          B   56       49    Male  186960
2        Prof          A   23       20    Male  110515
3        Prof          A   40       31    Male  131205
4        Prof          B   20       18    Male  104800
5        Prof          A   20       20    Male  122400
7        Prof          A   18       18    Male  126300
10       Prof          B   39       33    Male  128250
11       Prof          B   23       23    Male  134778
13       Prof          B   35       33    Male  162200
14       Prof          B   25       19    Male  153750
15       Prof          B   17        3    Male  150480
18       Prof          A   19        7    Male  107300
19       Prof          A   29       27    Male  150500
21       Prof          A   33       30    Male  103106
26       Prof          A   38       19    Male  148750
27       Prof          A   45       43    Male  155865
29       Prof          B   21       20    Male  123683
30  AssocProf          B    9        7    Male  107008
31       Prof          B   22       21    Male  155750
32       Prof          A   27       19    Male  103275
33       Prof          B   18       18    Male  120000
34  AssocProf          B   12        8    Male  119800
35       Prof          B   28       23    Male  126933
36       Prof          B   45       45    Male  146856
37       Prof          A   20        8    Male  102000
39       Prof          B   18       18  Female  129000
40       Prof          A   39       36  Female  137000
44       Prof          B   23       19  Female  151768
45       Prof          B   25       25  Female  140096
47  AssocProf          B   11       11  Female  103613
48       Prof          B   17       17  Female  111512
49       Prof          B   17       18  Female  122960
51       Prof          B   20       14  Female  127512
52       Prof          A   12        0  Female  105000
58       Prof          B   36       26  Female  144651
59  AssocProf          B   12       10  Female  103994
61  AssocProf          B   13       10  Female  103750
62  AssocProf          B   14        7  Female  109650
65       Prof          A   36       19  Female  117555
69       Prof          A   28        7  Female  116450
72       Prof          B   24       15  Female  161101
73       Prof          B   18       10  Female  105450
74  AssocProf          B   19        6  Female  104542
75       Prof          B   17       17  Female  124312
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646

>>> df_sal_f = df_sal[df["sex"] == 'Female']
>>> df_sal_f
         rank discipline  phd  service     sex  salary
39       Prof          B   18       18  Female  129000
40       Prof          A   39       36  Female  137000
44       Prof          B   23       19  Female  151768
45       Prof          B   25       25  Female  140096
47  AssocProf          B   11       11  Female  103613
48       Prof          B   17       17  Female  111512
49       Prof          B   17       18  Female  122960
51       Prof          B   20       14  Female  127512
52       Prof          A   12        0  Female  105000
58       Prof          B   36       26  Female  144651
59  AssocProf          B   12       10  Female  103994
61  AssocProf          B   13       10  Female  103750
62  AssocProf          B   14        7  Female  109650
65       Prof          A   36       19  Female  117555
69       Prof          A   28        7  Female  116450
72       Prof          B   24       15  Female  161101
73       Prof          B   18       10  Female  105450
74  AssocProf          B   19        6  Female  104542
75       Prof          B   17       17  Female  124312
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646


>>> df_sal_m = df_sal[df["sex"] == 'Male']
>>> df_sal_m
         rank discipline  phd  service   sex  salary
0        Prof          B   56       49  Male  186960
2        Prof          A   23       20  Male  110515
3        Prof          A   40       31  Male  131205
4        Prof          B   20       18  Male  104800
5        Prof          A   20       20  Male  122400
7        Prof          A   18       18  Male  126300
10       Prof          B   39       33  Male  128250
11       Prof          B   23       23  Male  134778
13       Prof          B   35       33  Male  162200
14       Prof          B   25       19  Male  153750
15       Prof          B   17        3  Male  150480
18       Prof          A   19        7  Male  107300
19       Prof          A   29       27  Male  150500
21       Prof          A   33       30  Male  103106
26       Prof          A   38       19  Male  148750
27       Prof          A   45       43  Male  155865
29       Prof          B   21       20  Male  123683
30  AssocProf          B    9        7  Male  107008
31       Prof          B   22       21  Male  155750
32       Prof          A   27       19  Male  103275
33       Prof          B   18       18  Male  120000
34  AssocProf          B   12        8  Male  119800
35       Prof          B   28       23  Male  126933
36       Prof          B   45       45  Male  146856
37       Prof          A   20        8  Male  102000



>>> df_sorted = df.sort_values(by = "service")
>>> df_sorted
        rank discipline  phd  service     sex  salary
55  AsstProf          A    2        0  Female   72500
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
..       ...        ...  ...      ...     ...     ...
40      Prof          A   39       36  Female  137000
27      Prof          A   45       43    Male  155865
36      Prof          B   45       45    Male  146856
0       Prof          B   56       49    Male  186960
9       Prof          A   51       51    Male   57800



>>> df = pd.read_csv("data/flights.csv")
>>> df.head()
   year  month  day  dep_time  dep_delay  arr_time  arr_delay carrier tailnum  flight origin dest  air_time  distance  hour  minute
0  2013      1    1     517.0        2.0     830.0       11.0      UA  N14228    1545    EWR  IAH     227.0      1400   5.0    17.0
1  2013      1    1     533.0        4.0     850.0       20.0      UA  N24211    1714    LGA  IAH     227.0      1416   5.0    33.0
2  2013      1    1     542.0        2.0     923.0       33.0      AA  N619AA    1141    JFK  MIA     160.0      1089   5.0    42.0
3  2013      1    1     554.0       -6.0     812.0      -25.0      DL  N668DN     461    LGA  ATL     116.0       762   5.0    54.0
4  2013      1    1     554.0       -4.0     740.0       12.0      UA  N39463    1696    EWR  ORD     150.0       719   5.0    54.0


>>> df.isnull()
         year  month    day  dep_time  dep_delay  arr_time  arr_delay  carrier  tailnum  flight  origin   dest  air_time  distance   hour  minute
0       False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
1       False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
2       False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
3       False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
4       False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
...       ...    ...    ...       ...        ...       ...        ...      ...      ...     ...     ...    ...       ...       ...    ...     ...
160749  False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
160750  False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
160751  False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
160752  False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False
160753  False  False  False     False      False     False      False    False    False   False   False  False     False     False  False   False

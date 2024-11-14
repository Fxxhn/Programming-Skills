Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Counting up from 0 to 50:")
Counting up from 0 to 50:
for i in range(0, 51):  # 51 is exclusive, so it counts up to 50
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
print("\nCounting down from 50 to 0:")

Counting down from 50 to 0:

for i in range(50, -1, -1):  # -1 is the step, so it decrements
    print(i)

    
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
print("\nCounting up from 30 to 50:")

Counting up from 30 to 50:
for i in range(30, 51):  # 51 is exclusive
    print(i)

    
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
print("\nCounting down from 50 to 10 in decrements of 2:")

Counting down from 50 to 10 in decrements of 2:
for i in range(50, 9, -2):  # 9 is exclusive, so it counts down to 10
    print(i)

    
50
48
46
44
42
40
38
36
34
32
30
28
26
24
22
20
18
16
14
12
10


20
20
print("\nCounting up from 100 to 200 in increments of 5:")

Counting up from 100 to 200 in increments of 5:
for i in range(100, 201, 5):  # 201 is exclusive
    print(i)

    
100
105
110
115
120
125
130
135
140
145
150
155
160
165
170
175
180
185
190
195
200
>>> for i in range(100, 201, 5):  # 201 is exclusive
...     print(i)
... 
...     
100
105
110
115
120
125
130
135
140
145
150
155
160
165
170
175
180
185
190
195
200

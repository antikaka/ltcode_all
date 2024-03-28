
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""

# s = "PAYPALISHIRING"
# numRows = 3
#
# ss = {
#     1:"",
#     2:"",
#     3:"",
#     4:"",
#     5:""
# }
# count = 0
# check = False
# halfcheck = True
# halfrow = numRows - 2
# halfrowcount = numRows - halfrow
# numcheck = numRows
# for num in range(len(s)):
#     if check == True and check != halfcheck:
#         count = halfrow
#         numcheck = halfrowcount
#     elif check == True and check == halfcheck:
#         count = 0
#         numcheck = numRows
#         check = False
#
#     count += 1
#     if count == 1:
#         ss[1] += s[num]
#         if count == numcheck:
#             check = True
#     if count == 2:
#         ss[2] += s[num]
#         if count == numcheck:
#             check = True
#     if count == 3:
#         ss[3] += s[num]
#         if count == numcheck:
#             check = True
#     if count == 4:
#         ss[4] += s[num]
#         if count == numcheck:
#             check = True
#     if count == 5:
#         ss[5] += s[num]
#         if count == numcheck:
#             check = True
#
# print(ss)

s = "PAYPALISHIRING"
numRows = 4
count = 0
step = 1
text = ""
ss = [[] for _ in range(numRows)]
# if len(s) == numRows:
#     return s
for char in s:
    if count == numRows:
        step = -1
    if count == 1:
        step = 1
    count += step
    ss[count - 1] += char
    print(ss, char, count)
for num in range(len(ss)):
    ss[num] = "".join(ss[num])
print("".join(ss))


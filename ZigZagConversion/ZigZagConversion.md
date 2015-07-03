# [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

---

## Description

---

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

---

比较简单的字符串编码题，将按照“Z”字形排列的字符串按行转换。通过对字符串的分析可以得到以下几点规律：

> * 每一竖列同一位置的字符之间相差的距离是2*rowNumber - 2
> * 每一竖列的字符与其同一行的斜列字符之间相差的距离是2*i，i代表当前行下标
> * 只有第一行和最后一行有斜列的字符
> * 当rowNumber=1、字符长度小于或等于rowNumber时可以直接返回原字符串

代码实现：[ZigZag Conversion](./ZigZagConversion.py)
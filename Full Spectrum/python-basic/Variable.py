"""
int : Integers
float : Decimal
string : Alphabet
"""

number = 1 #2 3 4 ...
name = 'Sirawit' # You can use double quot("") to make string
deci = 5.8 #float variable

print(12) #12

# Operator
"""
**
*
//
/
%
+
-
"""

print(1+2) # 3
print('1' + '2') # 12

print(5**2*8/2//3+7-5%4) # 39.0

# Example

"""
จงเขียนโปรแกรมเพื่อคำนวณหาเส้นรอบวงของสี่เหลี่ยมผืนผ้า โดยโปรแกรมจะรับ Input เป็นความกว้าง w และความสูง h ตามลำดับ

ตัวอย่างที่ 1:

Input: w=10 และ h=5

10
5
Expected output: หลังจากได้รับขนาดของสี่เหลี่ยมผืนผ้าแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น

Perimeter: 30.0
ตัวอย่างที่ 2:

Input: w=1 และ h=2

1.5
2
Expected output: หลังจากได้รับขนาดของสี่เหลี่ยมผืนผ้าแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น

Perimeter: 7.0
"""

# Solution

w = float(input())
h = float(input())

print("Parimeter:", (w + h) * 2)

"""
จงเขียนโปรแกรมเพื่อคำนวณหาจำนวนชั่วโมงและจำนวนนาที โดยมีการรับ Input เป็นจำนวนนาที และโปรแกรมจะแสดงผลลัพธ์ในรูปแบบ hh:mm (จำนวนชั่วโมง:จำนวนนาที)

ตัวอย่างที่ 1:

Input: จำนวนนาที 15 นาที

15
Expected output: หลังจากคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น hh:mm

0:15
ตัวอย่างที่ 2:

Input: จำนวนนาที 180 นาที

180
Expected output: หลังจากคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น hh:mm

3:0
ตัวอย่างที่ 3:

Input: จำนวนนาที 3659 นาที

3659
Expected output: หลังจากคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น hh:mm

60:59
"""
# Solution

mins = int(input())
mm = mins%60
hh = mins//60
print(f"{hh}:{mm}")
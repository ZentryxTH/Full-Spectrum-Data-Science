'''
if, else, elif
'''

# Example

"""
จงเขียนโปรแกรมเพื่อคำนวณราคาชานมไข่มุก โดยรับ input ดังนี้

เป็นสมาชิกหรือไม่ (member)มีค่าเป็น 'Y' หรือ 'N'
ขนาดของชานมไข่มุก (size)มีค่าเป็น 'M' หรือ 'L'
ใส่ topping ไข่มุกหรือไม่ (topping) มีค่าเป็น 'Y' หรือ 'N'
โดยราคาชานมไข่มุกแก้ว 'M' จะมีราคาที่ 50 บาท หากเป็น 'L' ต้องเพิ่ม 10 บาท ราคานี้เป็นราคารวม topping หากไม่ต้องการใส่ topping จะได้รับส่วนลด 10 บาท และหากเป็นสมาชิกจะได้รับส่วนลดจากราคารวม 10%

เมื่อโปรแกรมรับ input ทั้งหมดแล้ว หลังจากคำนวณ โปรแกรมจะแสดงผลลัพธ์ราคาสุทธิ

หมายเหตุ: นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input ตามตัวอักษรที่กำหนดไว้เท่านั้น ไม่มีตัวอักษรอื่นหรือตัวเลข

ตัวอย่างที่ 1:

Input: member='Y', size='M', และ topping='N' โดยโปรแกรมจะถาม member, size และ topping ตามลำดับ

Y
M
N
Expected output: หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น

Total price: 36.0
ตัวอย่างที่ 2:

Input: member='N', size='L', และ topping='Y' โดยโปรแกรมจะถาม member, size และ topping ตามลำดับ

N
L
Y
Expected output: หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น

Total price: 60.0
ตัวอย่างที่ 3:

Input: member='Y', size='L', และ topping='Y' โดยโปรแกรมจะถาม member, size และ topping ตามลำดับ

Y
L
Y
Expected output: หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น

Total price: 54.0
"""

# Solution

member = input()
size = input()
topping = input()
price = 0

if size == 'M':
  price = 40
elif size == 'L':
  price = 50
elif size == 'XL' :
  price = 60
else :
  print("Wrong type")

if topping == 'Y' :
  price += 10
elif topping == 'N':
  price = price
else :
  print("Wrong type")

if member == 'Y':
  price *= 0.9
else :
  print("Wrong type")

print(f"Total price: {price}")

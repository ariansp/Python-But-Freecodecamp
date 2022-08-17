done = True
#Every string will be True except 0 and ""(empty)
if done:
  print("Yes!")
else:
  print("No!")

print("""LOOK BELOW DUDE!
==============
BELOW!!!!""")
book_1_read = False
book_2_read = True
#The output is True coz it need only one true
read_any_book = any([book_1_read, book_2_read])
print(read_any_book)
#"All" meaning is, need the same bool to output a True
read_any_book = all([book_1_read, book_2_read])
print(read_any_book)
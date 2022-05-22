from arithmetic_arranger import arranger

#list for determining proper function
lst1 = ["234 + 8348","2342 - 2834"]

#list for testing upto the number of list items
lst2 = ["3453 + 45", "5677 + 29", "905 + 667", "567 - 832", "3452 - 36"]


#list for testing overflow in operand1
lst3 = ["23424 + 3424","234 + 4823"]


#list for testing overflow in operand2
lst4 = ["23 - 2342","243 + 42347","9874 + 2444"]


#list for testing operator type
lst5 = ["232 * 223","6709 % 9896"]

#list for overflow 
lst6 = ["3453 + 45", "5677 + 29", "905 + 667", "567 - 832", "3452 - 36,234 + 8348","2342 - 2834"]



arranger(lst1,True)
arranger(lst2,True)
arranger(lst3,True)
arranger(lst4,True)
arranger(lst5,True)
arranger(lst6,True)
arranger(lst1,False)
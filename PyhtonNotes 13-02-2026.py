'''
DATE 13-02-2026
Notes:
Operators: It is a symbol which is used to perform operations on operands.
1) Arithmetic Operators: + Addition
                         - Subtraction
                         * Multiplication
                         / Division (quotient)
                         // Floor Division (quotient without decimal part OR Round off division)
                         %  Modulus (remainder)
                         ** Exponentiation

2) Three ways to assign values to variable : =  a,b=10,20
                                                a=b=c=20
                                                a=b=10,20,30

3) Relational Operators: The value is given in boolean (True or False)
                         > Greater than
                         < Less than 
                         >= Greater than or equal to
                         <= Less than or equal to
                         == Equal to
                         != Not equal to
4) Assignment Operators: =  a = 10
                            += a += 5 (a = a + 5)
                            -= a -= 5 (a = a - 5)
                            *= a *= 5 (a = a * 5)
                            /= a /= 5 (a = a / 5)
                            //= a //= 5 (a = a // 5)
                            %= a %= 5 (a = a % 5)
                            **= a **= 5 (a = a ** 5)
5) Logical Operators: The value is given in boolean (True or False)
                      and  (True and True = True, True and False = False, False and False = False)
                      or   (True or True = True, True or False = True, False or False = False)
                      not   (not True = False, not False = True)

6) Bitwise Operators: It is used to perform bitwise operations on binary numbers.
                      &  (AND)
                      |  (OR)
                      ^  (XOR)
                      ~  (NOT)
                      << (Left Shift)
                      >> (Right Shift)
7) Unary Minus Operator: It is used to negate the value of the operand.
                         ex: a = 10 
                             print(-a)  # Output: -10
8) Identity Operators: The value is given in boolean (True or False)
                      is     (True if both operands refer to the same object, False otherwise)
                      is not (True if both operands do not refer to the same object, False otherwise) 
                  
'''

a = 20
print(a)
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)
a **= 5
print(a)

a,b=0,0
print(a and b)
print(a or b)
print(not a)
print(not b)

m=30
n=10
print(m<<2)
print(n>>2)
print(m&n)
print(m|n)
print(m^n)
print(~m)

a=True
b=False
print(type(b))
print(type(a))

l=[1,2,3,4]
print(10 in l)
print(5 not in l)

a = True
b = False
print(a is True)
print(b is not False)
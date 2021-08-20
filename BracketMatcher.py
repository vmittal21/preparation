# Question:

# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. 
# Otherwise return 0. 
# For example: 
# if str is "(hello (world))", then the output should be 1, 
# but if str is "((hello (world))" the the output should be 0 
# because the brackets do not correctly match up. 

# Only "(" and ")" will be used as brackets. 

# If str contains no brackets return 1.

# Use the Parameter Testing feature in the box below to test your code with different arguments.


# Solution Code:

# Language Used: Python
# Runtime Complexity: O(n)

def BracketMatcher(strParam):

    stack = []
    for i in range(len(strParam)):
      if strParam[i] == "(":
        stack.append("(")
       
      elif strParam[i] == ")" and len(stack)!=0 and stack[len(stack)-1] == "(":
        stack.pop()
       
      elif strParam[i] == ")" and stack[::-1] != "(":
        stack.append(")")
      
     
    if len(stack) == 0:
      return 1
    elif len(stack) > 0:
      return 0

# keep this function call here 
print(BracketMatcher(input()))
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == '(' or c == '{' or c == '['):
                stack.append(c)
            else:
                if(len(stack) < 1) :
                    return False
                a = stack[-1]
                del stack[-1]
                if ( c == ')'):
                    if (a != '('):
                        return False
                elif ( c == '}' ):
                    if( a != '{'):
                        return False
                elif ( c== ']' ):
                    if( a!= '['):
                        return False
        return len(stack) == 0
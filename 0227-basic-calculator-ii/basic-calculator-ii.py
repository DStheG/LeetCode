class Solution:
    def calculate(self, s: str) -> int:
        def isOperator(s: str):
            c = s[0]
            if c == '+' or c == '-' or c == '/' or c == '*':
                return True
            return False

        def doOperating(val1, val2, op):
            val1 = int(val1)
            val2 = int(val2)
            if (op == '+'):
                return val1 + val2
            elif (op == '-'):
                return val1 - val2
            elif (op == '/'):
                return val1 // val2
            elif (op == '*'):
                return val1 * val2
            else:
                return None
        
        val = ''
        vals = []
        ops = []
        for c in s:
            if (c == ' '):
                continue
            if(isOperator(c)):
                if (len(ops) and (ops[-1] == '*' or ops[-1] == '/')):
                    val = doOperating(vals[-1], int(val), ops[-1])
                    del(ops[-1])
                    del(vals[-1])
                    vals.append(val)
                    ops.append(c)
                else:
                    ops.append(c)
                    vals.append(int(val))
                val = ''
            else:
                val += c
        if (not len(ops)):
            return val
        if ((ops[-1] == '*' or ops[-1] == '/')):
            val = doOperating(vals[-1], int(val), ops[-1])
            del(ops[-1])
            del(vals[-1])
        vals.append(val)
        
        val = vals[0]
        for i in range(1, len(vals)):
            val = doOperating(val, vals[i], ops[i-1])
        return val

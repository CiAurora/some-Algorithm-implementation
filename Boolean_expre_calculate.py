def nibolan(str):
    flag = 0 #检查括号是否配对
    for elem in str:
        if elem == '(':
            flag += 1
        if elem == ')':
            flag -= 1
    if flag != 0:
        print('中缀表达式括号不匹配！')
        return -1
    priority = {'(':0,'!':1,'&':2,'^':3,'|':4} #不同运算符的优先级，数字越小优先级越高
    num = []
    operator = []
    for i in range(len(str)): # 扫描中缀表达式
        # 若为空格，跳过
        if str[i] == ' ':
            continue
        # 若为T/F，直接入操作数栈
        if str[i]=='T' or str[i]=='F':
            num.append(str[i])
        # 若为操作符
        else:
            # 若为‘（’，直接入运算符栈
            if str[i] == '(':
                operator.append(str[i])
            # 若为‘）’，则输出运算符堆栈中的运算符到操作数堆栈，直到遇到左括号为止
            elif str[i] == ')':
                while len(operator)!=0:
                    temp = operator.pop()
                    if temp != '(':
                        num.append(temp)
                    elif temp == '(':
                        break
            # 若为非括号运算符
            else:
                if len(operator) == 0:
                    operator.append(str[i])
                    continue
                # 若运算符栈顶为‘（’，直接存入运算符堆栈
                if operator[-1] == '(':
                    operator.append(str[i])
                # 若比运算符堆栈栈顶的运算符优先级高，则直接存入运算符栈
                elif priority[str[i]]<priority[operator[-1]]:
                    operator.append(str[i])
                # 若比运算符堆栈栈顶的运算符优先级低或相等，则不断输出栈顶运算符到操作数堆栈，直到栈顶没有运算符的优先级大于或者等于当前预算符
                else:
                    while len(operator) != 0:
                        temp = operator.pop()
                        if priority[temp]>priority[str[i]]:
                            break
                        num.append(temp)
                    # 压入当前运算符
                    operator.append(str[i])
    # 运算符栈剩下的全部弹入操作数栈
    while len(operator) != 0:
        temp = operator.pop()
        num.append(temp)

    print('后缀表达式为：',''.join(num))
    return num

def calculate(str):
    # 'T'/'F'<-->True/False
    def convert1(chr):
        if chr == 'T':
            return True
        else:
            return False
    def convert2(Bool):
        if Bool:
            return 'T'
        else:
            return 'F'
    # 转换输入中缀表达式为逆波兰表达式
    expre = nibolan(str)
    # 输入的中缀表达式括号不匹配，退出
    if expre == -1:
        return

    # 操作数栈
    num = []
    # 从左到右依次扫描语法单元的项目
    for elem in expre:
        # 如果扫描的项目是操作数，则将其压入操作数堆栈，并扫描下一个项目
        if elem == 'T' or elem == 'F':
            num.append(elem)
        # 如果扫描的项目是一个二元运算符，则对栈的顶上两个操作数执行该运算，运算结果压回栈顶
        elif elem == '&':
            if len(num)>=2:
                a = convert1(num.pop())
                b = convert1(num.pop())
                c = convert2(a and b)
                num.append(c)
            else:
                print('缺少操作数！')
                return -1
        elif elem == '|':
            if len(num)>=2:
                a = convert1(num.pop())
                b = convert1(num.pop())
                c = convert2(a or b)
                num.append(c)
            else:
                print('缺少操作数！')
                return -1
        elif elem == '^':
            if len(num)>=2:
                a = convert1(num.pop())
                b = convert1(num.pop())
                c = convert2(not(a or b))
                num.append(c)
            else:
                print('缺少操作数！')
                return -1
        # 如果扫描的项目是一个一元运算符，则对栈的顶上一个操作数执行该运算，运算结果压回栈顶
        elif elem == '!':
            if len(num)>=1:
                a = convert1(num.pop())
                c = convert2(not a)
                num.append(c)
            else:
                print('缺少操作数！')
                return -1
    # 刚好算出答案
    if len(num)==1:
        print('答案是：',num[0])
        return num[0]
    # 多剩了操作数
    else:
        print('缺少运算符！')
        return -1

str1='(T |T)& F&(F|T)'
print('1.测试数据1-无错表达式：',str1)
calculate(str1)
str2='(T |T)& F&(F|T))'
print('2.测试数据2-括号不匹配：',str2)
calculate(str2)
str3='(T |T)& F&|(F||T)'
print('3.测试数据3-缺少操作数：',str3)
calculate(str3)
str4='(T |T)& F&(F|T)T'
print('4.测试数据4-缺少运算符：',str4)
calculate(str4)
print('----------------------------------------')
print('再计算几个无错表达式吧！')
str5='(T |T) '
print('5.测试数据5-无错表达式：',str5)
calculate(str5)
str6='(T ^F)|T&F|(T^T)'
print('6.测试数据6-无错表达式：',str6)
calculate(str6)

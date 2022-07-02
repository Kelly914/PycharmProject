# Packages and Modules import statements
# --------------------------------------
import random
import sys

# codings
# --------------------------------------
'''
算法1：斐波那契数列的递归实现
'''

def fib(n):
    """
    构造一个斐波那契数
    :param n: 第几个斐波那契数，int类型
    :return: 一个斐波那契数，int类型
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def getFibList(fib_nums):
    """
    构造n个数的斐波那契数列
    :return: 构造的斐波那契数列，list类型
    """
    return [fib(i) for i in range(1, fib_nums + 1)]

nums = int(input('请输入斐波那契数列的长度：'))
print('构造的{}个元素的斐波那契数列为：{}'.format(nums,getFibList(nums)))

'''
算法2：“不死兔子”的递归实现
'''


def noDieOfRabbitFibs(month):
    """
    不死兔子递归算法实现
    :param month:月份，int类型
    :return: 当月的兔子数，int类型
    """
    if month == 1:
        return 1
    elif month == 2:
        return 1
    else:
        return noDieOfRabbitFibs(month - 1) + noDieOfRabbitFibs(month - 2)
print('一年后共计：{}只兔子'.format(2 * noDieOfRabbitFibs(12)))

'''
算法3：“变态青蛙跳”的递归实现
    --------------
    算法分析：
    设台阶数为n，对应的跳法数为f(n)
    n = 1 -- f(1) = 1
    n = 2 -- f(2) = 2
    n = 3 -- f(3) = f(2) + f(1)
    n = 4 -- f(4) = f(3) + f(2)
    n = 5 -- f(5) = f(4) + f(3)
    ...
    n = n -- f(n) = f(n-1) + f(n-2)
    所以，n个台阶，青蛙的跳法数f(n) = f(n-1) + f(n-2)
'''


def fibForgs(n):
    """
    “变态青蛙跳”的递归实现
    :param n: 台阶数，int类型
    :return: 对应跳法数，int类型
    """
    if n == 0:
        return '台阶数不合法！'
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibForgs(n - 1) + fibForgs(n - 2)
floor_nums = int(input('请输入台阶数：'))
print('青蛙跳上一个{}级台阶共计：{}种跳法'.format(floor_nums,fibForgs(floor_nums)))


'''
算法4：“变态青蛙跳”绝望升级版的递归实现
    --算法分析：
    设台阶数为n，对应的跳法数为f(n)
    假设没有台阶时青蛙原地跳一下，则：
    n = 0 -- f(0) = 1
    n = 1 -- f(1) = 1
    n = 2 -- f(2) = 2
    n = 3 -- f(3) = f(2) + f(1) + f(0)
    n = 4 -- f(4) = f(3) + f(2) + f(1) + f(0)
    n = 5 -- f(5) = f(4) + f(3) + f(2) + f(1) + f(0)
    ...
    n = n -- f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(1) + f(0)
    此递归公式无法直接看出等量关系，现对其采用数学归纳法进行化简：
    f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(1) + f(0) -- 1式
    现将所有的n = n - 1,得：
    f(n-1) = f(n-2) + f(n-3) + f(n-4) + ... + f(1) + f(0) -- 2式
    1式 - 2式：
    f(n) - f(n-1) = f(n-1)
    所以：
    f(n) = 2 * f(n-1)
    即：当台阶数为n时，对应跳法数f(n) = 2 * f(n-1)
'''


def fibForgsPlus(n):
    """
    “变态青蛙跳”绝望升级版的递归实现
    :param n: 台阶数，int类型
    :return: 对应跳法数，int类型
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2 * fibForgsPlus(n - 1)
floor_nums = int(input('请输入台阶数：'))
print('青蛙跳上一个{}级台阶共计：{}种跳法'.format(floor_nums,fibForgsPlus(floor_nums)))

'''
算法5：“猴子吃桃”问题的递归实现
'''


def monkey(x, day):
    """
    “猴子吃桃”问题的递归实现
    :param x: 当天桃子数，int类型
    :param day: 天数，int类型
    :return: 第一天的总桃子数，int类型
    """
    day -= 1
    if day == 0:
        return x
    x = 2 * (x + 1)
    return monkey(x, day)
print('10天前共计：{}个桃子'.format(monkey(1,10)))

'''
算法6：“数的阶乘”问题的递归实现
'''


def factorial(n):
    """
    “数的阶乘”问题的递归实现
    :param n: 计算阶乘的数，int类型
    :return: 阶乘的结果，int类型
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input('请输入数字：'))
print('数字{}的阶乘结果为：{}'.format(num,factorial(num)))

'''
算法7：“最后留下的人是第几号？”
    - 问题描述：有n个人围成一圈，顺序排号。从第一个人开始报数（1~3报数），凡报到3的人退出圈子，问最后留下的人原来排在第几号？
    - 测试用例：
    ```text
    输入：参与游戏的人数
    输出：最后剩下的人编号为：xx
    ```
'''


def makeAlogorithmLists(num):
    """
    构造一个符合算法要求的列表，列表长度表示参与游戏的人数，列表每个元素的值代表这个人的编号
    :param num:人数，int类型
    :return: list类型
    """
    return [x for x in range(1, num + 1)]


def alogorithm_7(l):
    """
    算法实现
    :param l: 游戏序列，list类型
    :return: 最后一个人的编号，int类型
    """
    # 计算报数
    k = 0
    while len(l) > 1:
        l_copy = l[:]
        for i in range(len(l_copy)):
            k += 1
            if k % 3 == 0:
                l.remove(l_copy[i])
    return l[0]
num = int(input('请输入参与游戏的人数：'))
print('{}个人围成一圈，退出圈子后最后剩下的这个人的编号是：{}'.format(num,alogorithm_7(makeAlogorithmLists(num))))

'''
算法8：数组调整
    - 问题描述：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
    - 测试用例：
    ```text
    输入：随机整数序列
    输出：按需调整之后的序列
    ```
'''


def makeRandomList(n, left, right):
    """
    构造n个数的，指定随机范围区间的随机数序列
    :param n: 序列个数，int类型
    :param left: 随机范围左区间，int类型
    :param right: 随机范围右区间，int类型
    :return: 构造出来的随机序列，list类型
    """
    return [random.randint(left, right) for i in range(n)]


def alogorithm_8(l):
    """
    算法8：数组调整算法实现
    :param l: 需要调整的序列，list类型
    :return: 调整后的序列，list类型
    """
    return [i for i in l if i % 2 == 1] + [j for j in l if j % 2 == 0]
n = int(input('请输入需要的序列长度：'))
left = int(input('请输入随机范围左区间：'))
right = int(input('请输入随机范围右区间：'))
init_random_list = makeRandomList(n,left,right)
print('原随机序列为：{}'.format(init_random_list))
print('按需调整后的序列为：{}'.format(alogorithm_8(init_random_list)))

'''
算法9：城镇人口普查
    - 问题描述：某城镇进行人口普查，得到了全体居民的生日。现请编写一段程序，找出镇上最年长和最年轻的人。
    - 测试用例：
    ```text
    输入：
    姓名，生日（年/月/日）
    输出：
    年龄最大的人是：xxx，生日为：xxx
    年龄最小的人是：xxx，生日为：xxx
    ```
'''


def makeAlogorithmData(person_num):
    """
    算法所需数据：居民生日数据准备
    测试样例：
    输入：
    请输入居民姓名及生日信息：tom,1919/09/09
    请输入居民姓名及生日信息：lisa,1929/09/10
    请输入居民姓名及生日信息：jack,1992/09/02
    输出：
    [['tom', '1919/09/09'], ['lisa', '1929/09/10'], ['jack', '1992/09/02']]
    :param person_num: 需要几条测试用例，int类型
    :return: 一组测试数据，list类型
    """
    return [input('请输入居民姓名及生日信息：').split(',') for i in range(person_num)]


def alogorithm_9(data):
    """
    传入测试数据
    :param data:测试样例，list类型
    :return: 年龄最大数据和年龄最小数据，list类型
    """
    # 计数生日数据合法的样本数
    count = 0
    # 年龄最小范围截止到当前今天算作合法
    max_data = ['', '2021/08/23']
    # 年龄最大范围截止到100年前的今天算作合法
    min_data = ['', '1921/08/23']
    for person in range(len(data)):
        # 先判断测试数据是否合法，合法的生日才有效
        if '1921/08/23' <= data[person][1] <= '2021/08/23':
            # 如果合法，则合法样本数+1
            count += 1
        # 如果当前居民的生日在'2021/08/23'之前：
        if data[person][1] < max_data[1]:
            max_data = data[person]
        if data[person][1] > min_data[1]:
            min_data = data[person]
    if count == 0:
        print('不存在任何合法数据！')
        # 不存在合法数据的话，算法无法执行，直接强制结束程序运行
        sys.exit()
    else:
        return count, max_data, min_data
num = int(input('请输入测试样本数：'))
count,max_data,min_data = alogorithm_9(makeAlogorithmData(num))
print('在共计{}份合法的居民生日样本数据中，年龄最大的居民是：{}，其生日为：{}；年龄最小的居民是：{}，其生日为：{}'.format(count,max_data[0],max_data[1],min_data[0],min_data[1]))

'''
    算法10：排列最小值
        - 问题描述：给定数字0-9各若干个。你可以以任意顺序排列这些数字，但必须全部使用。目标是使得最后得到的数尽可能小（注意0不能做首位）。
        - 测试用例：
        ```text
        每个输入包含1个测试用例。每个测试用例在一行中给出10个非负整数，顺序表示我们拥有数字0、数字1、……数字9的个数。整数间用一个空格分
        隔。10个数字的总个数不超过50，且至少拥有1个非0的数字。
        输出格式：
        在一行中输出能够组成的最小的数。
        例如：
        输入一组测试用例：
        2 2 0 0 0 3 0 0 1 0
        输出：
        能构成的最小值为：10015558
        ```
    --------------
    算法分析：
    该算法的难点其实在于：对一组测试用例的数据预处理。
    按照题目描述的要求输入，该组数据无法直接被算法使用
    我们需要按照测试用例的输入，将其转化、处理为：给定的所有可用数字的序列
    随后对该序列做算法操作，即可得到能够组成的最小值
    实现思路：
    例如：
    输入：3 4 2 1 3 2 3 1 2 3
    如果将其看作一个列表则该输入的含义为：num个index（3为列表元素值，0为该元素的索引）；
    即：
    3个0
    4个1
    2个2
    ...
    所以现在的关键问题就是：将其按照这个输入规律：
    000
    1111
    22
    3
    444
    55
    666
    7
    88
    999
    全部拼接在一起，得到这样的结果序列：
    000111122344455666788999
    只有拿到这样的结果，我们才能开始执行算法。
    继续分析：我们输入了这样的数字，请问如何组合，能够保证构造一个最小值呢？
    首先：该值的最高位是不能为0的，因为算法要求给到的所有数字都要使用到
    所以为了确保构成最小值，最高位只能为1；
    那其余位呢？其实只要其余位是升序排列即可，得到的最终结果就是一个最小值
    ok，思路明确，接下来实现该算法
'''


def makeAlogorithm_10Data(testUseCaseData):
    """
    依据输入的测试用例构造符合算法需求的测试数据
    :param testUseCaseData: 测试用例，str类型
    :return:预处理后的数据，list类型
    """
    testUseCaseData_list = testUseCaseData.split(' ')
    return [j for j in ''.join([str(i) * int(testUseCaseData_list[i]) for i in
                                range(len(testUseCaseData_list))])]


def alogorithm_10(data):
    """
    算法10实现
    :param data:预处理后的测试数据，list类型
    :return: 最终的最小值结果，str类型
    """
    for i in range(len(data)):
        # 循环遍历，只要找到第一个不为0的值，立刻将其与列表第一个元素做位置交换，随后立刻结束循环
        if data[i] != '0':
            data[0], data[i] = data[i], data[0]
            break
    return ''.join(data)
tests_10 = input('请输入一组测试用例')
print('该组测试用例：{}可以构成的最小整数值为：{}'.format(tests_10,alogorithm_10(makeAlogorithm_10Data(tests_10))))

'''
算法11：完美数列
    - 问题描述：给定一个正整数数列，和正整数p，设这个数列中的最大值是M，最小值是m，如果M <= m * p，则称这个数列是完美数列。
    - 测试用例：
    ```text
    输入：一个无序序列，一个整数
    输出：是否为完美序列
    ```
'''


def alogorithm_11(l, n):
    """
    算法11实现
    :param l: 正整数序列，list类型
    :param n: 正整数，int类型
    :return: 是否为完美数列，bool类型
    """
    if max(l) <= n * min(l):
        return True
    return False
random_list = makeRandomList(20,1,20)
print('随机数序列：{}，{}一个完美序列'.format(random_list,'是' if alogorithm_11(random_list,int(input('请输入一个值：'))) else '不是'))

'''
算法12：数字黑洞
    - 问题描述：给定任意一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序得到结果1，再按非递减排序得到结果2，然后用结
    果1-结果2，将得到一个新的数字。一直重复这样做，你会发现结果很快停留在6174，这个6174称之为“数字黑洞”，这个神奇的数字也称之为
    Kaprekar常数。
    例如，我们从6767开始，将得到：
    7766 - 6677 = 1089
    9810 - 0189 = 9621
    9621 - 1269 = 8352
    8532 - 2358 = 6174
    7641 - 1467 = 6174
    ......
    - 测试用例：
    输入：4位正整数
    输出：按照上述演示格式输出达到数字黑洞的过程
'''


def makeAlogorithm_12Data(num):
    """
    测试用例数据预处理
    :param num: 测试数据，str类型
    :return: 预处理后的可用数据，str类型
    """
    if len(num) < 4:
        num = '0' * (4 - len(num)) + num
        return num


def alogorithm_12(data):
    """
    算法12实现
    :param data: 预处理后的可用数据
    :return:
    """
    # 先计算非递增：递减排序结果
    str_down = ''.join(sorted(data, reverse=True))
    # 再计算非递减：递增排序结果
    str_up = ''.join(sorted(data))
    # 递减-递增
    result = str(int(str_down) - int(str_up))
    if len(result) < 4:
        result = '0' * (4 - len(result)) + result
    if result == '0000':
        print('{} - {} = 0000'.format(str_down, str_up))
    else:
        if result == '6174':
            print('{} - {} = {}'.format(str_down, str_up, result))
            # print('{} - {} = "0000"'.format(str_down, str_up))
            return
        else:
            print('{} - {} = {}'.format(str_down, str_up, result))
            return alogorithm_12(result)
# alogorithm_12(makeAlogorithm_12Data(input('请输入')))
alogorithm_12(makeAlogorithm_12Data(input('请输入一个数字，即将开始演算数字黑洞：')))


# run test UseCase if current modules is main
if __name__ == '__main__':
    pass

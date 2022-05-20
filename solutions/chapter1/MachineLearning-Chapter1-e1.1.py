"""
Curious
"""

"""
每个西瓜用一个6位的二进制数来代表
第0-1位代表色泽，01-青绿，10-乌黑，11-*（*代表青绿或乌黑均可）
第2-3位代表根蒂，01-蜷缩，10-稍蜷，11-*
第4-5位代表敲声，01-浊响，10-沉闷，11-*
"""


def num2str(num, str_list):
    if num & 0b11 == 0b01:
        if num != 0b010101:
            str_list += ' '
        str_list += '青绿'
    if num & 0b11 == 0b10:
        str_list += ' 乌黑'
    if num & 0b11 == 0b11:
        str_list += ' *'
    if num & 0b1100 == 0b0100:
        str_list += '蜷缩'
    if num & 0b1100 == 0b1000:
        str_list += '稍蜷'
    if num & 0b1100 == 0b1100:
        str_list += '*'
    if num & 0b110000 == 0b010000:
        str_list += '浊响'
    if num & 0b110000 == 0b100000:
        str_list += '沉闷'
    if num & 0b110000 == 0b110000:
        str_list += '*'

    return str_list


HypoList = []
StrList = ''
for i in range(0b010101, 0b111111 + 1):
    if i & 0b11 == 0 or i & 0b1100 == 0 or i & 0b110000 == 0:
        continue

    HypoList.append(i)

    StrList = num2str(i, StrList)

HypoLen = len(HypoList)
print(HypoLen)
print(HypoList)
for i in range(0, HypoLen):
    print('0b{:0>6b}'.format(HypoList[i]), end=' ')  # 用函数bin()也可打印二进制，但无法补位，而用print自己的格式化打印没有二进制
print('\t')
print(StrList)


PosHypo = 0b010101
NegHypo = 0b101010
VersionSpace = []
VersionSpaceStr = ''
for i in range(HypoLen):
    if (HypoList[i] | PosHypo) == HypoList[i] and (HypoList[i] | NegHypo) != HypoList[i]:
        VersionSpace.append(HypoList[i])
        VersionSpaceStr = num2str(HypoList[i], VersionSpaceStr)

print('\t')
print(len(VersionSpace))
print(VersionSpace)
for i in range(0, len(VersionSpace)):
    print('0b{:0>6b}'.format(VersionSpace[i]), end=' ')
print('\t')
print(VersionSpaceStr)

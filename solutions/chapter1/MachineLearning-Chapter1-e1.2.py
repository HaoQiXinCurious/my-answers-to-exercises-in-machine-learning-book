"""
Curious
"""

from numba.typed import List
import getHypoOld
from printAsBinary import print_as_binary
from getDisjunctiveFormNum import get_disjunctive_form_num, get_disjunctive_form_num_optimized

"""
第0-1位代表色泽，01-青绿，10-乌黑，11-*（*代表青绿或乌黑均可）
第2-4位代表根蒂，001-硬挺，010-稍蜷，100-蜷缩，111-*
第5-7位代表敲声，001-清脆，010-沉闷，100-浊响，111-*
"""

HypoOld, HypoOldStr = getHypoOld.get_hypo_old()  # 获得含*的48个合取式
print_as_binary(HypoOld, 8)
print(HypoOldStr)

HypoOldNoStar, HypoOldStrNoStar = getHypoOld.get_hypo_old_no_star()  # 获得不含*的18个合取式
print_as_binary(HypoOldNoStar, 8)
print(HypoOldStrNoStar)

# 将含*的48个合取式转换成由18个合取式析取组合而成的形式
HypoOldLen = len(HypoOld)
HypoNew = [0] * HypoOldLen  # 用于存放转换后的式子
for i in range(HypoOldLen):
    for j in range(len(HypoOldNoStar)):
        if HypoOld[i] | HypoOldNoStar[j] == HypoOld[i]:
            HypoNew[i] |= 0b1 << j
print_as_binary(HypoNew, 18)
print(HypoOldStr)

RecordSheet = [0] * (0b111111111111111111 + 1)  # 记录表，用于确认新的析合范式是否已记录并记录未记录的
k = 1  # 析取的合取式个数k，从1开始
Result = 0  # 记录结果，也就是析合范式的数量
type_HypoNew = List()
type_RecordSheet = List()
[type_HypoNew.append(x) for x in HypoNew]
[type_RecordSheet.append(x) for x in RecordSheet]
# while True:  # while循环
#     Result += get_disjunctive_form_num_optimized(type_HypoNew, type_RecordSheet, k)
#     # Result += get_disjunctive_form_num(HypoNew, RecordSheet, k)  # 求结果的函数，内部具体讲解
#     print(k, Result)
#     k += 1
#
#     if Result == 0b111111111111111111:  # 当结果达到能存在的析合范式的最大值时，循环结束，之后k再大结果不变
#         break

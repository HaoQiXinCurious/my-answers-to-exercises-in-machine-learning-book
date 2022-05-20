"""
Curious
"""
from numba import jit
from numba import njit


def get_disjunctive_form_num(hypo_new, record_sheet, k):
    count = 0  # 存储不重复的析合范式的数量
    current_flag = k - 1  # 记录正在移动的下标是第几号
    flag_sheet = [0] * k  # 记录每一个下标所处的位置
    for i in range(k):  # 设置好每个下标最初的位置
        flag_sheet[i] = i

    while True:
        disjunctive_form = 0  # 用于暂存新得到的析合范式
        for i in range(k):
            disjunctive_form |= hypo_new[flag_sheet[i]]  # 将当前下标表指向的几个式子析取
        if record_sheet[disjunctive_form] == 0:  # 将新的到的析取式与对照表进行比对
            count += 1  # 对照表还没有就给计数值加1
            record_sheet[disjunctive_form] = 1  # 计数加1后把对应位置置1，组织下次在这个值时进入
        # 当正在移动的下标走到它能走到的最边缘时就把指向的下标值-1，如果这个下标也在边缘则继续，直到值变为-1
        while current_flag >= 0 and flag_sheet[current_flag] == len(hypo_new) + current_flag - k:
            current_flag -= 1
        if current_flag == -1:  # 变为-1表示最前面的下标都走完了所有情况，即遍历完成，退出循环
            break
        flag_sheet[current_flag] += 1  # 给正在移动的下标位置+1，即下标的指向向左移动1位
        # 如果正在移动的下标不是最右边的下标，将它左边的下标值变为此下标值+1，并将移动的下标变为左边那个下标，循环直到移动的下标变为最左边的下标
        while current_flag < k - 1:
            flag_sheet[current_flag + 1] = flag_sheet[current_flag] + 1
            current_flag += 1

    return count


@njit  # 用于优化代码运算时间
def get_disjunctive_form_num_optimized(hypo_new, record_sheet, k):
    count = 0  # 存储不重复的析合范式的数量
    current_flag = 0  # 记录正在移动的下标是第几号
    flag_sheet = [0] * k  # 记录每一个下标所处的位置
    form_in_process = [0] * k  # 优化点，第i个位置里记录着第0到i个下标指向的式子析取而得的析取式
    flag_next_move = 0  # 记录下次循环下标要做的操作，0为让当前正在移动的下标自增1也就是右移一位，1为将当前下标右边的下标变为当前下标
    for i in range(k):  # 设置好每个下标最初的位置
        flag_sheet[i] = -1  # 置为-1是因为循环最开始的操作是第0个下标移动到第0位，所以是从-1变成0

    while True:
        if current_flag == 0:
            flag_sheet[current_flag] += 1
            if flag_sheet[0] > len(hypo_new) - k:  # 循环退出条件
                break
            form_in_process[0] = hypo_new[flag_sheet[0]]  # 给当前的第0位赋值hypo_new对应的式子
            if form_in_process[0] == 0b111111111111111111 and k > 1:  # 优化点，当k不为0且得到的值为全*时跳过
                continue
            current_flag += 1
            flag_next_move = 1
        else:
            if flag_next_move == 1:
                flag_sheet[current_flag] = flag_sheet[current_flag - 1] + 1
            else:
                flag_sheet[current_flag] += 1

            if flag_sheet[current_flag] > len(hypo_new) + current_flag - k:  # 当前下标走到边缘
                current_flag -= 1  # 当前下标走到边缘，所以将前一个下标变成新的当前下标
                flag_next_move = 0  # 下次循环让下标表对应新的当前下标的值自增1
                continue

            form_in_process[current_flag] = form_in_process[current_flag - 1] | hypo_new[flag_sheet[current_flag]]
            # 优化点，
            if form_in_process[current_flag] == form_in_process[current_flag - 1] \
                    or (form_in_process[current_flag] == 0b111111111111111111 and current_flag < k - 1):
                flag_next_move = 0
                continue

            current_flag += 1
            flag_next_move = 1

        if current_flag == k:  # 完成一次k个式子的析取
            current_flag -= 1  # 此时的current_flag已大于边界，回到循环前要减1
            flag_next_move = 0  # 设定下次循环时下标表对应当前下标的值自增1
            if record_sheet[form_in_process[current_flag]] == 0:  # 与对照表进行比对，没出现过计数+1后将对照表对应值置1
                count += 1
                record_sheet[form_in_process[current_flag]] = 1

    return count

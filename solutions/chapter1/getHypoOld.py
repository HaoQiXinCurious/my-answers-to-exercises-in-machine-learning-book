"""
Curious
"""

"""
第0-1位代表色泽，01-青绿，10-乌黑，11-*（*代表青绿或乌黑均可）
第2-4位代表根蒂，001-硬挺，010-稍蜷，100-蜷缩，111-*
第5-7位代表敲声，001-清脆，010-沉闷，100-浊响，111-*
"""


def get_hypo_old_list(x, y, z, num=0):  # 根据特征的值返回对应数字
    if x == 0:
        num |= 0b01
    elif x == 1:
        num |= 0b10
    else:
        num |= 0b11
    if y == 0:
        num |= 0b00100
    elif y == 1:
        num |= 0b01000
    elif y == 2:
        num |= 0b10000
    else:
        num |= 0b11100
    if z == 0:
        num |= 0b00100000
    elif z == 1:
        num |= 0b01000000
    elif z == 2:
        num |= 0b10000000
    else:
        num |= 0b11100000

    return num


def get_hypo_str_list(num, str_list):  # 根据对应数字返回字符串
    if num & 0b11 == 0b01:
        if num != 0b00100101:
            str_list += '\n'
        str_list += '青绿'
    if num & 0b11 == 0b10:
        str_list += '\n乌黑'
    if num & 0b11 == 0b11:
        str_list += '\n*'
    if num & 0b11100 == 0b00100:
        str_list += '硬挺'
    if num & 0b11100 == 0b01000:
        str_list += '稍蜷'
    if num & 0b11100 == 0b10000:
        str_list += '蜷缩'
    if num & 0b11100 == 0b11100:
        str_list += '*'
    if num & 0b11100000 == 0b00100000:
        str_list += '清脆'
    if num & 0b11100000 == 0b01000000:
        str_list += '沉闷'
    if num & 0b11100000 == 0b10000000:
        str_list += '浊响'
    if num & 0b11100000 == 0b11100000:
        str_list += '*'

    return str_list


def get_hypo_old():
    num_of_color_type_old = 3  # 色泽种类数（包括*）
    num_of_root_type_old = 4  # 根蒂种类数（包括*）
    num_of_sound_type_old = 4  # 敲声种类数（包括*）
    num_of_hypo = num_of_color_type_old * num_of_root_type_old * num_of_sound_type_old  # k=1时西瓜假设数
    hypo_old = [0] * num_of_hypo
    hypo_old_str = ''
    index = 0
    # 0-2，0-3，0-3三层循环，最外层0时给0-1位配01，1时10，2时11，第二、三层0时给2-4位或5-7位配001，1时010，2时100，3时111
    for i in range(num_of_color_type_old):
        for j in range(num_of_root_type_old):
            for k in range(num_of_sound_type_old):
                hypo_old[index] = get_hypo_old_list(i, j, k)  # 根据特征的值返回对应数字
                hypo_old_str = get_hypo_str_list(hypo_old[index], hypo_old_str)
                index += 1
    return hypo_old, hypo_old_str


def get_hypo_old_no_star():
    num_of_color_type_old = 2  # 色泽种类数（不包括*）
    num_of_root_type_old = 3  # 根蒂种类数（不包括*）
    num_of_sound_type_old = 3  # 敲声种类数（不包括*）
    num_of_hypo = num_of_color_type_old * num_of_root_type_old * num_of_sound_type_old  # k=1时西瓜假设数
    hypo_old = [0] * num_of_hypo
    hypo_old_str = ''
    index = 0
    # 0-2，0-3，0-3三层循环，最外层0时给0-1位配01，1时10，2时11，第二、三层0时给2-4位或5-7位配001，1时010，2时100，3时111
    for i in range(num_of_color_type_old):
        for j in range(num_of_root_type_old):
            for k in range(num_of_sound_type_old):
                hypo_old[index] = get_hypo_old_list(i, j, k)
                hypo_old_str = get_hypo_str_list(hypo_old[index], hypo_old_str)
                index += 1
    return hypo_old, hypo_old_str

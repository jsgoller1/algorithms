from itertools import izip
from operator import xor

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4,s5), ...."
    a = iter(iterable)
    return izip(a,a)

def quat_mult(quat1, quat2):
    if quat1 == quat2:
        if quat1 == "1":
            return "1", True
        else:
            return "1", False
    if quat1 == "1":
        return quat2, True
    if quat2 == "1":
        return quat1, True

    if quat1 == "i":
        if quat2 == "j":
            return "k", True
        if quat2 == "k":
            return "j", False

    if quat1 == "j":
        if quat2 == "i":
            return "k", False
        if quat2 == "k":
            return "i", True

    if quat1 == "k":
        if quat2 == "j":
            return "i", False
        if quat2 == "i":
            return "j", True

def total_quat_reduce(string):
    n = 0
    quat = "1"
    positive = True
    while n < len(string):
        #print "caught in total_quat_red"
        quat, sign = quat_mult(quat, string[n])
        positive = not(xor(sign, positive))
        n += 1
    return quat, positive

case_counter = 1
data = open('data.txt','r').read().split('\n')[1:-1]
for line1, line2 in pairwise(data):
    strlen, reps = line1.split(" ")
    strlen = int(strlen)
    reps = int(reps)
    chars = line2
    reducible = 'NO'
    if strlen == 1:
        print 'Case #'+str(case_counter)+":", reducible
        case_counter += 1
        continue
    which = 0
    if 'j' in chars:
        which+=1
    if 'k' in chars:
        which+=1
    if 'i' in chars:
        which+=1
    if which < 2:
        print 'Case #'+str(case_counter)+":", reducible
        case_counter += 1
        continue
    full = chars*reps
    full_len = strlen*reps

    i_index = 0
    quat1 = "1"
    pos1 = True
    while i_index < full_len-2:
        quat1, sign = quat_mult(quat1, full[i_index])
        i_index += 1
        pos1 = not(xor(sign, pos1))
        if quat1 == "i":
            neg2 = True
            quat2 = "1"
            j_index = 0
            j_substring = full[i_index:]
            while j_index < len(j_substring)-1:
                #print("caught at 86")
                pos2 = True
                quat2, sign = quat_mult(quat2, j_substring[j_index])
                j_index +=1
                pos2 = not(xor(sign, pos2))
                if quat2 == "j":
                    k_substring = j_substring[j_index:]
                    quat3, sign3 = total_quat_reduce(k_substring)
                    if quat3 == "k":
                        if not(xor(sign3, pos2)):
                            reducible = 'YES'

    print 'Case #'+str(case_counter)+":", reducible
    case_counter += 1

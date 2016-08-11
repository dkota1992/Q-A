S = """dir1
 dir11
 dir12
  picture.jpeg
  dir121
  file1.txt
dir2
 file2.gif
"""

def solution(S):
    S = S.split('\n')
    kk = []
    pp = []
    for ss in S:
        count = sum([1 for c in ss if c == ' '])
        pp.append("".join(c for c in ss if c not in (" ")))
        kk.append(count)
    count = 0
    for ss in pp:
        if '.jpeg' in ss or '.png' in ss or '.gif' in ss:
            count = count + len(ss) +1
            c = pp.index(ss)
            p = c
            while c>0:
                if kk[c-1]<kk[p]:
                    count = count + len(pp[c-1]) +1
                    p = p-1
                c = c-1
    return count  
            

print(solution(S))

# 올바른 문자열인지 확인하는 함수
def is_correct(p):
    cnt = 0
    for a in p:
        if a == '(': cnt += 1
        else: cnt -=1
        if cnt < 0: return False
    if cnt == 0: return True
    else: return False

# 균형잡힌 문자열을 u와 v로 분리하는 함수
def sep(p):
    cnt1, cnt2, idx = 0, 0, 0
    for i in range(len(p)):
        if p[i] == '(': cnt1 += 1
        elif p[i] == ')': cnt2 += 1
        if cnt1 == cnt2:
            idx = i
            break
    return p[:i+1], p[i+1:]

def running(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p is None: return p
    else:
        # 올바른 문자열인지 확인
        if is_correct(p): return p
        else:
            # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
            u, v = sep(p)
            if is_correct(u):
                return u + running(v)
            else:
                res = '(' + running(v) + ')'
                u = u[1:] # 첫 번째 문자 제거
                u = u[:-1] # 마지막 문자 제거
                for a in u:
                    if a == '(': res += ')'
                    else: res += '('
                return res

def solution(p):
    return running(p)

'''
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
'''
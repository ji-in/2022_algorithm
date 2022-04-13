def check(ans):
    for x, y, a in ans:
        if a == 0:
            if y != 0 and ([x-1, y, 1] not in ans and [x, y, 1] not in ans) and [x, y-1, 0] not in ans:
                return False
        else:
             if ([x, y-1, 0] not in ans and [x+1, y-1, 0] not in ans) and ([x-1, y, 1] not in ans or [x+1, y, 1] not in ans):
                    return False
    return True

def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        item = [x, y, a]
        if b: # 설치
            answer.append(item)
            if not check(answer):
                answer.remove(item)
        elif item in answer: # 삭제
            answer.remove(item)
            if not check(answer):
                answer.append(item)

    return sorted(answer)
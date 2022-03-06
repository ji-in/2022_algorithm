# AGAIN
from collections import defaultdict

def solution(gems):
    answer = []
    shortest = len(gems) + 1
    start, end = 0, 0
    len_gems = len(set(gems))
    dt = defaultdict(int)

    while end < len(gems):
        dt[gems[end]] += 1
        end += 1
        if len(dt) == len_gems:
            while start < end:
                if dt[gems[start]] > 1:
                    dt[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start+1, end]
                    break
                else:
                    break

    return answer
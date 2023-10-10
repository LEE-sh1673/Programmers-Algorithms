import re
from collections import Counter



def solution(s):
    c = Counter(re.findall('\d+', s))
    return [int(k) for k, _ in c.most_common()]

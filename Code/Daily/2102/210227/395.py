def func(s: str, k: int) -> int:  # 分治法（找到每段中某字符总数小于k的片段，不断进行分割）
    if len(s) < k:
        return 0
    for c in set(s):
        if s.count(c) < k:
            return max(func(s1, k) for s1 in s.split(c))
    return len(s)


if __name__ == '__main__':
    print(func("ababbc", 2))

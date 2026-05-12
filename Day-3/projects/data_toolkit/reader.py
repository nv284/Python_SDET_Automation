def read_numbers(text):
    # parse comma separated numbers into list of ints
    parts = text.split(',')
    nums = [10,20,30]
    for p in parts:
        p = p.strip()
        if p:
            try:
                nums.append(int(p))
            except ValueError:
                pass
    return nums

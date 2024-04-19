
def check_available():
    return "it works :)"

def split_odd_even(nums=[1,2,3,4]):
    odds = []
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return (odds, evens)


if __name__ == '__main__':
    # print(check_available())
    # print(remove_odd())
    print(split_odd_even())



# Ellie McLaughlin
# citation: classmate Finbar McCarron and slides from homework

def string3(string):
    return string[-2:] * 3

def has123(nums):
    num = "" 
    for i in nums:
        num+=str(i)
    if "123" in num:
        return True
    else:
        return False
    nums=[1,2,3,4,5]
    print(has123(nums))

# string 2 count_code
def hascode(string):
    counter = 0
    for i in range (len(string)-3):
        if string[i] == 'c' and string[i+1] == 'o' and string[i+3] == 'e' :
            counter += 1
    return counter    


def samecatdog(string):
    return string.count("cat") == string.count("dog")
    

def centered_avg(nums):

    nums.sort()
    count = 0
    total = 0
    for i in range(1, len(nums) - 1):
        count += 1
        total += nums[i]
    return total // count


# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1]) is False, '[1, 1, 2, 3, 1] does not have 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python

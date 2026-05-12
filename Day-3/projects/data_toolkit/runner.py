from reader import read_numbers
from processor import stats

print('Data Toolkit Runner')
sample = '10,20,30,40,50'
nums = read_numbers(sample)
print('Numbers:', nums)
report = stats(nums)
print('Stats:', report)

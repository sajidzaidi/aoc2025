with open('input.txt', 'r') as f:
    top_section, bottom_section = f.read().split('\n\n')

    intervals = top_section.splitlines()
    
    ingredients = bottom_section.splitlines()


parsed_intervals = []

for interval in intervals:
    lower, upper = map(int, interval.split("-"))
    parsed_intervals.append((lower, upper))

# Check if a number is in any interval
def is_in_any_interval(number, intervals):
    return any(lower <= number <= upper for lower, upper in intervals)

print(sum( is_in_any_interval(int(x),parsed_intervals) for x in ingredients))

merged_intervals=[]
parsed_intervals.sort()
for lower, upper in parsed_intervals:
    if merged_intervals and lower <= merged_intervals[-1][1]:
            merged_intervals[-1][1]=max(merged_intervals[-1][1],upper)
    else:
        merged_intervals.append([lower,upper])
    
print(sum(x[1]-x[0]+1 for x in merged_intervals) )
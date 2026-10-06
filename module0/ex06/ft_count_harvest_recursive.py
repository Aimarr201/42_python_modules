
def ft_count_harvest_recursive(days=None, i=1):
    if (days is None):
        days = int(input("Days until harvest: "))
    print(f"Day {i}")
    if (i < days):
        ft_count_harvest_recursive(days, i=i + 1)
    else:
        print("Harvest time!")

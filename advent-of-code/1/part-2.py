"""
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They
offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
--------
I believe this is "three sum".

Dumb n^2 approach:
    - inputs = read_input_set()
    - comps_1 = {item: 2020-item for item in inputs}
    - for each item in inputs:
        for each key, value in comps_1:
            if key != item && value - item in inputs:
                return key * item * (value-item)

Another dumb n^2 approach:
    - inputs = read_input_set()
    - comps_1 = {item: 2020-item for item in inputs}
    - comps_2 = {subtract each item in input from each value in comps_1 if item != key}
    - Third value is intersection of comps_2 with input

Seems like we have to make a first list of compliments and then do 2sum on that.
"""

def three_sum(numbers):
    comp_1 = {item: 2020-item for item in numbers}
    comp_2 = set()
    for key, value in comp_1.items():
        for num in numbers:
            if key != num and value - num in numbers:
                print(f"Numbers: {[key, num, value-num]}")
                return(key * num * (value-num))

def main():
    numbers = set(int(val) for val in open('input.txt', 'r').read().split('\n') if val)
    print(three_sum(numbers))


if __name__ == '__main__':
    main()    
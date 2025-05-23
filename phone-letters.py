phone_dic = {
   '2': ['a', 'b', 'c'],
   '3': ['d', 'e', 'f'],
   '4': ['g', 'h', 'i'],
   '5': ['j', 'k', 'l'],     
   '6': ['m', 'n', 'o'],
   '7': ['p', 'q', 'r', 's'],
   '8': ['t', 'u', 'v'],
   '9': ['w', 'x', 'y', 'z']
}


def letter_combinations(digits):
    if not digits:
        return []

    result = []

    def backtrack(combination, next_digits):
        print('in backtrack method:', next_digits)
        if not next_digits:
            result.append(combination)
            return
        for letter in phone_dic[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])

    backtrack("", digits)
    return result


print(letter_combinations("23"))
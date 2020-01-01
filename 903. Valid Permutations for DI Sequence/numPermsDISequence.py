def process_perm(S, combinations, processed):
    new_processed_combinations = []
    increasing = 1
    if S[processed] == "D":
        increasing = 0

    num_seq = range(0, len(S) + 1)
    for valid_combination in combinations:
        # find leftover numbers
        bank = [num for num in num_seq if num not in valid_combination]

        # find the right "half" of leftover numbers
        cutoff_num = valid_combination[-1]


        possible_nums = []
        for num in bank:
            if increasing == 1 and num > cutoff_num:
                possible_nums.append(num)
            elif increasing == 0 and num < cutoff_num:
                possible_nums.append(num)

        # add char to combinations,
        for num in possible_nums:
            new_perm = list(valid_combination)
            new_perm.append(num)
            new_processed_combinations.append(new_perm)

    return new_processed_combinations

class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        num_seq = range(0, len(S) + 1)
        num_seq_list = []
        for num in num_seq:
            temp = []
            temp.append(num)
            num_seq_list.append(temp)
        # [[0], [1], [2], [3]]


        return_valid_perm = 0
        for i in range(0, len(S)):
            num_seq_list = process_perm(S, num_seq_list, i)
            # print(num_seq_list)






        return len(num_seq_list)

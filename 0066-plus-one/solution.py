class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tem_list = digits[::-1]
        n = len(tem_list)
        l = []
        next_check = tem_list[0]
        index = 0

        if tem_list[0] < 9:
            tem_list = [tem_list[0] + 1] + tem_list[1:]

        elif tem_list[0] == 9:
            while next_check == 9:
                l.append(0)
                index += 1
                if index <= n-1:
                    next_check = tem_list[index]
                elif index == n:
                    next_check = 1

            if index == n:
                l.append(1)
                tem_list = l
            elif index == n-1:
                tem_list = l + [tem_list[index]+1]
            elif index < n-1:
                tem_list = l + [tem_list[index]+1] + tem_list[index+1:]


        return tem_list[::-1]

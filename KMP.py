class KMP:
    def get_next_val_arr(self, pattern_string):
        next_val_arr = [0] * (pattern_string[0] + 1)
        i, j = 1, 0
        while i < pattern_string[0]:
            # pattern_string[i]表示后缀字母
            # pattern_string[j]表示前缀字母
            if j == 0 or pattern_string[i] == pattern_string[j]:
                i += 1
                j += 1
                if pattern_string[i] != pattern_string[j]:
                    next_val_arr[i] = j
                else:
                    next_val_arr[i] = next_val_arr[j]
            else:
                j = next_val_arr[j]
        return next_val_arr

    def kmp(self, primary_string, pattern_string):
        # 作字符串处理，第一位填放字符串长度
        primary_string_length = len(primary_string)
        primary_string = [primary_string_length] + list(primary_string)
        pattern_string_length = len(pattern_string)
        pattern_string = [pattern_string_length] + list(pattern_string)

        # 得到next_val_arr数据
        next_val_arr = self.get_next_val_arr(pattern_string)

        i, j = 1, 1
        while i <= primary_string[0] and j <= pattern_string[0]:
            if j == 0 or primary_string[i] == pattern_string[j]:
                i += 1
                j += 1
            else:
                j = next_val_arr[j]
        if j > pattern_string[0]:
            return i - pattern_string[0] - 1
        else:
            return -1


if __name__ == '__main__':
    kmp = KMP()
    print(kmp.kmp('abcdabcdabcfe', 'abcdabcf'))




class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        binary_str = str(binary)
        binary_list = list(binary_str[2:])
        binary_list.reverse()
        binary_list.extend(['0'] * (32 - len(binary_list)))
        binary_str_reversed = "".join(binary_list)
        return int(binary_str_reversed, 2)
        

        
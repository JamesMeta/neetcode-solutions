class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            first_str = strs[0]
            second_str = strs[1]

            common_prefixes = []

            for i in range(len(first_str) + 1):

                back_prefix = first_str[:i]

                if (second_str.startswith(back_prefix)):
                    common_prefixes.append(back_prefix)

            if len(common_prefixes) == 0:
                return ''

            elif len(strs) == 2:
                return max(common_prefixes)
            
            else: 
                for word in strs[2:]:

                    common_prefixes_copy = common_prefixes.copy()

                    for prefix in common_prefixes_copy:
                        if not word.startswith(prefix):
                            common_prefixes.remove(prefix)
                
                if len(common_prefixes) == 0:
                    return ''

                else:
                    return max(common_prefixes)

            



            

                



        
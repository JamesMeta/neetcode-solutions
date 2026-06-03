class Solution:
    def reverse(self, x: int) -> int:
        maximum_value_first_half = 21474
        maximum_value_last_half = 83647
        minimum_value_first_half = 21474
        minimum_value_last_half = 83648

        x_str = str(x)

        x_list = list(x_str)
          
        if x > 0:

            x_list.reverse()
            x_str_reversed = ''.join(x_list)  

            if len(x_str_reversed) >= 10 and int(x_str_reversed[0]) >= 2:
                median = len(x_str_reversed) // 2
                x_str_first_half = int(x_str_reversed[:median])
                x_str_last_half = int(x_str_reversed[median:])

                if x_str_first_half > maximum_value_first_half or (x_str_first_half == maximum_value_first_half and x_str_last_half > maximum_value_last_half) :
                    return 0
            
            return int(x_str_reversed)

        if x < 0:

            x_list.pop(0)
            x_list.reverse()
            x_str_reversed = ''.join(x_list)  

            if len(x_str_reversed) >= 10 and int(x_str_reversed[0]) >= 2:
                median = len(x_str_reversed) // 2
                x_str_first_half = int(x_str_reversed[:median])
                x_str_last_half = int(x_str_reversed[median:])

                if x_str_first_half > minimum_value_first_half or (x_str_first_half == minimum_value_first_half and x_str_last_half > minimum_value_last_half) :
                    return 0
            
            return int(x_str_reversed) * -1 
        else:
            return 0
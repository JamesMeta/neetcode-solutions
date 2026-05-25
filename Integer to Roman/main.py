class Solution:
    def intToRoman(self, num: int) -> str:

        convert_dict = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }

        roman_string = ""
        while num > 0:
            if num >= 1000:
                roman_string += convert_dict[1000]
                num -= 1000
            
            elif num >= 900:
                roman_string += convert_dict[100] + convert_dict[1000]
                num -= 900
            
            elif num >= 500:
                roman_string += convert_dict[500]
                num -= 500
            
            elif num >= 400:
                roman_string += convert_dict[100] + convert_dict[500]
                num -= 400
            
            elif num >= 100:
                roman_string += convert_dict[100]
                num -= 100
            
            elif num >= 90:
                roman_string += convert_dict[10] + convert_dict[100]
                num -= 90
            
            elif num >= 50:
                roman_string += convert_dict[50]
                num -= 50
            
            elif num >= 40:
                roman_string += convert_dict[10] + convert_dict[50]
                num -= 40
            
            elif num >= 10:
                roman_string += convert_dict[10]
                num -= 10
            
            elif num >= 9:
                roman_string += convert_dict[1] + convert_dict[10]
                num -= 9
            
            elif num >= 5:
                roman_string += convert_dict[5]
                num -= 5
            
            elif num >= 4:
                roman_string += convert_dict[1] + convert_dict[5]
                num -= 4
            
            else:
                roman_string += convert_dict[1]
                num -= 1

        return roman_string
        
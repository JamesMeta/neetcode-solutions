from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        position_speed = list(zip(position, speed))
        position_speed.sort(reverse=True, key=lambda x: x[0])

        POSITION = 0
        SPEED = 1

        required_hours = 0
        car_fleets = 0

        for i, car_position_speed in enumerate(position_speed):
            hours = ((target - car_position_speed[POSITION]) / car_position_speed[SPEED])
            
            if hours <= required_hours:
                pass
            else:
                car_fleets += 1
                required_hours = hours
            
        return (car_fleets)





        
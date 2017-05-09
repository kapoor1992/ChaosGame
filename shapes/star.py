import math
from shape import Shape

class Star(Shape):
    total_vertices = 10
    
    def vertices(self):
        gold_rat = (math.sqrt(5) + 1) / 2
        
        top_y = 50 + ((100 * gold_rat) * math.sin(math.radians(72)))
        bot_y = 50 - (50/math.tan(math.radians(18)))
        right_x = 100 + math.sin(math.radians(24))
        right_y = 50 - (100 + math.cos(math.radians(24)))
        right_tip_x = 50 + (100 * gold_rat)
        left_tip_x = -50 - (100 * gold_rat)
        left_x = -50 - (100 * math.sin(math.radians(24)))
        left_y = right_y
        right_bot_tip_x = (100 * gold_rat) * (math.sin(math.radians(54)))
        right_bot_tip_y = bot_y - ((100 * gold_rat) * (math.cos(math.radians(54))))
        left_bot_tip_x = -right_bot_tip_x
        left_bot_tip_y = right_bot_tip_y

        self.vertex0 = [-50, 50]
        self.vertex1 = [0, top_y]
        self.vertex2 = [50, 50]
        self.vertex3 = [right_tip_x, 50]
        self.vertex4 = [right_x, right_y]
        self.vertex5 = [right_bot_tip_x, right_bot_tip_y]
        self.vertex6 = [0, bot_y]
        self.vertex7 = [left_bot_tip_x, left_bot_tip_y]
        self.vertex8 = [left_x, left_y]
        self.vertex9 = [left_tip_x, 50]

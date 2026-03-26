"""
Applications-
- Udemy have differnet courses
- there are different groups of courses 
but have some similarities
- Then we can use factory design pattern

prons-
- decouppled code with main
- easiy to update code

"""

class Pizza:
    def prepare(self):
        raise NotImplementedError("this should be overridden by subclass")

class ChessePizza(Pizza):
    def prepare(self):
        return "Preparing cheese pizza"
        
class VeggiePizza(Pizza):
    def prepare(self):
        return "Preparing Viggie pizza"
        
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type=='cheese':
            return ChessePizza()
        elif pizza_type=='veggie':
            return VeggiePizza()
        else:
            raise ValueError (f"unknown piza type: {pizza_type}")
        
def main():
    try:
        user_input="cheese"
        pizza=PizzaFactory.create_pizza(user_input)
        print(pizza.prepare())
    except ValueError as e:
        print(e)


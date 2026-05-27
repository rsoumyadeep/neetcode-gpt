class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        

        x_odd=init
        

        def derivative(x):
            return 2*x

        for t in range(iterations):

            x_new=x_odd - learning_rate*derivative(x_odd)
            x_odd=x_new

        return round(x_odd,5)

        




from typing import List
def average(salary: List[int]) -> float:
        n = len(salary)
        mini = min(salary)
        maxi = max(salary)
        return (sum(salary) - mini - maxi) / (n - 2)
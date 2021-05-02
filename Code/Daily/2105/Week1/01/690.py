from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        all_employees = {employee.id: employee for employee in employees}

        def dfs(employee_id):
            employee = all_employees[employee_id]

            return employee.importance + sum(dfs(employee_subemp_id) for employee_subemp_id in employee.subordinates)

        return dfs(id)

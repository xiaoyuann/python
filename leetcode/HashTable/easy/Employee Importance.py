"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d={employee.id:employee for employee in employees}
        sumImportance=0
        temp=[d[id]]
        while temp:
            top=temp.pop()
            sumImportance+=top.importance
            for n in top.subordinates:
                temp.append(d[n])
        return sumImportance
        
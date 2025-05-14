#7. Access Modifiers: Public, Private, and Protected: Create a class Employee with: a public variable name, a protected variable _salary, and a private variable __ssn. Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable



emp1 = Employee("Ali", 50000, "123-45-6789")

print("Name (Public):", emp1.name)          # ✅ Works
print("Salary (Protected):", emp1._salary)  # ✅ Technically works (but not recommended)
# print("SSN (Private):", emp1.__ssn)       ❌ Error: private attribute
print("SSN (Private):", emp1._Employee__ssn) # ✅ Name mangling trick


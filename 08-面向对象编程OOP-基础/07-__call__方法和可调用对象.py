# Files: 
# Author：jiang liu
# Date ：2020/3/25 13:33
# Tool ：PyCharm


# 定义了__call__方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用。
class SalaryAccount:
    """ 工资计算类 """

    def __call__(self, salary):
        print("算工资啦...")
        yearSalary = salary * 12
        daySalary = salary // 22.5
        hoursSalary = daySalary // 8

        return dict(yearSalary=yearSalary,
                    monthSalary=salary, daySalary=daySalary, hoursSalary=hoursSalary)


s = SalaryAccount()
print(s(20000))

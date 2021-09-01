import logging

_LOGGER = logging.getLogger(__name__)


class _PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommisionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9),
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError("wrong employee id %s", employee_id)
        return policy

    def calcalate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            if employee.address:
                print("- Sent to:")
                print(employee.address)
            print("")


def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    _payroll_system.calcalate_payroll(employees)


class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class LTDPolicy:
    def __init__(self):
        self._base_policy=None

    def track_work(self,hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payrol()
        return base_salary * 0.6

    def apply_to_policy(self,base_policy):
        self._base_policy=base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError("Base policy missing.")

class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommisionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commision_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commision_per_sale

    @property
    def commision(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calcalate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision


_payroll_system = _PayrollSystem()

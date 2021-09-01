import logging

_LOGGER = logging.getLogger(__name__)

from .hr import calculate_payroll
from .productivity import track
from .employees import employee_database,Employee

employees = employee_database.employees

track(employees,40)
calculate_payroll(employees)

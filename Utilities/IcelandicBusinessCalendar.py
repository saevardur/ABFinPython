from pandas.tseries.holiday import Holiday, AbstractHolidayCalendar, nearest_workday, MO


class IcelandicCalendar(AbstractHolidayCalendar):
    rules = [Holiday('N��rsdagur', month=1,  day=1),
             Holiday('Sumardagurinn fyrst', month=4, day=18,offset=DateOffset(weekday=TH(1))),
             Holiday('1. ma�', month=5, day=1),
             Holiday('17. j�n�', month=6, day=17),
             Holiday('Fr�dagur verslunarmanna', month=8, day=1,offset=DateOffset(weekday=MO(1))),
             Holiday('J�ladagur', month=12, day=25),
             Holiday('Annar � j�lum', month=12, day=26)]

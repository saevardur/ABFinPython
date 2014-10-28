from pandas.tseries.holiday import Holiday, AbstractHolidayCalendar, nearest_workday, MO


class IcelandicCalendar(AbstractHolidayCalendar):
    rules = [Holiday('Nýársdagur', month=1,  day=1),
             Holiday('Sumardagurinn fyrst', month=4, day=18,offset=DateOffset(weekday=TH(1))),
             Holiday('1. maí', month=5, day=1),
             Holiday('17. júní', month=6, day=17),
             Holiday('Frídagur verslunarmanna', month=8, day=1,offset=DateOffset(weekday=MO(1))),
             Holiday('Jóladagur', month=12, day=25),
             Holiday('Annar í jólum', month=12, day=26)]

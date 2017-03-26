# testing ground for code snippets
import datetime
def get_date_from_nbp_format(date_str_nbp):
    year = int(date_str_nbp[:4])
    month = int(date_str_nbp[4:6])
    day = int(date_str_nbp[6:])
    print(datetime.date(year, month, day))

get_date_from_nbp_format('20150430')
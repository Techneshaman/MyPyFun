import pandas
import datetime
import numpy
import matplotlib.pyplot as plotter

year_numbers = [2012, 2013, 2014, 2015, 2016, 2017]
file_paths = []

for year_number in year_numbers:
    file_path = '/Users/michalwitkowski/PyWorkspace/MyPyFun/exchange_rates_pln/archiwum_tab_a_{year}.csv'\
                                                                                       .format(year=year_number)
    file_paths.append(file_path)

exchange_rates_pandas = pandas.DataFrame()

for file_path in file_paths:
    pandas_df = pandas.read_csv(file_path, sep=';')
    exchange_rates_pandas = pandas.concat([exchange_rates_pandas, pandas_df], ignore_index=True)

CURRENCY_LIST = list(exchange_rates_pandas)
CURRENCY_LIST.remove('data')
print(CURRENCY_LIST)


def get_date_from_nbp_format(date_str_nbp):
    year = int(str(date_str_nbp)[:4])
    month = int(str(date_str_nbp)[4:6])
    day = int(str(date_str_nbp)[6:])
    return datetime.date(year, month, day)

exchange_rates_pandas['date'] = exchange_rates_pandas['data'].apply(get_date_from_nbp_format)
exchange_rates_pandas = exchange_rates_pandas.drop('data', 1)


def get_float_from_nbp_str(nbp_exchange_rate_str):
    if isinstance(nbp_exchange_rate_str, str):
        new_str = nbp_exchange_rate_str.replace(',', '.')
        output_float = float(new_str)
        return output_float
    else:
        return numpy.NaN

for currency in CURRENCY_LIST:
    exchange_rates_pandas[currency] = exchange_rates_pandas[currency].apply(get_float_from_nbp_str)

print(exchange_rates_pandas)

plotter.figure()
plotter.plot(exchange_rates_pandas['date'], exchange_rates_pandas[['1AUD', '1EUR', '1CHF', '1USD']])
plotter.legend(['1AUD', '1EUR', '1CHF', '1USD'], loc='lower right')
plotter.show()

import mplfinance
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
from mpl_finance import candlestick_ohlc

acao2 = 'RSID3'

df_bolsa = mplfinance.get_stock_historical_data(stock=acao2,
                                          country='brazil',
                                          from_date='01/01/2010',
                                          to_date='02/07/2020')

df_bolsa.index.names = ['Data']
df_bolsa.columns = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Volume', 'Moeda']

df_ = df_bolsa.copy(deep=True)

df_['Data'] = df_.index.map(mdates.date2num)

# compute the simple moving average
df_['ema21'] = df_['Fechamento'].ewm(span=21, adjust=False).mean()

print(df_)

tendencia_alta=1
for i in range(6):
  if(df_.ema21[-i-1] < df_.ema21[-i-2]):
    tendencia_alta=0

print()
if(tendencia_alta==1):
    print(acao2 + ' está em tendência de alta!')
else:
    print(acao2 + ' não está em tendência de alta!')
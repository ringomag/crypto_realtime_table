Django aplication with cryptocurrency data which is updated for every 10 secconds(Celery).
In this app is used Redis for channel_layer, and websocket/channels for asynchronous data send to frontend.

GECKO's API url:
'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'

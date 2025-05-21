#2
stock_dic ={
    'info':	[600,630,620],
'ril':	[1430,1490,1567],
'mtl':	[234,180,160],
} 

inputs = input("Enter one input value from (print, add): ")

if inputs == 'print':
    for k,v in stock_dic.items():
        total = 0
        for item in v:
            total = total + item
        avg = total/len(v)
        print(k,"==>",v,'==>',round(avg,2))
elif inputs == 'add':
    ticker = input("Enter stock ticker: ")
    price = float(input("Enter price: "))
    if ticker in stock_dic:
        stock_dic[ticker].append(price)
    else:
        stock_dic[ticker] = [price]
    print(f"{ticker} updated to: {stock_dic[ticker]}")
import matplotlib as plt
import random
import math
import networkx as nx

coins = ["ADA","ALGO","ANKR","APE","ATOM","AVAX","AXS","BCH","BNB","BTC","BTG","CAKE","CELO",
    "CHZ","COMP","CRO","CTSI","DOGE","DOT","EOS","ETC","ETH","FIL","FTM","GALA","GRT","ICP","IOST",
    "KCS", "LUNA","LTC","MANA","MATIC","MKR","NEO","OMG","ONE","ONT","OXT","PAXG","QTUM","REN","SAND","SNX","SOL",
    "STORJ","SUSHI","THETA","TRX","UNI","USDC","USDT","VET","XLM","XMR","XRP","YFI","ZIL",]

graph = nx.complete_graph(coins) # Makes a Complete Graph

def find_unique_combinations(lst):# finds all unique 2 element combinations in a list
    unique_combinations = set()

    if len(lst) < 2:
        return unique_combinations

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            combination = tuple(sorted([lst[i], lst[j]]))
            unique_combinations.add(combination)

    return list(unique_combinations)

combo_list = find_unique_combinations(coins)

for u, v in graph.edges:
    # Generate a random value for the edge weight (you can adjust the range as needed)
    random_weight = random.uniform(0.1, 1.0)
    
    # Assign the random value as an attribute to the edge
    graph[u][v]['Exchange Rate'] = random_weight
    
def arbitrage_finder(graph, combo_list, limit): #Locates Arbitrage Opprotunites 
    count = 0
    while limit > count:
        bellman_ford_path = nx.bellman_ford_path(graph, combo_list[0], combo_list[1], weight='Exchange Rates')
        if bellman_ford_path != nx.get_edge_attributes(graph, (combo_list[0],combo_list[1])):
            print("Trading Opprotunity Found")
        count =+ 1
            


        



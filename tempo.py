# from collections import Counter

# a = ['2 4 2', '2 3 3', '3 45 6', '5 5 65']
# threshold = 2

# def func(a, threshold):
    
#     re, result = [], []
#     count = 0 
#     for j in a:
#         j = j.split()
#         j = [int(i) for i in j]
#         j = list(set(j) )
#         re += j
#     counts = Counter(re)
#     result = [d for d in re if counts[d] >= threshold]
#     print(list(set(result) ))

# func(a, threshold)

# from core.models import Team

# teamss = Team.objects.all().values()

# print(teamss)


# dictionary = {'id': {6: 7, 0: 3, 1: 4, 2: 5, 8: 9, 4: 1, 7: 8, 5: 2, 3: 6},
#  'name': {6: 'Manchester City', 0: 'Arsenal', 1: 'Brighton Have Albion', 2: 'Fulham F.C.', 8: 'Tottenham', 4: 'Liverpool', 7: 'Manchester United', 5: 'Chelsea', 3: 'Everton'},
#   'games': {6: 6, 0: 6, 1: 6, 2: 6, 8: 6, 4: 6, 7: 6, 5: 6, 3: 6},
#    'win': {6: 5, 0: 5, 1: 4, 2: 3, 8: 3, 4: 2, 7: 2, 5: 2, 3: 1},
#  'draw': {6: 1, 0: 0, 1: 0, 2: 2, 8: 2, 4: 3, 7: 2, 5: 2, 3: 3}, 
#  'loss': {6: 0, 0: 1, 1: 2, 2: 1, 8: 1, 4: 1, 7: 2, 5: 2, 3: 2},
#   'scored': {6: 22, 0: 15, 1: 12, 2: 12, 8: 12, 4: 13, 7: 12, 5: 12, 3: 12},
#  'conceded': {6: 2, 0: 6, 1: 10, 2: 10, 8: 10, 4: 5, 7: 12, 5: 10, 3: 12},
#   'league_id': {6: 1, 0: 1, 1: 1, 2: 1, 8: 1, 4: 1, 7: 1, 5: 1, 3: 1},
#    'points': {6: 16, 0: 15, 1: 12, 2: 11, 8: 11, 4: 9, 7: 8, 5: 8, 3: 6},
#  'average': {6: 24, 0: 21, 1: 22, 2: 22, 8: 22, 4: 18, 
# 7: 24, 5: 22, 3: 24}}
# # print(dictionary)
# for key, value in dictionary.items():
#     print("this is the key  ", key)
#     for k, v in value.items():
#         print(v)



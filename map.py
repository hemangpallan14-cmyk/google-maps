cities=['a','b','c','d','e']
roads={
       ('a','b'),
       ('b','c'),
       ('c','a'),
       ('d','e'),
       ('e','a'),
       ('c','d'),
       }
matrix=[0*len(cities) for_in range (len(cities))]
for i in range (len(cities)):
    for j in range (len(cities)):
        if (cities[i],cities[j]) in roads:
            matrix[i][j]==1
        else:
            matrix[i][j]==0    



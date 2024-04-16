#LAB 4

#Q1.
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_benefit = 0
    knapsack = []
    for benefit, weight in items:
        if weight <= capacity:
            total_benefit += benefit
            knapsack.append((benefit, weight))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_benefit += fraction * benefit
            knapsack.append((benefit * fraction, weight * fraction))
            break  

    return total_benefit, knapsack
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50  
total_benefit, knapsack = fractional_knapsack(items, capacity)
print("Optimal solution:")
print("Total benefit:", total_benefit)
print("Selected items:")
for item in knapsack:
    print("Benefit:", item[0], ", Weight:", item[1])


#Q2.
arr1=[0,2,3,4,5]
temp=[]
for i in range(0,len(arr1)):
    a=arr1[i]*i
    temp.append(a)
sum=0
for j in range(0,len(temp)):
    sum+=temp[j]
print(temp)
print(sum)

#Q3.
arr1=[7,5,1,4]
arr2=[6,17,9,3]
a=sorted(arr1)
b=sorted(arr2, reverse=True)
sum=0
if len(a)==len(b):
    for i in range(0,len(a)):
        sum+=(a[i]*b[i])
print(a)
print(b)
print(sum)

#LAB 5

#Q1.
def min_candies(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)
ratings = [4, 6, 4, 5, 6, 2]

min_candies_needed = min_candies(ratings)
print("Minimum number of candies needed:", min_candies_needed)

#Q3.
def min_power_plants(n, k, cities):
    power_plants = 0
    i = 0

    while i < n:
        j = i + k - 1 
        while j >= i - k + 1 and (j >= 0 and cities[j] == '0'):
            j -= 1

        if j < i - k + 1:  
            return -1

        power_plants += 1
        i = j + k  

    return power_plants

n = 6
k = 2
cities = "101010"

result = min_power_plants(n, k, cities)
print("Lowest number of power plants needed:", result)

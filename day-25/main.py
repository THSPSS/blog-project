# with open("weather_data.csv") as weather_info:
     # data = weather_info.readlines()

# import csv
#
# with open("weather_data.csv") as weather_info:
#     data = csv.reader(weather_info)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp": #if row[1] != "temp'
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()

#total = 0
#num = 0
#for temp in temp_list:
#    total += temp
#    num += 1
#temp_avg = total/num
#print(round(temp_avg))


#avg_temp = sum(temp_list)/len(temp_list)
#print(avg_temp)

#print(data["temp"].mean())
#print(data["temp"].max())


#Get Data in columns
#print(data["condition"])
#print(data.condition)

#Get Data in rows
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
print(monday.condition)
#
# mon_temp = int(monday.temp)
# mon_temp_f = mon_temp * 1.8 + 32
# print(mon_temp_f)
#
#
#
# #create dataframe from scratch
# data_dict = {
#     "students" : ["Amy","James","Chloe"],
#     "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#TODO count Squirrels Color


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_suqirrel = len(data[data["Primary Fur Color"] == "Black"])


squirrel_dict = {
    "fur color" : ["grey","red","black"],
    "counting" : [grey_squirrel,red_squirrel,black_suqirrel],
}

squirrel_color = pandas.DataFrame(squirrel_dict)
squirrel_color.to_csv("squirrel_count.csv")


# counting=[]
# fur_color = ["grey","red","black"]
# grey =0
# red = 0
# black = 0
# fur_col = data["Primary Fur Color"]
# for col in fur_col:
#     if col == "Gray":
#         grey+=1
#     elif col == "Cinnamon":
#         red += 1
#     elif col == "Black":
#         black += 1
#
# counting.append(grey)
# counting.append(red)
# counting.append(black)
#
# print(counting)
# print(fur_color)
# a_dict = {}
# a_dict["Fur color"] = fur_color
# a_dict["counting"] = counting
#
# print(a_dict)
#
# squirrel_fur_count = pandas.DataFrame([a_dict])
# squirrel_fur_count.to_csv("squirrel_count.csv")

#print(raw_data)

#fur_col_list = data["Primary Fur Color"].to_list()
#print(fur_col_list)



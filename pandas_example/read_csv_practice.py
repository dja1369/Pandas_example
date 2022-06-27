with open('./pandas_example/csv_files/weather_data.csv', 'r') as csv:
    # data = []
    # for line in csv.readlines():
    #     data.append(line.strip()) # 판다스 처럼 출력
    data = csv.readlines() # 간단하게 출력
    
print('normal readMethod')        
print(data)
print()

import csv

with open('./pandas_example/csv_files/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    print(data) # csv오브젝트 생성됨 이는 iterable(반복가능) 하다
    print('using csv library')
    temperatures = [] 
    for row in data:
        print(row)
        row[1] # 온도만 출력 
        if row[1] != 'temp': #temp 라벨 제거 
            temperatures.append(int(row[1])) # 온도 리스트에 추가
    
    print(temperatures) # 온도를 저장한 리스트 
    print()
    
import pandas as pd

print('using pandas')            
data = pd.read_csv('./pandas_example/csv_files/weather_data.csv')
print(data)
print()
print(data['temp']) # 원하는 열만 출력도 가능, 라벨, 데이터 타입 출력.

data_dict = data.to_dict()
print(data_dict) # 사전형으로 변환

temp_list = data['temp'].to_list()
print(temp_list) # 리스트로 변환

# 온도 평균값 구하기 
# 1. sum 함수 이용 
print()
ret = sum(temp_list)
ret = ret / len(temp_list)
print(ret)
ret = 0 # 초기화
print()

# 2. numpy 이용
import numpy
ret = numpy.mean(temp_list)
print(ret)

# 3. 판다스 자체 함수 이용 
print()
print(data['temp'].mean()) 

# 온도중 최고값 출력 
print()
print(data['temp'].max()) 

# 데이터 에서 컬럼 가져오기
# data['temp'] or data.temp

# 데이터 에서 열 가져오기
# data[data['temp']] or data[data.temp] 
# data[data['temp'] == 'Monday']

# 데이터 에서 가장 높은 온도를 가진 행 찾기 
print(data[data.temp == data['temp'].max()])

monday = data[data.day == 'Monday']
print(monday.condition)

mondey_temp = monday.temp
# 온도를 화씨로 변경
monday_temp_F = monday.temp * 9/5 + 32
print(monday_temp_F)


# Csv 파일 만들기 
student_dict = {
    'student' : ['Lee', 'Kim', 'Joe'],
    'scores' : [80, 65, 38]
}

student_pd = pd.DataFrame(student_dict)
print(student_pd)
student_pd.to_csv("./pandas_example/csv_files/student_data.csv")
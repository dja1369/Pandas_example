import pandas as pd

# 뉴욕 센트럴 파크 다람쥐들을 색깔별로 몇마리 있는지 정제
data = pd.read_csv('pandas_example/csv_files/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv')

print(data['Primary Fur Color'])

gray_squirrels = data[data['Primary Fur Color'] == 'Gray'] # 털색이 회색인 모든 다람쥐 행 출력 
gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray']) # 판다스의 series는 반복취급이 가능하여 길이가 나온다
print(gray_squirrels)

black_squirrels = data[data['Primary Fur Color'] == 'Black'] # 털색이 검정색인 모든 다람쥐 행 추출 
black_squirrels = len(data[data['Primary Fur Color'] == 'Black']) # 길이는 행의 모든갯수이기에 행마다 1마리 씩 있으므로 Count를 하면 검정털을 가진 다람쥐 숫자가 나온다.
print(black_squirrels)

cinnamon_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
cinnamon_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print(cinnamon_squirrels)

data_dict = { # CSV로 변경을 위해 사전형으로 데이터 삽입.
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [gray_squirrels, black_squirrels, cinnamon_squirrels]
}

replace_data = pd.DataFrame(data_dict)

print(replace_data)

replace_data.to_csv('pandas_example/csv_files/Central_Park_Squirrel_Count.csv') # CSV파일 생성.
import pandas as pd

# 建立 DataFrame
data = {
    '姓名': ['小明', '小華', '小美'],
    '年齡': [20, 21, 19],
    '成績': [85, 92, 78]
}
df = pd.DataFrame(data)

# 基本操作
print(df.head())  # 顯示前幾筆資料
print(df.describe())  # 統計摘要
print(df['成績'].mean())  # 平均成績

# 讀取 CSV 檔案
# df = pd.read_csv('data.csv')

# 資料篩選
high_scores = df[df['成績'] > 80]
print(high_scores)

# 資料排序
sorted_df = df.sort_values('成績', ascending=False)
print(sorted_df)

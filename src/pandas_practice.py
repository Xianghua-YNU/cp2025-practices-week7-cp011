import pandas as pd
import matplotlib.pyplot as plt

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    
    该函数创建一个包含学生姓名、年龄、成绩和所在城市的数据框架，
    并将其保存为UTF-8编码的CSV文件。
    
    Returns:
        None
    """
    # 学生需要在此处实现代码
    

def load_data():
    """任务1: 读取数据文件"""
    # 学生需要在此处实现代码
    data = pd.read_csv('data.csv')  # 假设数据文件名为 data.csv
    print("读取的数据：")
    print(data)

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    # 学生需要在此处实现代码
    print("\n数据基本信息：")
    print(data.info())
    print("\n数据描述统计：")
    print(data.describe())

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    # 学生需要在此处实现代码
    print("\n缺失值情况：")
    print(data.isnull().sum())

# 填充缺失值
    data_filled = data.fillna(data.mean())  # 用均值填充
    print("\n处理后缺失值情况：")
    print(data_filled.isnull().sum())

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    # 学生需要在此处实现代码
    mean_value = data['column_name'].mean()  # 替换 'column_name' 为实际列名
    median_value = data['column_name'].median()
    std_dev = data['column_name'].std()

    print(f"\n列 'column_name' 的均值：{mean_value}")
    print(f"列 'column_name' 的中位数：{median_value}")
    print(f"列 'column_name' 的标准差：{std_dev}")

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    # 学生需要在此处实现代码
    data['column_name'].hist()
    plt.title('直方图')
    plt.xlabel('column_name')
    plt.ylabel('Frequency')
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    # 学生需要在此处实现代码
    data_filled.to_csv('processed_data.csv', index=False)
    print("\n保存的文件路径和文件名：processed_data.csv")

# 总结
    print("\n总结：")
    print("本次实验通过 Pandas 库完成了数据的读取、查看、处理缺失值、统计分析、可视化和保存。")

def main():
    """主函数，执行所有数据处理流程"""
    # 学生需要在此处组织代码流程
    pass

if __name__ == "__main__":
    main()

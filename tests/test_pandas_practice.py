import pandas as pd
import matplotlib.pyplot as plt

def create_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    该函数创建一个包含学生姓名、年龄、成绩和所在城市的数据框架，
    并将其保存为UTF-8编码的csv文件。
    """

    df = pd.DataFrame(data)
    df.to_csv('students.csv', index=False, encoding='utf-8')

def load_data():
    """任务1：读取数据文件"""
    data = pd.read_csv('students.csv', encoding='utf-8')
    return data

def show_basic_info(data):
    """任务2：显示数据基本信息"""
    print("基本信息：")
    print(data.info())
    print("\n描述性统计：")
    print(data.describe())

def handle_missing_values(data):
    """任务3：处理缺失值"""
    # 找到缺失值列
    missing_values = data.isnull().sum()
    print("缺失值情况：")
    print(missing_values)
    # 填充缺失值
    data['成绩'].fillna(data['成绩'].mean(), inplace=True)
    return data

def analyze_statistics(data):
    """任务4：统计分析数值列"""
    mean_score = data['成绩'].mean()
    median_score = data['成绩'].median()
    std_dev_score = data['成绩'].std()
    print(f"成绩均值：{mean_score}")
    print(f"成绩中位数：{median_score}")
    print(f"成绩标准差：{std_dev_score}")

def visualize_data(data, column_name='成绩'):
    """任务5：数据可视化"""
    plt.figure(figsize=(10, 6))
    plt.hist(data[column_name], bins=5, color='blue', alpha=0.7)
    plt.title(f'{column_name} 分布')
    plt.xlabel(column_name)
    plt.ylabel('频率')
    plt.grid(True)
    plt.show()

def save_processed_data(data):
    """任务6：保存处理后的数据"""
    data.to_csv('processed_students.csv', index=False, encoding='utf-8')
    print("处理后的数据已保存到 processed_students.csv")

def main():
    """主函数，执行所有数据处理流程"""
    create_frame()
    data = load_data()
    show_basic_info(data)
    data = handle_missing_values(data)
    analyze_statistics(data)
    visualize_data(data)
    save_processed_data(data)

if __name__ == "__main__":
    main()

    

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
     data = {
        '姓名': ['张三', '李四', '王五', '赵六'],
        '年龄': [20, 21, 22, 23],
        '成绩': [85, 90, None, 88],
        '城市': ['北京', '上海', '广州', '深圳']
    }
    df = pd.DataFrame(data)
    df.to_csv('students.csv', encoding='utf-8', index=False)

def load_data():
    """任务1: 读取数据文件"""
    # 学生需要在此处实现代码
   data = pd.read_csv('students.csv')
    return data

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    # 学生需要在此处实现代码
    print("数据基本信息:")
    print(data.info())
    print("\n数据摘要:")
    print(data.describe())

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    # 学生需要在此处实现代码
   data['成绩'].fillna(data['成绩'].mean(), inplace=True)
    print("处理后缺失值情况:")
    print(data)

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    # 学生需要在此处实现代码
   

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    # 学生需要在此处实现代码
    mean_score = data['成绩'].mean()
    median_score = data['成绩'].median()
    std_score = data['成绩'].std()
    print(f"成绩均值: {mean_score}")
    print(f"成绩中位数: {median_score}")
    print(f"成绩标准差: {std_score}")

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    # 学生需要在此处实现代码
    data.to_csv('processed_students.csv', encoding='utf-8', index=False)
    print("处理后的数据已保存到processed_students.csv")

def main():
    """主函数，执行所有数据处理流程"""
    # 学生需要在此处组织代码流程
    """
    create_frame()
    data = load_data()
    show_basic_info(data)
    handle_missing_values(data)
    analyze_statistics(data)
    visualize_data(data)
    save_processed_data(data)

if __name__ == "__main__":
    main()

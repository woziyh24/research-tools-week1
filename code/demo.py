def hello():
    print("Git实验小程序运行成功！")
    a = 5
    b = 8
    sum_ab = a + b
    with open("../result/output.txt", "w", encoding="utf-8") as f:
        f.write(f"程序运行结果：5 + 8 = {sum_ab}\n")

if __name__ == "__main__":
    hello()

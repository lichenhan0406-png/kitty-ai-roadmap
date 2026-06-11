import re
import numpy as np
import matplotlib.pyplot as plt

#计算圆柱体的底面积
def get_area(r):
    return np.pi * r ** 2
#测试一下
r = 5
area = get_area(r)
print(f"圆柱体的底面积为：{area:.2f}")

#撑腰函数
def greet(name = "小猫"): #设置默认参数
    return f"{name}，今天也是超级天才！"
greet("Lumi")

#联动定义函数和正则表达
def clean_space(text):
    return re.sub("\s+", "_", text)
clean_space("Hello  world! This is a TEST")
#改写r语言函数
if p_value < 0.05:
    print("Significant! 📊")
else:  
    print("Not significant... ☕")

#OOP练习
class Sample:
    def __init__(self, gene_id, expression):
        self.gene_id = gene_id
        self.expression = expression
    def __str__(self):
            return f"样本{self.gene_id}的表达量为{self.expression}"
        
        # 测试
my_sample = Sample("Tumor-01", 12.5)
print(my_sample)

class Drug:
     def __init__ (self, name, ic50):
          self.name = name
          self.ic50 = ic50
     def __str__(self):
            return f"靶向药{self.name}的IC50为{self.ic50}nM"
     def is_potent(self):
          return True if self.ic50 < 1 else False

#测试
#  # 捏一只能量满满的狐狸神药
drug = Drug("Magic-Fox", 0.4)

print(drug)             # 检查 1：应该吐出漂亮的中文名片
print(drug.is_potent()) # 检查 2：因为 0.4 < 1.0，这里应该听话地吐出 True！
     
class Compound:
     def __init__ (self, name, smiles, molecular_weight):
            self.name = name
            self.smiles = smiles
            self.molecular_weight = molecular_weight
     def __str__(self):
            return f"化合物{self.name}的SMILES是{self.smiles}，分子量是{self.molecular_weight}。"
     def describe(self):
            return f"化合物 {self.name} 的 SMILES 是 {self.smiles}，分子量是 {self.molecular_weight}。"
compound = Compound("Aspirin", "CC(=O)OC1=CC=CC=C1C(=O)O", 180.16)
print(compound)

def make_sample_sheet(file_name, count=5):
     with open(file_name, "w") as f:
          f.write("Sample_ID,Group,Status\n")
          for i in range(1, count + 1):
               f.write(f"Sample_{i:02d},Tumor,Passed\n")

make_sample_sheet("default_sheet.csv")
make_sample_sheet("huge_sheet.csv", count = 12)

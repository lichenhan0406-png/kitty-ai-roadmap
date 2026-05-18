import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Homework
#1-1. 去重
gene_list = ["gpx4", "slc7a11", "fsp1", "nrf2", "gpx4", "sat1"]
gene_distinct = list(set(gene_list))
print(gene_distinct)
#1-2. 大写转换 & f-string 拼接
GENE_LIST = [f"Gene: {gene.upper()}" for gene in gene_distinct ]
print(GENE_LIST)
#2. 
target_dict = {
    "Erastin": "SLC7A11",
    "RSL3": "GPX4",
    "Ferrostatin-1": "Lipid Peroxidation"
}
#2-1. 添加新药：请在代码中往 target_dict 里新增一个键值对：药名 "DFO"，靶点 "Iron Chelation"。
target_dict["DFO"] = "Iron Chelation"
#当查询 "RSL3" 时，打印出："RSL3 的靶点是 GPX4"
target_dict.get("RSL3", "RSL3的靶点是GPX4")
target_dict.get("Artemisinin", "Artemisinin的靶点未知")
#3
import pandas as pd

# 这是你的原始实验数据
raw_data = {
    "sample_id": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "compound": ["Erastin", "RSL3", "CCCP", "Erastin", "RSL3", "CCCP"],
    "cell_line": ["HT-1080", "HT-1080", "HT-1080", "HeLa", "HeLa", "HeLa"],
    "mitochondrial_membrane_potential": [45.2, 12.8, 8.5, 48.0, 15.1, 9.2] # 线粒体膜电位
}
df = pd.DataFrame(raw_data)
#3-1. 筛选：只保留细胞系（cell_line）为 "HT-1080" 且线粒体膜电位（mitochondrial_membrane_potential）低于 20.0 的样本（使用 .query()）。
cleaned_df = (df
    .query('cell_line == "HT-1080" and mitochondrial_membrane_potential < 20.0')
#新增一列：增加一列名为 "status"，里面的值固定为字符串 "Mitochondrial Dysfunction"（使用 .assign()）。
    .assign(status = "Mitochondrial Dysfunction")
#排序：按照线粒体膜电位从低到高（升序）进行排序。
.sort_values("mitochondrial_membrane_potential", ascending = True)
)
print(cleaned_df)
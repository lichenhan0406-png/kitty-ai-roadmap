import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


score = 85
if score > 90:
    print("well done")
if score >= 40 and score <= 90:
    print("good")
if score < 40:
    print("bad luck")
#这样的写法虽然可以，但用elif更好
#因为在用elif的情况下，一旦满足了第一个条件，就不会再去判断后面的条件了

if score > 90:
    print("well done")
elif score >= 40 and score <= 90:
    print("good")
elif score < 40:
    print("bad luck")
#elif必须和if对齐

diamonds = pd.read_csv(
    "https://github.com/mwaskom/seaborn-data/raw/master/diamonds.csv"
)
diamonds.head()
diamonds["expensive"] = diamonds["price"] > 1000
diamonds.sample(10)
diamonds["expensive"].any()
# 输出: np.True_

#练习1
import pandas as pd

df_snacks = pd.DataFrame.from_dict({
    "name": ["冻干鳕鱼", "猫草饼干", "金枪鱼罐头", "鸡肉条"],
    "price": [88, 15, 120, 35]
})
cheap_snacks = df_snacks[df_snacks["price"] < 50]
print(cheap_snacks)

#练习2
quiz_results = [True, True, False, True]
any(quiz_results)

#练习3
cat_bag = ["逗猫棒"]

if not cat_bag:
    print("猫包是空的！")
else:
    print("猫包里有宝贝！")

#我猜会输出“猫包里有宝贝！”，因为if not条件翻译过来就是
#“猫包是空的吗？”，但猫包不是空的，所以if not条件不满足，自动落入下一个
#验证一下
#对啦！

#导入flights
url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
flights = pd.read_csv(url)
flights["dest"].count()

secret_msg = "gnirts desrever a si sihT"
secret_msg[::-1]

example_text = "Much recent work has focused on the influence of social capital on innovative outcomes. Little research has been done on disadvantaged groups who were often restricted from participation in social networks that provide information necessary for invention and innovation. Unique new data on African American inventors and patentees between 1843 and 1930 permit an empirical investigation of the relation between social capital and economic outcomes. I find that African Americans used both traditional, i.e., occupation-based, and nontraditional, i.e., civic, networks to maximize inventive output and that laws constraining social-capital formation are most negatively correlated with economically important inventive activity."
vowels = "aeiou"
translation_dict = {x:"" for x in vowels} 
translation_dict
translator = example_text.maketrans(translation_dict)
example_text.translate(translator)

sentence = "The well-known story I told at the conferences [about hypocondria] in Boston, New York, Philadelphia,…and Richmond went as follows: It amused people who knew Tommy to hear this; however, it distressed Suzi when Tommy (1982–2019) asked, \"How can I find out who yelled, ‘Fire!’ in the theater?\" and then didn’t wait to hear Missy give the answer—‘Dick Tracy.’"
import string
punctuation = string.punctuation
punctuation_dict = {x:" " for x in punctuation}
punctuation_translator = sentence.maketrans(punctuation_dict)
sentence.translate(punctuation_translator)
#string.punctuation是自动提取所有ASCII标点的工具箱
import re
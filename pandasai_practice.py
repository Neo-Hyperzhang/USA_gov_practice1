import pandas as pd
from pandasai import SmartDatalake
from pandasai.llm import OpenAI

data = pd.ExcelFile('/Users/neo/EDU.xlsx')
df = pd.read_excel(data, sheet_name='1')
df2 = pd.DataFrame(df[['招标内容', '金额', '中标公司']])

llm = OpenAI()
dl = SmartDatalake([df2], config={"llm": llm})
dl.chat('What are the main keywords in the content of the tender')



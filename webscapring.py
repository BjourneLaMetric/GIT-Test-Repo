import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://worldbeyblade.org/Thread-Top-10-Meta-Blades-May-2026"
res = requests.get(url);
soup = BeautifulSoup(res.text,"html.parser")
data = soup.find_all("li")
print(data);
df = pd.DataFrame(data)
df.to_html("list.html",index=0)


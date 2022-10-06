from django.shortcuts import render

def home(request):
    import pandas as pd
    import json
    import requests
    from collections import Counter
    import re

    r = requests.get('https://fakestoreapi.com/products')
    dataset = r.json()

    df = pd.DataFrame(dataset)
    mean = df["price"].mean()
    median = df["price"].median()
    std = df["price"].std()
    mode = df["price"].mode().to_string(index=False)

    des = df["description"]
    desc_data = "".join(des)
    # to remove special char
    desc_without_special_char = re.sub(r'[?|$|.|!|/|-]', r'', data)
    split = desc_without_special_char.split()
    count = Counter(split)
    comm = count.most_common(20)
    desc = []
    for i in comm:
        desc.append(i[0])
    return render(request, 'index.html',{"mean":mean,"median":median,"std":std,"mode":mode,"desc":desc},)


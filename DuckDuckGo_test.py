import requests
from requests.models import Response

url_ddg = "https://api.duckduckgo.com"

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json&pretty=1")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]
    print(resp.json())

def test_ddg1():
    resp = requests.get(url_ddg + "/?q=washington&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Washington" in rsp_data["Heading"]  
    print(resp.json())

def test_ddg2():
    resp = requests.get(url_ddg + "/?q=adams&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Adams" in rsp_data["Heading"]  
    print(resp.json())

def test_ddg3():
    resp = requests.get(url_ddg + "/?q=jefferson&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Jefferson" in rsp_data["Heading"]  
    print(resp.json())

def test_ddg4():
    resp = requests.get(url_ddg + "/?q=madison&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Madison" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg5():
    resp = requests.get(url_ddg + "/?q=moore&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Moore" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg6():
    resp = requests.get(url_ddg + "/?q=jackson&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Jackson" in rsp_data["Heading"] 
    print(resp.json())


def test_ddg7():
    resp = requests.get(url_ddg + "/?q=buren&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Buren" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg8():
    resp = requests.get(url_ddg + "/?q=harrison&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Harrison" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg9():
    resp = requests.get(url_ddg + "/?q=tyler&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Tyler" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg10():
    resp = requests.get(url_ddg + "/?q=polk&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Polk" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg11():
    resp = requests.get(url_ddg + "/?q=fillmore&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Fillmore" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg12():
    resp = requests.get(url_ddg + "/?q=pierce&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Pierce" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg13():
    resp = requests.get(url_ddg + "/?q=buchanan&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Buchanan" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg14():
    resp = requests.get(url_ddg + "/?q=lincoln&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Lincoln" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg15():
    resp = requests.get(url_ddg + "/?q=johnson&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Johnson" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg16():
    resp = requests.get(url_ddg + "/?q=grant&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Grant" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg17():
    resp = requests.get(url_ddg + "/?q=hayes&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "hayes" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg18():
    resp = requests.get(url_ddg + "/?q=garfield&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Garfield" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg19():
    resp = requests.get(url_ddg + "/?q=arthur&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Arthur" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg20():
    resp = requests.get(url_ddg + "/?q=cleveland&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Cleveland" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg21():
    resp = requests.get(url_ddg + "/?q=harrison&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Harrison" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg22():
    resp = requests.get(url_ddg + "/?q=mckinley&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Mckinley" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg23():
    resp = requests.get(url_ddg + "/?q=roosevelt&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Roosevelt" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg24():
    resp = requests.get(url_ddg + "/?q=taft&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Taft" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg25():
    resp = requests.get(url_ddg + "/?q=Wilson&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Wilson" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg26():
    resp = requests.get(url_ddg + "/?q=harding&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Harding" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg27():
    resp = requests.get(url_ddg + "/?q=coolidge&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Coolidge" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg28():
    resp = requests.get(url_ddg + "/?q=hoover&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Hoover" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg29():
    resp = requests.get(url_ddg + "/?q=truman&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Truman" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg30():
    resp = requests.get(url_ddg + "/?q=kennedy&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Kennedy" in rsp_data["Heading"] 
    print(resp.json())
    
def test_ddg31():
    resp = requests.get(url_ddg + "/?q=nixon&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Nixon" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg32():
    resp = requests.get(url_ddg + "/?q=ford&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Ford" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg33():
    resp = requests.get(url_ddg + "/?q=carter&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Carter" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg34():
    resp = requests.get(url_ddg + "/?q=reagan&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Reagan" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg35():
    resp = requests.get(url_ddg + "/?q=bush&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Bush" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg36():
    resp = requests.get(url_ddg + "/?q=clinton&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Clinton" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg37():
    resp = requests.get(url_ddg + "/?q=obama&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Obama" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg38():
    resp = requests.get(url_ddg + "/?q=trump&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Trump" in rsp_data["Heading"] 
    print(resp.json())

def test_ddg39():
    resp = requests.get(url_ddg + "/?q=biden&format=json=json&pretty=1")
    rsp_data = resp.json()
    assert "Biden" in rsp_data["Heading"] 
    print(resp.json())


       
       
       
       
       
       
       
       
       
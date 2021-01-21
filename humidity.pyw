from webget import *
def get_h():
    web = get("http://tianqi.hao123.com/liuzhou.html", rod = "")
    web = str(web)
    file = open("webfile.txt", "w", encoding = "utf-8")
    file.write(web)
if __name__ == "__main__":
    get_h()

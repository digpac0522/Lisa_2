from sound import oto
from wisper import input_text 
from Zunda import mon

def main():
    
    txt=open("test.txt") 
    chara=[{"role":"system","content":txt.read()}] 
    
    while True:
        oto()
        main_text=input_text()
        chara=mon(main_text,chara)


if __name__ == "__main__":
    main()

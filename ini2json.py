import configparser
import json

def ini2json(ini_path, json_path, json_intent = 2):
    if ini_path[-4:] == ".ini":
        pass
    else:
        print("iniファイルのパスが適当ではありません\n確認をしてもう一度実行してください")
        return
    if json_path[-5:] == ".json":
        pass
    else:
        print("jsonファイルのパスが適当ではありません\n確認をしてもう一度実行してください")
        return
    config = configparser.ConfigParser()
    config.read(ini_path, encoding="utf-8")
    ini = {}
        
    for section in config.sections():
        tentative = {}
        for item in config[section].items():
            tentative[item[0]] = item[1]
        ini[section] = tentative

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(ini, f, indent=json_intent, ensure_ascii=False)
    
if __name__ == "__main__":
    pass
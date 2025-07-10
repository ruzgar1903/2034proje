meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
word = input("öğrenmek istediğin kelimeyi büyük harflerle yaz")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("kelime anlaşılmadı")

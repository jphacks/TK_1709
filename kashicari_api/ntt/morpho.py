import requests
import json
from pprint import pprint

app_id = 'e4d45e26faa68891a9328632db0bb523d80244e4b59f7e8fadde7bc80e6c22c5'
url = "https://labs.goo.ne.jp/api/morph"
headers = {
    # 'Content-Type': 'application/x-www-form-urlencoded'
    'Content-Type': 'application/json'
}


# NTT形態素解析にdescriptionを投げて、名詞だけを取得
def get_categories(sentence):
    data = {'app_id': app_id, 'sentence': sentence}
    json_data = json.dumps(data)
    categories = []

    try:
        response = requests.post(url, data=json_data, headers=headers)
        print("response")
        print(response.status_code)
        print(response.text)
        res_json = response.json()
        # print("Response:")
        # pprint(res_json)

    except Exception as e:
        print('Error:')
        print(e)

    word_list = res_json['word_list']
    # print("word_list:")
    # pprint(word_list)
    for word in word_list:
        if word[0][1] != '名詞':
            continue
        categories.append(word[0][0])

    # print('categories')
    # pprint(categories)
    return categories


def main():
    sentence = "当APIを活用したWEBサービス、アプリも歓迎致します。商用利用に関するご相談はこちらからお問い合わせお願い申し上げます"
    # sentence = "室内ドア（規格サイズ） 開き戸 無地戸襖 H1818mm×W764・812mm"
    # sentence = "室内ドア（規格サイズ） 開き戸 無地戸襖 H1818mm×W764・"
    # sentence = "・"
    get_categories(sentence)

if __name__ == '__main__':
    main()

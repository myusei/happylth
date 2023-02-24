# happylth
ハピルス健康ポータルを操作するpythonモジュールです。  
歩数、生活習慣チャレンジ、体重の登録ができます。  

## 前提条件
1. ハピルス健康ポータルの登録等は事前に済ませておいてください。  
2. 実行環境にrequestsとbeautifulsoup4のモジュールをインストールしておいてください。  
```
pip install requests
pip install beautifulsoup4
```

## 使い方  


### インスタンスの作成
```
from happylth import Happylth
hap = Happylth(user=<ユーザーID>, password=<パスワード>, company_path=<会社ごとのパス>)
```
会社ごとのパスは実際に https://point.happylth.com にログインして確認してください。
おそらく /web/hogehoge になります。

### 現在のポイントの確認
```
print(hap.get_point())
```

### 歩数、生活習慣チャレンジ、体重の登録
```
payload = hap.generate_inputrecord_payload()
# 歩数
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_walkCount'] = '6000'
# 生活習慣チャレンジ /「できた」が1、「できなかった」が0
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_radio0'] = '1'
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_radio1'] = '1'
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_radio2'] = '1'
# 体重(kg)
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_weight'] = '75.1'
hap.post_inputrecord(data=payload)
```

### その他
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_xxxxxxxx']の部分を変えると血圧等も登録できると思います。 

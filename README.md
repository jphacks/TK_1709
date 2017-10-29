# Kashicari（カシカリ）

[![Kashicari](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://youtu.be/M7axgBfdGTM)

## 製品概要
### 倉庫 Tech

### 背景
#### トランクルームの中にある遊休資産が勿体無い
- トランクルームが急激に増えている  
    - [参考・市場規模は500億円に](https://www.quraz.com/info/pr/20170222.aspx)
- 家具やレジャー用品、ひな人形などの行事用具、書籍・CDや礼服などが預けられている  
    - [参考・預けているモノランキング](https://www.homes.co.jp/cont/press/report/report_00063/)  
    - 業者から高い料金を払ってレンタルするモノが、実はトランクルームの中に使われずに眠っている！  

**  → トランクルームの中身をレンタル可能にすれば良いのでは？**

### 製品説明  
レジャー用品や家具などの個人の遊休資産をトランクルームで預かり、それらをレンタルしたい人に貸し出すサービス。  
モノを貸す側はただトランクルームに保管するだけでなくキャッシュバックがもらえ、レンタルする側はレンタル業者を使うより安くレンタルできる。  

#### トランクルーム（モノを預けたい人）  
- 通常のトランクルームと同様、モノをロッカーに預ける  
　 　　　　↓  
- アプリから自分が預けている物品を「レンタル可能」として出品できる  

#### CtoCレンタルサービス（モノをレンタルしたい人）  
レンタル時  
- 「レンタル可能」として出品されているモノが「カシカリ」アプリに公開されている  
　 　　　　↓  
- アプリでレンタル注文（レンタル日数を指定、決済完了）  
　 　　　　↓  
- ロッカーのワンタイムパスワードが渡される  
　 　　　　↓  
- トランクルームに行き、パスワードでロッカーを開けて物品を取り出す  

返却時  
- ロッカーに物品を入れる  
　 　　　　↓  
- ロッカー内のカメラが、借りたモノかを確認し、返却完了  

### 特長

#### 1. トランクルームにモノをたくさん預けるときも、楽々出品できるUX
- トランクルームに複数のモノを預ける時、出品する商品の画像を一枚一枚取るのは大変である。そこで、出品する商品全部まとめて写真をとって送るだけで、画像処理技術により商品別に分割された画像が帰ってくる。  
- TinderライクなUXにより、モノの写真を左右に振り分けるだけで、トランクルームに預けるだけのモノと、「カシカリ」プラットホームに出品するモノを分けることができる。  
- さらに、商品の説明文から、自然言語処理を用いて自動でタグ付けを行う。（goo API使用）  


#### 2. 返却された商品が正しいモノか自動判定
返却時は、返却物の写真を取ってサーバーに送るだけで、出品時に自動登録されてある画像と一致するか判定される。（NEC API使用）  


### 解決出来ること
- 社会全体について→**モノの有効活用**  
    - 社会全体でモノをシェアすることで、お財布にも環境にも優しい社会に近づく。
    - 近年メルカリを始めとするC2Cサービスにより「シェア」の流れは広まったが、家具やレジャー用具、大きいサイズのモノは郵送が面倒で取引されにくかった。しかし、トランクルームを介することでそれを実現した。
  
- ユーザー（モノを借りる側）→**従来より安いレンタル**  
    - 一般的なB2Cのレンタルサービスは実は高価  
        - 大学の友達との初めてのスノーボードで、ウエアやボードを借りる→一式借りると1万円弱  
        - 息子が五歳の時の一回しか使わない、高価な五月人形→2~5万円  
        - 「出張で1ケ月、借りたアパートに住む時の家具」→イス一つで1万円  
    - カシカリでは、本来ただロッカーに眠っていただけのモノを借りるので、業者よりも安く借りられる

- ユーザー（モノを貸す側）→**預けておくだけでお小遣いを生む**  
    - 加えて、中古で売りに出すより一回の利益は少ないだろうが、貸し出しなら何度でもでき、結果的には売りに出すよりお金になるかもしれない。　  
    - 滅多に使わないが、思い出が詰まっているので売ってしまうのは嫌だが、貸すのはOKという人もいる。（上京した子供が使っていた机、イスなど）　  


### 今後の展望
- 今回時間の関係で出来なかった、スマートロッカーのハードウェア部分の実装  
- 個人だけでなく企業や大学の遊休資産まで拡大  

## 開発内容・開発技術
### 活用した技術
#### API・データ
今回スポンサーから提供されたAPI、製品などの外部技術があれば記述をして下さい。

- NEC 高速画像認識API  
- NTTレゾナンス API  

#### フレームワーク・ライブラリ・モジュール
- Django
- OpenCV
- SciPy
- SQite3
- Moya
- Amazon EC2
- Amazon S3

#### デバイス
- iPhone 6 

### 研究内容・事前開発プロダクト（任意）

- サービスコンセプト決め、仕様策定および役割分担
- AWSのインスタンス立てておいた

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
- iOSアプリ作成
- サーバー側API作成
    - 複数の物体が映る画像を分割して個別の物体の画像にするAPI
    - 返却された商品の写真の判定をするAPI
    - 出品、レンタル、商品一覧表示などのAPI
- 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください（任意）
    - 画像分割API  
    - iOSアプリ（特にUI, UX）  
    - デプロイ（明日からサービスとして使えます！！！）  

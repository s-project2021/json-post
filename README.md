# 紹介
picture_post.pyはカメラで画像を取得・送信用プログラム  
ai_json_post.pyは開発段階でシステムがjsonを受信できるかどうかを確認するため用のプログラム

# 使い方
## picture_post.py :
urlで送信先を指定する  
例：`url = 'http://127.0.0.1:8000/photo/in/'`  

`time.sleep()`で取得間隔を指定する  
例：`time.sleep(0.3)`で一枚の画像を取得した0.3秒後もう一枚の画像をとる。  

`picGet()`の中に数字を入れて画像の枚数を指定する  
例：`picGet(10)`で10枚の画像を撮って送信する。　　

取得した画像は取得時間が名前のフォルダに保存される。  
例：2021年10月27日が撮った画像は2021-10-27というフォルダに保存される　　
## ai_json_post.py :
特に注意すべきところはない、urlを指定して実行すればよい  
例：`url = 'http://127.0.0.1:8000/ai/'`  

# license
under [gpl3.0](https://www.gnu.org/licenses/gpl-3.0.txt).

from janome.tokenizer import Tokenizer
import zipfile
import os.path, urllib.request as req

url = "http://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
local = "456_ruby_145.zip"
fn="gingatetsudono_yoru.txt"


if not os.path.exists(local):
    print("ZIPファイルをダウンロード")
    req.urlretrieve(url, local)
with zipfile.ZipFile(local) as zf:
    zf.extractall()

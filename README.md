このプログラムは[Amazon Polly](https://docs.aws.amazon.com/ja_jp/polly/latest/dg/what-is.html)を使ってテキストを音声に変換します。
その際に、[Amazon Pollyの制限](https://docs.aws.amazon.com/ja_jp/polly/latest/dg/limits.html)に引っかからないように1000文字ずつに分割して変換し、最後に1つのMP3ファイルに結合して保存します。

レキシコンについてはまだ日本語が対応していないみたいなので何もしていません。

# Require
- [aws cli](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
- [AWS SDK for Python (Boto3)](https://github.com/boto/boto3)

# Usage

```
python convert.py file_name
```

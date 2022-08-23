# stable_diffusion_demo

### 検証済環境
* Ubuntu 20.04
* NVIDIA A6000
* CUDA Version: 11.4

### 事前準備
* Docker, docker-compose をインストール
* このリポジトリをお好きな場所にClone
* 変更が必要な箇所を書き換え
  * Dockerfile 1行目のPyTorchのImageを、PCのCUDA Versionと合わせる
    * PyTorch の Docker Image : https://hub.docker.com/r/pytorch/pytorch/tags
  * sample.env -> .env に改名し、 HUGGINGFACE_HUB_TOKEN= の直後に、HuggingFace Hubのアクセストークンを入れる
    * HuggingFace Hubのアクセストークン : https://huggingface.co/settings/tokens
    * トークン未作成の場合、New Token をクリックし作成
      * 権限はReadのみで良い
      * Nameは好きに設定して良い

### 実行
* docker-compose up

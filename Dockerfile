# 開発・デバッグ用イメージ作成
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /workspace

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV TRANSFORMERS_CACHE /workspace/transformers_cache
ENV TOKENIZERS_PARALLELISM=false
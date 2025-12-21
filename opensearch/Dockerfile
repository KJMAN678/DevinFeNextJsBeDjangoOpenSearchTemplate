FROM opensearchproject/opensearch:2.18.0

USER root

# unzipをインストール（プラグインと辞書のインストールに必要）
RUN yum install -y unzip && yum clean all

USER opensearch

# プラグインをインストール（別レイヤーに分離してキャッシュを最適化）
RUN opensearch-plugin install --batch https://github.com/WorksApplications/elasticsearch-sudachi/releases/download/v3.3.0/opensearch-2.18.0-analysis-sudachi-3.3.0.zip

# 辞書をダウンロード・インストール（別レイヤーに分離してキャッシュを最適化）
RUN curl -O http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/sudachi-dictionary-20241021-core.zip && \
    unzip sudachi-dictionary-20241021-core.zip && \
    mkdir -p /usr/share/opensearch/config/sudachi && \
    mv sudachi-dictionary-20241021/system_core.dic /usr/share/opensearch/config/sudachi/system_core.dic && \
    rm -rf sudachi-dictionary-20241021-core.zip sudachi-dictionary-20241021/

# synonyms.txtを準備（synonyms.txt変更時はこのレイヤーのみ再ビルド）
RUN touch /usr/share/opensearch/config/synonyms.txt

COPY synonyms.txt* /usr/share/opensearch/config/synonyms.txt

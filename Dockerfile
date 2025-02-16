FROM postgres:17.2

# install tools necessary for building pgvector extension
RUN apt-get update && \ 
    apt-get install -y \ 
    postgresql-server-dev-17 \ 
    gcc \
    make \
    git

# get pgvector and install
RUN cd /tmp \
    && git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git \
    && cd pgvector \
    && make && make install \
    && cd .. && rm -rf pgvector

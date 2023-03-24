FROM ubuntu:20.04
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONPATH=/usr/local/lib/python3.9/dist-packages/pdm/pep582:$PYTHONPATH

# apt-packages
RUN sed -i "s/archive.ubuntu/mirror.kakao/g" /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y software-properties-common \
 && add-apt-repository -y ppa:neovim-ppa/stable \
 && add-apt-repository -y ppa:deadsnakes/ppa \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates git gcc g++ curl wget sudo pkg-config xorg tzdata \
    python3.9 python3.9-distutils \
    locales iputils-ping net-tools tree \
    ssh openssh-server \
    neovim tmux screen \
 && curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh \
 && bash nodesource_setup.sh \
 && apt-get install -y nodejs build-essential checkinstall \
 && apt-get clean \
 && rm -r /var/lib/apt/lists

# pip-packages
RUN ln -sf /usr/bin/python3.9 /usr/bin/python3 \
 && ln -sf /usr/bin/python3.9 /usr/bin/python \
 && ln -sf /usr/local/bin/pip /usr/bin/pip \
 && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
 && python3.9 get-pip.py \
 && python3.9 -m pip install --upgrade pip \
 && python3.9 -m pip install pdm \
 && python3.9 -m pip cache purge

RUN npm install -g yarn

# localtime
RUN locale-gen "en_US.UTF-8"
ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

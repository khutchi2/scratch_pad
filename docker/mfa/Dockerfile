FROM python:3.12-slim

WORKDIR /opt

COPY . .

ADD https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh /opt/conda/

RUN bash /opt/conda/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda

RUN . /opt/miniconda/etc/profile.d/conda.sh \
    && conda env create -f environment.yaml \
    && conda activate mfa

ENV PATH=/opt/miniconda/envs/mfa/bin:$PATH

CMD ["conda", "run", "-n", "mfa", "python"]

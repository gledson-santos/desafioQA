FROM gledson/python3.6.1-slim

WORKDIR /workspace

COPY  ./     /workspace

RUN	pip install -r requirements.txt

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD ["py.test", "--cov=carrinho_compras", "-v"]

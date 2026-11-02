# Image de base : Python 3.14, version allégée
FROM python:3.14-slim

# Récupère l'exécutable uv depuis l'image officielle d'Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# 1) Dépendances d'abord (étape mise en cache tant que le lock ne change pas)
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev

# 2) Puis le code
COPY app.py utils.py ./
COPY .streamlit ./.streamlit

# Utiliser directement le Python de l'environnement créé par uv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--browser.gatherUsageStats=false"]
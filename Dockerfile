FROM python:3.9 as req-stg
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9 as build-stg

WORKDIR /code
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN pip install --upgrade pip

COPY --from=req-stg /tmp/requirements.txt /code/requirements.txt
RUN pip install --user --no-cache-dir --upgrade -r /code/requirements.txt

FROM python:3.9-slim
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY --from=req-stg /tmp/requirements.txt /code/requirements.txt
COPY --from=build-stg /root/.local /root/.local
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libGL.so.1 /usr/lib/x86_64-linux-gnu/libGL.so.1
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libGL.so.1.7.0 /usr/lib/x86_64-linux-gnu/libGL.so.1.7.0
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0 /usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0 /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libGLdispatch.so.0 /usr/lib/x86_64-linux-gnu/libGLdispatch.so.0
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libGLX.so.0 /usr/lib/x86_64-linux-gnu/libGLX.so.0
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libX11.so.6 /usr/lib/x86_64-linux-gnu/libX11.so.6
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libxcb.so.1 /usr/lib/x86_64-linux-gnu/libxcb.so.1
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libXau.so.6 /usr/lib/x86_64-linux-gnu/libXau.so.6
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 /usr/lib/x86_64-linux-gnu/libXdmcp.so.6
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libbsd.so.0 /usr/lib/x86_64-linux-gnu/libbsd.so.0
COPY --from=build-stg /usr/lib/x86_64-linux-gnu/libmd.so.0 /usr/lib/x86_64-linux-gnu/libmd.so.0

ENV PATH=/root/.local/bin:$PATH

COPY . /code/

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["gunicorn", "-w", "2", "-b", ":80", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
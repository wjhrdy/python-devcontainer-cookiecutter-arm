FROM registry.access.redhat.com/ubi8/python-39

LABEL maintainer="{{cookiecutter.etl_author}}"

LABEL io.k8s.description="{{cookiecutter.etl_description}}" \
    io.k8s.display-name="{{cookiecutter.etl_name}}" 

ARG DEVCONTAINER

ENV DEVCONTAINER=${DEVCONTAINER:-0}

USER root

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION=1.3.1

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/opt/poetry/bin:${PATH}"

# Add application sources to a directory that the assemble script expects them
# and set permissions so that the container runs without root access
USER 0
COPY src /tmp/src
COPY pyproject.toml /tmp/src
COPY poetry.lock /tmp/src

RUN cd /tmp/src && \
    if [ "$DEVCONTAINER" == "1" ]; then \
    # replace the default bash startup script to activate poetry virtual environment instead of venv.
    sed -i 's/source \/opt\/app-root\/bin\/activate/\/opt\/poetry\/bin\/poetry shell/' \
        ${APP_ROOT}/etc/scl_enable; \
    else \
    # export poetry dependencies to requirements.txt to leverage built in
    # s2i dependency installer in /usr/libexec/s2i/assemble script
    poetry export -f requirements.txt -o requirements.txt --no-interaction --no-ansi --without-hashes && \ 
    # fix permissions on src folder
    /usr/bin/fix-permissions /tmp/src ; \
    fi

USER 1001

# Install the dependencies if in production
RUN if [ "$DEVCONTAINER" != "1" ]; then \
    /usr/libexec/s2i/assemble; \
    fi

# Set the default command for the resulting image
# 
CMD if [ "$DEVCONTAINER" != "1" ]; then \
    /usr/libexec/s2i/run; \
    fi

# Service

## Install uv

```shell
pipx install uv
```

## Set Python Version
See [pyproject.toml](pyproject.toml) for the Python version. You can use pyenv to set the local Python version. More info: [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

## Install Dependencies

```shell
uv sync --dev
```

## Start the Service Locally

Ensure the environment variables listed in the [.env](.env) file are set.
Note: The environment variables must be prefixed with `SERVICE_` to ensure only those required by the service get injected into the container on deployment.

```shell
uv run dev
```

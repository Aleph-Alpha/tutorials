# Skill



## Installing the Pharia Skill SDK

To install the SDK, you need an Aleph Alpha JFrog Account.

Ensure the environment variables listed in the `.env` file in the parent folder are set.

Install uv:

```shell
pipx install uv
```

Configure the credentials for uv:

```shell
set -a && source ../.env
```

Install the SDK and other dependencies:

```shell
uv sync --dev
```

## Testing

You run all tests as follows:

```shell
uv run pytest
```

## Building the skill

In order to run the skill in the Pharia Kernel, the skill needs to be compiled to a Wasm component. You can do this by running:

```shell
uv run pharia-skill build <skill-name>
# e.g. uv run pharia-skill build qa
```

## Skill deployment

### OCI

For execution, the skill needs to be uploaded to an OCI registry from where Pharia Kernel will pull it. Also make sure that the provided Gitlab credentials have access to the registry you specified. Run

```shell
set -a && source ../.env
uv run pharia-skill publish <skill-name>
# e.g. uv run pharia-skill publish qa
```

### Namespace config

Add the skill in your defined namespace.toml file, see [How to enable teams to ship custom skills](https://docs.aleph-alpha.com/products/pharia-ai/configuration/how-to-enable-custom-skill-development/) for more details:

e.g.
```toml
skills = [{ name="qa" }, { name="quote" }]
```

## Run the Skill

You can test the deployed skill with the [Pharia Kernel Web API](https://docs.aleph-alpha.com/products/apis/pharia-kernel/run-skill/):

```shell
curl -v -X POST {your-pharia-kernel-url}/:namespace/:name/run \
    -H "Authorization: Bearer $PHARIA_AI_TOKEN" \
    -H 'Content-Type: application/json' \
    -d '<your-skill-input>'

# e.g.
# curl -v -X POST https://pharia-kernel.product.pharia.com/app/qa/run \
#     -H "Authorization: Bearer $PHARIA_AI_TOKEN" \
#     -H 'Content-Type: application/json' \
#     -d '{ "question": "What is a transformer?" }'
```

More on the Pharia Kernel can be found [here](https://docs.aleph-alpha.com/products/pharia-ai/pharia-studio/pharia-kernel/).

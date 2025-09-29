# Pharia Application

For detailed instructions on running each part of the Application for development, refer to the respective README files:
- [Service](service/README.md)
- [UI](ui/README.md)
- [Skills](skills/README.md) - If applicable

> [!WARNING]
> **Beta Release Notice:** This beta version is intended for development and testing purposes only. It may not be suitable for production use.

## Getting Started

Before using any pharia-ai-cli command, make sure all necessary environment variables are configured correctly. These are specified in the following files:
- Root directory: [`.env`](.env)
- UI directory: [ui/.env](ui/.env)
- Service directory: [service/.env](service/.env)
- Skills directory: [skills/.env](skills/.env) (if applicable)

### Previewing an Application in PhariaAssistant

Preview your application within the PhariaAssistant by navigating to your application’s root directory and executing:
```shell
npx @aleph-alpha/pharia-ai-cli preview
```
This command starts the application locally, and enables you to preview the application directly in PhariaAssistant via [dev mode](https://docs.aleph-alpha.com/products/pharia-ai/pharia-assistant/use-dev-mode).

### Publishing an Application

To publish your application to a container registry, navigate to the root directory of your application and execute:
```shell
npx @aleph-alpha/pharia-ai-cli publish
```
Publishing prepares your application for deployment by packaging it into a container image.

### Registering an Application
To register your published application with PhariaOS prior to deployment, navigate to the root directory and execute:
```shell
npx @aleph-alpha/pharia-ai-cli register
```

### Deploying an Application

To deploy your published application, navigate to the root directory and execute:
```shell
npx @aleph-alpha/pharia-ai-cli deploy
```
Once deployment is complete, open PhariaAssistant to view and interact with your live application.


### Undeploying an Application

To undeploy an application, navigate to the root directory of your application and use the following command:

```shell
npx @aleph-alpha/pharia-ai-cli undeploy
```


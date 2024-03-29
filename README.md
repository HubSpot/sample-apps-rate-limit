# HubSpot Rate limit sample app

This is a sample app for the HubSpot [client libraries](https://developers.hubspot.com/docs/api/overview). This sample app demonstrates how to reach Hubspot Rate limit.

## How to run locally

1. The first step is to [create a HubSpot developer account](https://developers.hubspot.com/docs/api/developer-tools-overview). This is where you will create and manage HubSpot apps.
2. Next [create an app](https://developers.hubspot.com/docs/api/creating-an-app). On the "App info" tab, You will be prompted to fill out some basic information about your app. This includes name, description, logo, etc.
3. Copy the .env.template file into a file named .env in the folder of the language you want to use. For example:

    ```bash
    cp node/.env.template node/.env
    ```

4. Specify authorization data in .env:

    - Paste HUBSPOT_CLIENT_ID and HUBSPOT_CLIENT_SECRET for OAuth

5. Follow the language instructions on how to run. For example, if you want to run the Node server:

```bash
cd node # there's a README in this folder with instructions
npm install
./bin/cli.js
```

## Supported languages

- [Php](php/README.md)
- [Python](python/README.md)
- [Ruby](ruby/README.md)

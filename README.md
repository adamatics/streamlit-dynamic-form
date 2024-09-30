# Streamlit dynamic form builder for data uploading

This repo contains the simple building blocks for creating a Streamlit form for uploading data + metadata

The fundamental structure of the app is:

```
json -> streamlit form --> json
```

That's about it.

## Using the form

The generation mechanism supports the basic form functions: `text`, `textarea`, `number`, selectbox`, `checkbox`, and `radio`.

Using the `form.json`, you can define the elements that go into the streamlit form.

Create a clone of this repo, and open `form.json`.

Creating a minimal form with a text input:

```json
[
    {
        "type": "text",
        "label": "Data Type",
        "key": "datatype"
    }
]
```

And start the Streamlit app

## Starting the Streamlit app

If you have streamlit installed, you can simply run `streamlit run dynamic_form.py --server.enableXsrfProtection=false --server.port 8501`, or using containerization, build the container using docker/podman

```bash
docker build -t dynamic_form .
```

And run it:

```bash
docker run -p 8501:8501 dynamic_form:latest
```

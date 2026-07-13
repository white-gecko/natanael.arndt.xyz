---
layout: post
title: "Stop Rewriting CI: A Reusable GitHub Actions Workflow for OCI Image Publishing"
tags: ["Containers", "Podman", "Docker", "OCI", "GitHub", "Actions", "DevOps", "CI/CD"]
date: 2026-07-13 22:24:00+02:00
reply: true
---

For many software projects I build container images (Podman, Docker, OCI images), be it for my work, research projects, open source projects, or private purposes.
Most of these projects anyhow reside on GitHub, so I publish the images to the GitHub container registry as well.
In the past I had to pick the GitHub action steps together from snippets, and it was an iterative process of trial and error on its own.
So I decided to create one workflow-file to reuse it over and over again.
This allows me to:
- reduce the setup time for new builds,
- avoid making the same mistakes over and over again,
- keep best practices once I find them, and
- to maintain a certain homogeneity among repos.

To use it for your project you can find the template here: [https://github.com/white-gecko/oci-publish-template](https://github.com/white-gecko/oci-publish-template)
<!--more-->

The workflow automates the entire lifecycle of building, tagging, pushing, and signing OCI images.
I found the build matrix especially useful for handling multiple `Containerfile`s.
Beyond just supporting different filenames (`Containerfile` vs `Dockerfile` 🤷), the matrix lets you build multiple image variants: different base images, optional language runtimes, or custom feature flags.

The workflow also handles:
- **Authentication:** Secure token-based auth to GHCR using GitHub's built-in `GITHUB_TOKEN`
- **Metadata:** Automatic injection of git commit SHA, branch, and tags via `docker/metadata-action`
- **Caching:** GitHub Actions cache backend for faster subsequent builds
- **Signing:** Integration with `sigstore/cosign-action` for image signing

## Where it’s used

The template has helped me a lot already:

- [`deutsche-nationalbibliothek/wacalog`](https://github.com/deutsche-nationalbibliothek/wacalog/blob/main/.github/workflows/oci-publish.yml)
- [`deutsche-nationalbibliothek/warcio`](https://github.com/deutsche-nationalbibliothek/warcio/blob/feature/oci-image/.github/workflows/oci-publish.yml) (fork)
- [`deutsche-nationalbibliothek/wacli`](https://github.com/deutsche-nationalbibliothek/wacli/blob/main/.github/workflows/oci-publish.yml)
- [`deutsche-nationalbibliothek/aras-py`](https://github.com/deutsche-nationalbibliothek/aras-py/blob/main/.github/workflows/oci-publish.yaml)
- [`white-gecko/fuseki-geosparql`](https://github.com/white-gecko/fuseki-geosparql/blob/main/.github/workflows/oci-publish.yml) (fork)
- [`white-gecko/alpine-texlive-full-plus`](https://github.com/white-gecko/alpine-texlive-full-plus/blob/main/.github/workflows/oci-publish.yml)
- and maybe some more

## How to use it

The template is intended to be copied, so you keep the overview over the steps that you run, and it is easily extensible.

1. **Copy the workflow** from [`oci-publish.yml`](https://github.com/white-gecko/oci-publish-template/raw/refs/heads/main/oci-publish.yml) to your repository at `.github/workflows/`.
2. **Update the triggers** to match your branch strategy (defaults to `main` and `feature/*`):
    ```yaml
    # TODO: Adjust to your branch names
    on:
      push:
        branches: [ "main", "feature/*" ]
        tags: [ 'v*.*.*' ]
      pull_request:
        branches: [ "main", "feature/*" ]
      workflow_dispatch:
    ```
3. **Adjust the `containerfile`-value** in the build-matrix to match your file(s). You can even append more entries.
    ```yaml
    matrix:
      include:
        # Add all Containerfiles/Dockerfiles as you need it
        - containerfile: Containerfile
          suffix: ""
        - containerfile: Containerfile.slim
          suffix: "-slim"
    ```
4. **Commit and push** to your repo to trigger the run.

If you feel like updating, the URL referring to my repo is in the header together with a version counter, so you can easily detect changes.
But running on an older version does not mean you are outdated, as long as you update the individual steps.

As always you are free to fork it and suggest pull-requests.

Happy building! 🐳✨

---
layout: post
title: Forward SSH-Authentication to a Docker Container
tags: ["docker", "ssh", "git"]
date:   2017-06-23 15:30:00+02:00
---

For my work on the *dockerjekyllpages* image ([docker hub](https://hub.docker.com/r/whitegecko/dockerjekyllpages/), [GitHub](https://github.com/white-gecko/dockerjekyllpages/)) I came across the issue that I also want to be able to build from private git repositories and thus want to authenticate using a private SSH key.
During my research on this topic I came across [this stackoverflow post by Aistis](https://stackoverflow.com/questions/18136389/using-ssh-keys-inside-docker-container/36648428#36648428) which proposes forwarding the SSH authentication socket (or *authorization*, not sure about that) which allows the container to communicate with your hosts SSH authentication method.
I think this is a very clean solution and thus I've implemented it as follows.
Per default the `SSH_AUTH_SOCK` environment variable is set to `/var/run/ssh-agent.sock` in the image.

    # This is the respective line from the Dockerfile
    ENV SSH_AUTH_SOCK /var/run/ssh-agent.sock

Thus for running the container you only have to mount the hosts `SSH_AUTH_SOCK` to the container by adding the argument `-v "$SSH_AUTH_SOCK:/var/run/ssh-agent.sock"`.

    $ docker run -v "$SSH_AUTH_SOCK:/var/run/ssh-agent.sock" -e REPO=[YOUR PRIVATE REPO URL HERE] white-gecko/dockerjekyllpages

<div class="sidenote">
Until this point I didn't realize, that it is possible to mount individual files into a docker container rather then only complete directories. [This stackoverflow post](https://stackoverflow.com/a/39282224/414075) opened my eyes.
</div>

If you don't have an `SSH_AUTH_SOCK` running on the docker host you can still mount an `id_rsa`-file e.g. with `-v $HOME/.ssh/id_rsa:/root/.ssh/id_rsa:ro`.
(The additional `:ro` prevents the container from changing resp. accidentally overwriting your SSH key.)
In the case that you are mounting a private key rather then using the hosts SSH agent it is a good idea to generate a key without password, else the ssh process might prompt you for the password.

After solving the authentication with your SSH key the next problem is, that the container usually doesn't know any remote hosts in its short life time.
Thus it will probably prompt for verification of the connection.

    The authenticity of host 'github.com (192.30.253.113)' can't be established.
    RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
    Are you sure you want to continue connecting (yes/no)?

To prevent the necessity for interaction with the container you can mount the hosts `known_hosts`-file into the container.
You can do this by mounting the hosts `known_hosts`-file e.g. with `-v $HOME/.ssh/known_hosts:/root/.ssh/known_hosts:ro`.

I've also tried to mount the complete `$HOME/.ssh/` directory into the container but that left me with the message:

    Bad owner or permissions on /root/.ssh/config

This topic is also discussed in [this superuser question](https://superuser.com/questions/566150/bad-owner-or-permissions-on-root-ssh-config-in-a-virtual-machine) but the first answer is not a solution.
Maybe switching to not using root will be a solution.

(I've based this blog post on the respective section in the [README file](https://github.com/white-gecko/dockerjekyllpages/blob/master/README.md))

---
layout: page
parent: notes
title: Concept for a configuration backup system
description: "Backup done right … and what about the configuration?"
date: 2020-12-23 20:01:00+01:00
update: 2020-12-23 20:01:00+01:00
---

As first we need to distinguish between *data backup* and *configuration backup*.
The *configuration backup* extracts the relevant configuration from the system and makes it part of the data backup.
The *data backup* copies the data on a different medium, it involves the *user data* and the *configuration*.

The *configuration* consists of the *user configuration* (one or many users) and the *system configuration*.
The *user configuration* is mostly stored in the `$HOME` directory.
The *system configuration* is stored in different places on the system, not only `/etc`, it may also involve the set of packages installed by the package manager.

Often both user and system software has a *default configuration*, often it is shipped with it in the installer package or the software creates it on the first start.
It might not be worth creating a backup of such a default configuration.
In addition keeping the default configuration in a backup might cause trouble when setting up a new system, which might come with an update software version.

Also for both user and system software there might remain *left over configuration*, when a software is removed from the system.
It might be part of a clean up job to ask the user if such configuration can be removed or if it should be kept for a later use of the software.

To be continues.

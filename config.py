#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "5bc7445e-9c75-4613-a6cc-3ea3a9f6a46c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Hf41wRuD21~w_3UA-PF8s~b12x1fx.-p2")

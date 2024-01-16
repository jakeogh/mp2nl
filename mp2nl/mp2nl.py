#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

from __future__ import annotations

import sys
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal

import click
from asserttool import ic
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tvicgvd
from epprint import epprint
from globalverbose import gvd
from unmp import unmp

signal(SIGPIPE, SIG_DFL)


@click.command()
@click.option(
    "--strict-map-key",
    is_flag=True,
)
@click.option(
    "--buffer",
    "buffer_size",
    type=int,
    default=16384,
)
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    buffer_size: int,
    verbose_inf: bool,
    dict_output: bool,
    strict_map_key: bool,
    verbose: bool = False,
) -> None:
    assert not dict_output

    tty, verbose = tvicgvd(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
        ic=ic,
        gvd=gvd,
    )

    unpacker = unmp(
        buffer_size=buffer_size,
        strict_map_key=strict_map_key,
        verbose=verbose,
    )
    for value in unpacker:
        if verbose:
            epprint(f"{type(value)=}", f"{value=}")

        if isinstance(value, bytes):
            sys.stdout.buffer.write(value + b"\n")  # hopefully value is bytes
            sys.stdout.buffer.flush()
        elif isinstance(value, str):
            sys.stdout.write(value + "\n")
            sys.stdout.flush()
        elif isinstance(value, int):
            sys.stdout.write(str(value) + "\n")
            sys.stdout.flush()
        elif isinstance(value, float):
            sys.stdout.write(str(value) + "\n")
            sys.stdout.flush()
        else:
            raise NotImplementedError(type(value))

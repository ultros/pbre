#!/usr/bin/env python3

import importlib
import os


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result}')
        return original_result

    return wrapper


@trace
def get_plugin_names():
    file_list = []
    for files in os.listdir("plugins"):
        if files.endswith(".py") and not files.endswith("__.py"):
            file_list.append(files)

    return file_list


def import_plugin():
    for file in get_plugin_names():
        print(f"[+] Running {file}...")
        plugin_module = importlib.import_module("plugins." + file[:-3])
        plugin = plugin_module.Plugin()
        plugin.main()


# @trace
def main():
    import_plugin()


if __name__ == "__main__":
    main()

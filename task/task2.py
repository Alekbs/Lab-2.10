#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garm(*args):
    if args:
        args = [1 / arg for arg in args]
        return len(args) / sum(args)
    else:
        return None


if __name__ == "__main__":
    print(garm())
    print(garm(2, 2, 5, 1, 4))

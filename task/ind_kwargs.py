#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Сортировка студентов по рейтингу
"""


def stud(**kwargs):
    if kwargs:
        return sorted(kwargs.items(), key=lambda x: x[1], reverse=True)
    else:
        return None


if __name__ == "__main__":
    print(stud(Egor=6, Lera=99, Anton=35))

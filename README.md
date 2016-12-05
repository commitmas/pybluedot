# pybluedot
The Python team project for Commitmas 2016

[![Build Status](https://travis-ci.org/commitmas/pybluedot.svg?branch=master)](https://travis-ci.org/commitmas/pybluedot)

## Introduction

In this year's Commitmas, the Python team will work on a project that makes use of [NASA's APIs](https://api.nasa.gov).

"pybluedot" is a Python library/command-line utility that allows for easy display of NASA data

## Instructions

First, [sign up for a NASA developer key](https://api.nasa.gov/index.html#apply-for-an-api-key) (this will allow you to authenticate to any of NASA's APIs)

> Note that NASA restricts the number of API requests you can make across all of their APIs to 1000 per hour. This should be more than enough for normal testing, but be aware of this in case you try to put an API call into a loop or something like that :smile:

# Design

There are several components that we'll need to create for this project. If you want to take on one of these components, please refer to the links below to navigate to the relevant Github Issue, and let us know there!

- [Configuration system](https://github.com/commitmas/pybluedot/issues/2)
- [Command-line parsing](https://github.com/commitmas/pybluedot/issues/3)
- API bindings (actual functions that represent API endpoints)
- [Unit tests for everything](https://github.com/commitmas/pybluedot/issues/4) (this can be something you take on across all components, or each component developer can write their own tests)

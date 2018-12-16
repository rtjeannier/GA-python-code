---
title: Getting Data
duration: "2:30"
creator:
 name: Joseph Nelson/Mark Mummert
 city: DC
---

# ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Getting Data

This is a big lesson. And it's important.

## Learning Objectives

At the end of this session, you will be able to:
- Describe the basics of HTTP protocol
- Explain what APIs do and why they are increasingly prevalent
- Demonstrate use of APIs
- Demonstrate webscraping using Beautiful Soup

## Overview

By now you should be familiar with how we work with data that's already provided for us. But what happens when we don't have the data that we want?

Today we'll cover two ways to get information from the internet:
- APIs
- Webscraping

Before we dive into these topics, we'll first review HTTP.

## HTTP

Our discussion of how HTTP works is [here](./APIS-HTTP.md)

## Overview of APIs

We'll first run through this [deck](./intro-to-apis.pdf) on why APIs are increasingly prevalent, and their value.


## Using Our First API!

Today we will be working with [SWAPI](https://swapi.co/). It's a very simple database API that is great for beginners.

This API takes some request from our computer, and returns a structured response. In this case, the response is in JSON.

What is an API?

Application Programming Interface
- Structured way to expose specific functionality and data access to users
- Web APIs usually follow the "REST" standard

How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)

The script we'll follow to make requests and use our very first API (gasp!) is available in the code folder.

## Webscraping 101

Now, we'll take a look at collecting data when things are not so neatly structured for us. This is where webscraping comes in.

We'll first be scraping [this](.code/example.html) page. Our script for doing so is available [here](.code/python-webscraping.ipynb)

### Independent Practice

Finally, let's build our **very own** scraper on data from out in the wild.

I'd like you to scrape the first page of quotes from this Lincoln page: http://www.abrahamlincolnonline.org/lincoln/speeches/quotes.htm

Alternatively, scrape from here: http://www.successories.com/iquote/author/291/abraham-lincoln-quotes/1 (preferred)

Add all the quotes to a list.


## Additional Resources

- [Blog post on json with pandas](https://www.dataquest.io/blog/using-json-data-in-pandas/)
- [API article Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface)
- [Programmable web](http://www.programmableweb.com/)
- Please also download [Anaconda with Python 2.7 (not 3.5)](https://www.continuum.io/)
- A [discussion](https://medium.com/ggv-capital/a-tale-of-2-api-platforms-39f8dfd77436#.92bwnnahv) on APIs used properly for development (Slack) vs improperly (Twitter)

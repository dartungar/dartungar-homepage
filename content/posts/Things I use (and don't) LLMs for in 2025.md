---
title: Things I use (and don't) LLMs for in 2025
description: Some use cases for LLMs
summary: It's not an actual intellingence, but it is useful
date: 2025-05-25
draft: false
tags:
  - LLM
  - tools
  - AI
---
LLMs get a lot of hype these days. I don't think they'll be able to replace a proper developer yet - not until they're able to guess people's unexpressed wishes and actually resolve bugs. But they are an excellent tool if you don't expect actual intelligence from them.

In this article, I'll list:

- things that LLMs are a great help for
- things where LLMs can help if used cautiously
- things that LLMs are not ready to do yet (and perhaps never will)

### The Setup

I use [librechat.ai](https://www.librechat.ai/), hosted through [Coolify](https://coolify.io/) on my Hetzner instance. It allows me to use OpenAI, Anthropic, Google, and DeepSeek's models from one interface, build my own agents, and more. API costs are significantly lower than having a subscription - I usually go through $10 in a couple of months. 
I am quite happy with this setup.

Now, to the list!

### The Good

**Kickstarting a task**. LLMs are great for this, especially if you're tired or have a fear of blank page. What I usually do is prompt an LLM with "Hey, I'm starting work on X. (optionally I list my first thoughts and assumptions) What do you think?"

I rarely get something useful from the LLM's answer per se. But I do often get some leads and new thoughts. Sometimes I disagree with the LLM's output and that creates an impulse to think, which is cool.

Mind the anchoring, though.

**Proofreading**. I'm quite confident in my English - too confident, I'd say (I know it's not perfect). Sometimes I run my texts through an LLM just to see if I missed something.

They are also a great source of inspiration - there are times when I want to change the tone of my writing to more/less professional, but don't know where to start. I often ask an LLM to rewrite my text just to get an idea of how my text could look like after I change the tone. This is only for inspiration though - I don't feel right using the LLM's output as is.

**Small refactorings.** Split a huge method into a couple of small ones, abstract an interface, make code more concise and readable, etc - LLMs are pretty good at this, but only when you can tell how good the results are (because sometimes they screw up).

**Writing scripts.** LLMs are awesome for writing short, one-off scripts, especially in Python. Their shortcomings do not come up too much here, and I am usually able to describe what the script needs to do in a few bullet points which keeps the friction low.

### The Sometimes Good

**Looking for information**. I never trust LLMs, because they don't know right from wrong. That's why replacing Google with an LLM is a double-edged sword - it does work fast, but it can give you complete nonsense with the confidence of a 7-year**-old.

Major LLM providers are adding "grounding" in actual internet searches as an inherent feature now, but it still is shaky. LLMs still can't differentiate between a trustworthy source and an obviously untrustworthy one.

What I do for now is use LLMs for search if I have absolutely no idea about the topic I'm searching, and use their output as a starting point. It works...alright, I suppose?

**Summarising.** LLMs are good at this. But to summarise a text is to understand it; if I want to understand a text, I'll try to summarise it myself. Giving the task to an LLM is probably fine for mundane tasks? Although, to be honest, I'd prefer people would write concisely to begin with.

### The Bad

**Working with big context**. Even though some models can hold a medium-sized app in their context now, they are still horrible with anything that actually requires such big context.

There's something missing from LLMs that prevents them from doing a good job with tasks that span across the whole codebase. Maybe this is actual intelligence? Who knows, but I wouldn't even try medium or huge refactorings in enterprise codebases using LLM agents right now. (using LLMs for small tasks on a per-file basis is still great)

**Working with non-mainstream technologies**. I have tried to get LLMs to help with Godot game engine, and it's been pretty awful. Sometimes they mess up different versions of it, sometimes they try to gaslight me into tweaking settings that are not there. Sometimes they work fine, though.

This is somehow mitigated with enabling search.

**Vibe coding.** Maybe my use cases were too niche, or maybe I'm too poor an overseer, but almost every time I tried to get LLMs to write a complete solution it went terribly. Maybe it's the "working with big context" problem all over again.

### Final Thoughts

LLMs are not an AI by any means, but they can make a software engineer's life easier. 
Do not trust them, do not treat them like a human, don't expect reliability and accountability - and you're good.
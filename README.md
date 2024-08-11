# Discord Dataclasses

This Python "_Package_" is made to implement differents things from the Discord API in Python as dataclasses. Goals for
this is to parse JSON data recieved from Flask response (or other user made endpoint) and facilitate work on object sent
by Discord. This is not meant to operate Gateway API.

**Status :** Work in progress ! 🏗️

**I'm not affiliated with Discord.**

## Acknowledgment ⭐️

I would like to thank :

* **Rapptz** – creator of discord.py, the best module for Discord API – who allows me to learn Python years ago. Some of
  his
  work is directly borrowed in this package (seek comments to know) and I presume most of my code imagination could not
  have been there if I didn't first read Rapptz documentation and code.
* **ChatGPT** – Powerful AI tools from OpenAI – which helps me to solve some of my problems, formatting my code, fixing
  my erros and above all doing the sh**ty works when writting enums and other repetitive task.
* **PyCharm** – Excellent Python IDE – which provides me a good environment to work in.

## Roadmap 🎯

* [ ] Create dataclasses for all Discord Objects.
  * [ ] Manage Partial Data
* [ ] Organize Repo.
* [ ] Implement intanciation of dataclasses from json reading. Nested object should become dataclass as they are parsed.
* [ ] Write a ~~good~~ ~~real~~ ~~meaningful~~ correct README.md
  * [ ] _Maybe write a documentation if not lazy_

## History 📖

I was writting a Flask application to make a simple Discord bot that can run slash command, but I was irritated to parse
JSON manually with key provided by the discord documentation. So I decided to create a class for application command
from which I could get information without raising thousands of error as missing key or unexpected. So, reading the
documentation, I created this class, but I realized that the documentation linked much more object to create a slash
command, without that, I couldn't create a class that is stable. Then, I began to create classes for each encountered
objects in the documentation. Later realizing that Rapptz already made this in his repo. I continued anyway as I thought
it could help me to learn coding. I could have saved sevral hours if I remembered it before launching me in that trip.

**Additional information :** Engish is not my native language so semantic errors can be found in this repo and comment may not be translated.


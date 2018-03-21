# pelican-prismjs

[![GitHub license](https://img.shields.io/github/license/EpicSoftworks/pelican-prismjs.svg)](https://github.com/EpicSoftworks/pelican-prismjs/blob/master/LICENSE)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/epicsoftworks)

This plugin brings PrismJS syntax highlighter integration in Markdown for Pelican. Why? PrismJS is lightweight, supports many languages and has a download builder to make your version of PrismJS and not include more than needed. It's pretty good, you can select what you want and go!

## Requirements

There are no additional requirements other than Pelican itself. I wanted to keep things clean and minimal.

## Installation

I have my plugins stored in my home folder. I think it's a nice central place to keep plugins. Adjust the location accordingly when you have a different location.

```
cd ~/pelican-plugins
git clone https://github.com/EpicSoftworks/pelican-prismjs.git
```

Then simply add the following configuration to your `pelicanconf.py`

```
PLUGIN_PATHS = ['/home/rob/pelican-plugins']
PLUGINS = ['pelican-prismjs', 'pelican-other-cool-plugins']
```

After you've added the config the only thing left to do is run `pelican content`

## Examples

I've made a live page with each plugin that requires additional attributes and doesn't purely reply on CSS available for PrismJS on [my blog](). Here are a few quick snippets that make life easier.

#### Line Hightlight
#### Line Numbers
#### Show Invisibles
#### File Hightlighter
#### Show Language
#### JSONP Hightlight
#### Command Line

## Donation

If this project has helped you reduce to develop something then you can show some love and donate a cup of coffee :)

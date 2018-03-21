#!/usr/bin/env python
# -- coding: utf-8 --

from pelican import signals, contents
from os import path
import re

def match_pre_options(string, language):
    # pre-defined list of supported options
    options = [
        'data-user', # commandline plugin
        'data-host', # commandline plugin
        'data-output', # commandline plugin
        'data-src', # file highlight plugin
        'data-label', # toolbar plugin
        'data-line', # line highlight
        'data-start', # line highlight
        'data-language', # show language plugin
        'data-jsonp', # jsonp hightlight
        'data-filename', # jsonp hightlight
        'class' # generic
    ]

    # string we return
    attributes = ''
    commandLine = False

    # loop through valid options
    for option in options:
        regex = r"%"+option+"=([\w,-/ ]+)"
        removal_regex = r"(%"+option+"=[\w,-/ ]+[\r\n]{1})"
        match = re.findall(regex, string)
        #  Check if there is a match
        if (len(match) > 0) or (option == 'class'):
            string = re.sub(removal_regex, '', string)
            if option == 'class':
                additional_classes = ''
                matched = ''
                # Support for command-line class
                if commandLine == True:
                    additional_classes = ' command-line'
                if len(match) > 0:
                    matched = ' ' + match[0]
                attributes = attributes + ' ' + option + '="' + additional_classes + matched + '"'
            else:
                attributes = attributes + ' ' + option + '="' + match[0] + '"'
                # Support for command-line class
                if option in ['data-user', 'data-host', 'data-output']:
                    commandLine = True

    # return attributes
    return [string, attributes]

def convert_code_blocks(content_object):
    # Check if there is content to check
    if content_object._content:
        article = content_object._content
    else:
        return

    # Regex to match code blocks
    code_regex = r"(<code>[\s\S\#\=]*?<\/code>)"
    matches = re.findall(code_regex, article)

    if len(matches) > 0:
        updated_article = article

        # Go through each <pre> element instance that we found above, and parse it:
        for match in matches:
            # try and match the language
            regex_language = r"<code>([\w]+)"
            match_language = re.findall(regex_language, match)
            if len(match_language) > 0:
                language = match_language[0]
            else:
                language = 'none'

            # remove the language from the markdown code block
            regex = r"<code>([\w]+[\r\n]{1})"
            match = re.sub(regex, '', match)
            regex = r"(</code>)"
            match = re.sub(regex, '', match)

            # match attributes and remove them
            match, attributes = match_pre_options(match, language)

            # Replace article with new content
            replacement = '<pre' + attributes + '><code class="language-' + language + '">' + match + '</code></pre>'
            updated_article = re.sub(code_regex, replacement, updated_article, 1)

        # Replace given content
        content_object._content = updated_article

def disable_md_extension(pelican_object):
    pelican_object.settings['MARKDOWN']['extension_configs'] = {}

# Make Pelican work (see http://docs.getpelican.com/en/3.3.0/plugins.html#how-to-create-plugins):
def register():
    signals.initialized.connect(disable_md_extension)
    signals.content_object_init.connect(convert_code_blocks)

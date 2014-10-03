# Sublime NestedSnippet plugin

Nest snippets in your source code; partially replaced by snippet-caller; by
default setup works only for html-code.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

Allows you to nest snippets execute snippet when you are already have snippet
running.


### Usage

  ```
  # type your tab-trigger, e.g.:
  ds| # <- cursor

  # execute snippet
  <div style="|"></div> # <- cursor

  # type another tab-trigger
  <div style="mb|"></div> # <- cursor

  # execute snippet
  <div style="margin-bottom: 10px|"></div> # <- cursor

  # hit "goto next field"
  <div style="margin-bottom: 10px">|</div> # <- cursor
  ```

### Commands

Commands binded in [sublime-snippet-caller](http://github.com/shagabutdinov/sublime-snippet-caller)
plugin in order to avoid kemap conflicts.
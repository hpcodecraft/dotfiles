An extension for [Hyper](https://github.com/zeit/hyper) to replace the cursor with a emoji sequence. Why? Because I was bored.

# Installation

Add `hyper-emoji-cursor` to the `plugins` array of your `.hyper.js` file.

# Options

You may configure the extension by adding a `emojiCursor` object to the `.hyper.js` file's `config` object. Use the following options:

```javascript
emojiCursor: {
  speed: 2000, // length of the sequence in milliseconds
  fontSize: 60, // font size of the emoji in css pixels
  emoji: ['🐱', '🙀', '😾', '😿', '😹', '😼', '😺', '😻', '😸', '😽'] // custom emoji sequence.
},
```

# Simple Debug Log // Python
Author: Darius Strasel @dariusstrasel
# Overview:
A Python library for creating priority-sorted debug logs to support application telemetry.

# How to Use:
Use **debug.info(), debug.api(), or debug.critical()**, the same way you'd use print(). The difference between these three respective methods is their output.

Each of these methods will produce a seperate log file, while also sending their message to STDOUT.

e.g.
```python
debug.critical("This is an example.")
```
Sends the following to your console:
```
2017-05-30 14:26:38.429844: CRITICAL: This is an example.
```
And produces a "CRITICAL.log" at the root directory.

The message format is as follows:

```python
datetime.datetime.now(): debug.priority_map[priority]['message header']"strings and stuff and such"
```

# API:
The API is custimizable! If you'd like to change an existing method, or add your own, do as follows:
    
Add a method:
    
- Add config key to debug.priorirty_map dictionary:
```python
   priority_map = {
        1: {'filename': 'INFO.log', 'message_header': 'INFO'},
        2: {'filename': 'DEBUG.log', 'message_header': 'DEBUG'},
        3: {'filename': 'CRITICAL.log', 'message_header': 'CRITICAL'},
        4: {'filename': 'EXAMPLE.log', 'message_header': 'EXAMPLE',  # This is an example.
    }
```

- Add class method to debug class:
```python
    @classmethod
    def example(self, text):
        example_priority = 0  # This represents the key in the debug.priority_map dictionary.
        return self.__debug_print("%s: %s" % (self.priority_map[example_priority]['message_header'], text), example_priority)
```
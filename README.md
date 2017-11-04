# sublime-openbrowser
Open link on your browser with sublime

# Install
Copy openbrowser.py to your user Packages directory

# Key Binding
```
[
    {"keys" : ["ctrl+alt+g"],"command" : "open_browser", "args" : {"url" : "http://www.google.fr/?q=%s"}},
    {"keys" : ["ctrl+alt+j"],"command" : "open_browser", "args" : {"url" : "http://api.jquery.com/%s"}},
    {"keys" : ["ctrl+alt+w"],"command" : "open_browser", "args" : {"url" : "http://codex.wordpress.org/Function_Reference/%s"}},    
    {"keys" : ["ctrl+alt+y"],"command" : "open_browser", "args" : {"url" : "https://docs.python.org/2/search.html?q=%s"}},
    {"keys" : ["ctrl+alt+m"],"command" : "open_browser", "args" : {"url" : "http://php.net/manual/en/function.%s.php"}},
    {"keys" : ["ctrl+alt+s"],"command" : "open_browser", "args" : {"url" : "http://stackoverflow.com/search?tab=relevance&q=%s"}},
    {"keys" : ["ctrl+alt+e"],"command" : "open_browser", "args" : {"url" : "http://perldoc.perl.org/5.10.1/functions/%s.html"}},

    {"keys" : ["ctrl+alt+r"],"command" : "open_browser", "args" : {"url" : "http://grooveshark.com/#!/search?q=%s"}},

    {"keys" : ["ctrl+alt+o"],"command" : "open_browser", "args" : {"url" : "%s"}}
]
```
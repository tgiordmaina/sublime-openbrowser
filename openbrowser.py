import webbrowser
import sublime, sublime_plugin



class OpenBrowserCommand(sublime_plugin.TextCommand):

    def run(self,edit,url):
        selection = ""
        for region in self.view.sel():
            selection += self.view.substr(region)
        myURL = url % selection;
        if myURL.startswith("http") :
            webbrowser.open(myURL)
        else :
            webbrowser.open( "http://" + myURL )
